class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d_s={}
        d_t={}
        if len(s)!=len(t):
            return False
        if sorted(s)==sorted(t):
            return True
        else:
            return False