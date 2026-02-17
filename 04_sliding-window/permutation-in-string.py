"""
See recent code | did dry-run perfectly
"""

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # permutation means same char counts
        if len(s1) > len(s2):
            # impossible for s1 to be in s2
            return False

        # e.g. [1, 2, 0] represents 'bab', since char count of a is 1, and b is 2
        s1CharCounts = [0] * 26 # array with each index being the ASCII value of the char
        windowCharCounts = [0] * 26

        for index in range(len(s1)): # e.g. s1 = 'abc' len is 3 so range(0, 2)
            # char = s1[index]
            s1CharCounts[ord(s1[index]) - ord("a")] += 1
            # char in s2 = s2[index]
            windowCharCounts[ord(s2[index]) - ord("a")] += 1

        if s1CharCounts == windowCharCounts:
            return True # s1 permutation is in s2 since identical charCounts at this point

        l = 0
        # go through rest of s2
        for r in range(len(s1), len(s2)): # end index non-inclusive | range(3, 6) s2 = 'lecabee' so last index
            # chop off left side elem:
            windowCharCounts[ord(s2[l]) - ord("a")] -= 1
            l += 1 # keeping sliding window size of s1 by moving both left and right

            windowCharCounts[ord(s2[r]) - ord("a")] += 1

            # find good window, i.e. permutation of s1 in s2
            if s1CharCounts == windowCharCounts:
                return True

        return False
