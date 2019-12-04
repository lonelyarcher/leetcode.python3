class Solution:
    
    def __init__(self):
        self.cache = {}
    
    def numPermsDISequence(self, S):
        """
        :type S: str
        :rtype: int
        """
        if len(S) == 1:
            return [[1, 0]] if S == 'D' else [[0, 1]]
        ans = []
        if S in self.cache:
            return self.cache[S]
        
        for i in range(len(S) + 1):
            if i == 0 and S[i] == 'D':
                for arr in self.numPermsDISequence(S[1:]):
                    ans.append([len(S)] + arr)
            elif i == len(S) and S[i - 1] == 'I':
                for arr in self.numPermsDISequence(S[:-1]):
                    ans.append(arr + [len(S)])
            elif S[i - 1] == 'I' and S[i] == 'D':
                for arr in self.numPermsDISequence(S[:i - 1] + 'D' + S[i + 1:]):
                    arr.insert(i, len(S))
                    ans.append(arr)
                for arr in self.numPermsDISequence(S[:i - 1] + 'I' + S[i + 1:]):
                    arr.insert(i, len(S))
                    ans.append(arr)
               
        
            
        self.cache[S] = ans
        return ans


a = set(Solution().numPermsDISequence('IDDDIIDIIIIIIIIDIDID'))
print( len(a) )