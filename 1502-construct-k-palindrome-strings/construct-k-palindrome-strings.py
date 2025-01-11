class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s)<k:
            return False
        
        c=Counter(s)
        odd_freq = sum(i%2 for i in c.values())
        return odd_freq<=k