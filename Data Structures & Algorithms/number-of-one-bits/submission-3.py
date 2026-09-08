class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        while n: 
            n, r = divmod(n, 2)
            if r:
                cnt +=1 
                
        return cnt