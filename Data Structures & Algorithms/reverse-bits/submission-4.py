class Solution:
    def reverseBits(self, n: int) -> int:
        ans = []
        for i in range(32): 
            n, r = divmod(n, 2)
            ans.append(r)

        print(ans)

        a = 0
        for i in range(31,-1, -1):
            
            if ans[32-i-1]:
                a+= 2**i
        
        return a