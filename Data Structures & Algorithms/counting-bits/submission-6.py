class Solution:
    def countBits(self, nums: int) -> List[int]:
        ans = []
    
        for n in range(nums + 1): 
            cnt = 0
            while n: 
                n, r = divmod(n, 2)
                if r: 
                    cnt +=1 
            
            ans.append(cnt)

        return ans