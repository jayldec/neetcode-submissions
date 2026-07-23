
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        
        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]   # valid palindrome substring
        
        for i in range(len(s)):
            # Odd length palindrome
            p1 = expand(i, i)
            # Even length palindrome
            p2 = expand(i, i+1)
            
            # Take the longer palindrome
            res = max(res, p1, p2, key=len)
        
        return res
