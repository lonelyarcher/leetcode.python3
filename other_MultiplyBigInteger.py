class Solution():
    def multiply(self, num1, num2):
        num1, num2 = num1[::-1], num2[::-1]
        res = [0] * (len(num1) + len(num2) + 1)
        for i in range(len(num1)):
            for j in range(len(num2)):
                prod = int(num1[i]) * int(num2[j])
                res[i + j] += prod
                res[i + j + 1] += res[i + j] // 10 # no need to consider i+j+1 will overflow, because if will be considered later 
                res[i + j] = res[i + j] % 10
        while len(res) > 1 and res[-1] == 0: res.pop() 
        return "".join([str(i) for i in res])[::-1].lstrip("0")
#test
print(Solution().multiply("77","99"))
# remove by value, 
# del by index without returning, 
# pop by index with returning and default pop the last index
# strip(""): remove the leading or tailing space, rstrip tailing, lstrip leading.