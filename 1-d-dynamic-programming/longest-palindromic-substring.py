"""
Go through the string, expanding the current substring from setting both the left and
right pointers as the current index, over-writing the longest palindromic substring if
the current substring length is greater. Then, do the same, but for even-length
substrings, by setting l, r = i, i + 1. Finally, return the longest palindromic
substring.
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        resIdx = 0
        resLen = 0

        for i in range(len(s)):
            # odd length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resIdx = l
                    resLen = r - l + 1
                l -= 1
                r += 1

            # even length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resIdx = l
                    resLen = r - l + 1
                l -= 1
                r += 1

        return s[resIdx : resIdx + resLen]

# Alternative solution:

class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.resIdx = 0
        self.resLen = 0

        for i in range(len(s)):
            self.expandOutward(s, i, False)
            self.expandOutward(s, i, True)
            
        return s[self.resIdx : self.resIdx + self.resLen]
    
    def expandOutward(self, s: str, i: int, isEven: bool) -> None:
        l = i 
        r = i + 1 if isEven else i # only difference

        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > self.resLen:
                self.resIdx = l
                self.resLen = r - l + 1
            l -= 1
            r += 1

        return
