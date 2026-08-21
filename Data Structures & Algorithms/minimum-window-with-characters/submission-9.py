class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)> len(s):
            return ""

        tProf = Counter(t)
        windowProf = defaultdict(int)
        left = 0
        ans = ""
        best= float("inf")
        have, needed = 0, len(tProf.keys())
        
        for right in range(len(s)):
            windowProf[s[right]] += 1  
            # random char case 
            if s[right] not in tProf: 
                continue

            # satasfied for char
            if windowProf[s[right]] == tProf[s[right]]: 
                have += 1 
                # all satasfied 

            while s[left] not in tProf or windowProf[s[left]] > tProf[s[left]]:
                windowProf[s[left]] -= 1
                if  windowProf[s[left]] == 0:
                    del windowProf[s[left]]

                left += 1 

            if have == needed:
                if best >= right - left + 1:
                    ans = s[left: right + 1]
                    best = right - left + 1
        
        return ans 