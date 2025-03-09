import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
from torch.utils.data import Dataset, DataLoader
import re
from collections import Counter


class TextDataset(Dataset):
    def __init__(self, file_path, max_seq_length):
        self.max_seq_length = max_seq_length
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read().lower()
        
        # Tokenize the text
        self.tokens = re.findall(r'\w+', text)
        print(self.tokens)
        
        # Build vocabulary
        self.vocab = Counter(self.tokens)
        self.vocab = sorted(self.vocab, key=self.vocab.get, reverse=True) + ['<unk>']
        self.vocab_size = len(self.vocab)
        self.word_to_idx = {word: idx for idx, word in enumerate(self.vocab)}
        self.idx_to_word = {idx: word for idx, word in enumerate(self.vocab)}
        
        # Convert tokens to indices
        self.data = [self.word_to_idx[word] for word in self.tokens]
        
    def __len__(self):
        return len(self.data) - self.max_seq_length  
    
    def __getitem__(self, idx):
        # Randomly sample a sequence length between 1 and max_seq_length
        seq_length = torch.randint(1, self.max_seq_length + 1, (1,)).item()
        seq = self.data[idx:idx + seq_length]
        target = self.data[idx + seq_length]
        return torch.tensor(seq, dtype=torch.long), torch.tensor(target, dtype=torch.long)


class SimpleTransformer(nn.Module):
    def __init__(self, vocab_size, embed_dim, num_heads, num_layers, max_seq_length):
        super(SimpleTransformer, self).__init__()
        self.embedding = nn.Embedding(vocab_size, embed_dim)
        self.positional_encoding = nn.Parameter(torch.zeros(1, max_seq_length, embed_dim))
        self.transformer = nn.Transformer(d_model=embed_dim, nhead=num_heads, num_encoder_layers=num_layers)
        self.fc = nn.Linear(embed_dim, vocab_size)
    
    def forward(self, x, mask):
        seq_length = x.size(1)
        x = self.embedding(x) + self.positional_encoding[:, :seq_length, :]
        
        # Transpose x to (sequence_length, batch_size, embed_dim) for Transformer
        x = x.permute(1, 0, 2)
        
        # Pass the mask to the Transformer
        output = self.transformer(x, x, src_key_padding_mask=~mask.bool())  # Apply mask
        
        # Transpose back to (batch_size, sequence_length, embed_dim)
        output = output.permute(1, 0, 2)
        
        # Predict the next word (use the last token's output)
        output = self.fc(output[:, -1, :])
        return output
    
def train(model, dataloader, criterion, optimizer, device):
    model.train()
    total_loss = 0
    for batch_idx, (data, target, mask) in enumerate(dataloader):
        data, target, mask = data.to(device), target.to(device), mask.to(device)
        optimizer.zero_grad()
        output = model(data, mask)
        loss = criterion(output, target)
        loss.backward()
        optimizer.step()
        total_loss += loss.item()
    return total_loss / len(dataloader)

def predict(model, input_text, dataset, device, max_seq_length):
    model.eval()
    tokens = re.findall(r'\w+', input_text)
    token_ids = [dataset.word_to_idx.get(token,  dataset.word_to_idx["<unk>"]) for token in tokens]
    # Truncate or pad the sequence to max_seq_length
    if len(token_ids) > max_seq_length:
        token_ids = token_ids[-max_seq_length:]  # Truncate to the last max_seq_length tokens
    else:
        token_ids = [0] * (max_seq_length - len(token_ids)) + token_ids  # Pad with zeros
    
    # Convert to tensor and add batch dimension
    input_seq = torch.tensor([token_ids], dtype=torch.long).to(device)
    
    # Create a mask (all ones since there's no padding in this case)
    mask = (input_seq != 0).float().to(device)
    
    # Predict the next word
    with torch.no_grad():
        output = model(input_seq, mask)
        predicted_token_id = torch.argmax(output, dim=1).item()
    
    # Convert the predicted token ID back to a word
    predicted_word = dataset.idx_to_word.get(predicted_token_id, '<unk>')
    
    return predicted_word

def collate_fn(batch):
    # Separate sequences and targets
    sequences, targets = zip(*batch)
    
    # Pad sequences to the maximum length in the batch
    padded_sequences = torch.nn.utils.rnn.pad_sequence(sequences, batch_first=True, padding_value=0)
    
    # Create a mask for padding tokens
    mask = (padded_sequences != 0)  # Boolean mask
    mask = mask.float()  # Convert to float (1 for real tokens, 0 for padding)
    
    # Convert targets to a tensor
    targets = torch.tensor(targets, dtype=torch.long)
    
    return padded_sequences, targets, mask

def main():
    # Hyperparameters
    file_path = 'training.txt'
    max_seq_length = 10
    batch_size = 32
    embed_dim = 64
    num_heads = 4
    num_layers = 2
    learning_rate = 0.001
    num_epochs = 10
    
    # Load dataset
    dataset = TextDataset(file_path, max_seq_length)
    dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True, collate_fn=collate_fn)
    
    # Initialize model, loss, and optimizer
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model = SimpleTransformer(dataset.vocab_size, embed_dim, num_heads, num_layers, max_seq_length).to(device)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=learning_rate)
    
    # Training loop
    for epoch in range(num_epochs):
        loss = train(model, dataloader, criterion, optimizer, device)
        print(f'Epoch {epoch+1}/{num_epochs}, Loss: {loss:.4f}')
    
    # Save the model
    torch.save(model.state_dict(), 'transformer_model.pth')

    # predict 

    input_text = "I love you"
    predicted_word = predict(model, input_text, dataset, device, max_seq_length)
    print(f"Input: '{input_text}' -> Predicted next word: '{predicted_word}'")
    



if __name__ == '__main__':
    main()