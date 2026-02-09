"""
At every iteration, see if current substring length, r - l + 1 (diff in indexes + 1, for size)
can overwrite longest (eventually return). If the newest character that s[r] reaches is in
charsSeen = set(), then remove the left-most character (charsSeen.remove(s[l])), and shift left
pointer one over → do in while loop until s[r] isn't in charsSeen, then add that into charsSeen.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charsSeen = set()
        longest = 0
        l = 0
        for r, char in enumerate(s):
            #remove left-most char until this duplicate char is removed from hashset
            while char in charsSeen:
                charsSeen.remove(s[l])
                l += 1

            charsSeen.add(char) #safe to add; know it won't be duplicated
            longest = max(longest, r - l + 1)

        return longest
