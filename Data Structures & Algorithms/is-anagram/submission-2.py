class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s)!=len(t):
        #     return False
        # if sorted(s)==sorted(t):
        #     return True
        # else:
        #     return False

        ds={}
        dt={}
        if len(s)!=len(t):
            return False

        for i in range(len(s)):
            ds[s[i]]=1+ds.get(s[i],0)
            dt[t[i]]=1+dt.get(t[i],0)
        
        for k,v in ds.items():
            if v!=dt.get(k, 0):
                return False
        return True