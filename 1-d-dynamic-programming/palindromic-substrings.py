"""
Same idea as with Longest Palindromic Substring, but incrementing res every time a
palindrome is counted (whenever s[l] == s[r])
"""

class Solution:

    def countSubstrings(self, s: str) -> int:
        self.res = 0

        for i in range(len(s)):
            self.countPali(s, i, i)
            self.countPali(s, i, i + 1)
        return self.res

    # affects self.res
    def countPali(self, s, l, r) -> None:
        while l >= 0 and r < len(s) and s[l] == s[r]:
            self.res += 1
            l -= 1
            r += 1
        return
