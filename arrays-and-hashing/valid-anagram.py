"""
counts lists of [0] * 26 for every letter of alphabet. Loop through first string, adding to counts at the right index by doing counts[ord(char) - ord("a")] (difference in ASCII value from char to a will give proper index in counts. Then, loop through other string, decrementing that count at that char's index in counts. Then, loop through counts -> if there's a count != 0, then return False. Otherwise, return True.
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # hash set - optimal O(26) -> O(1) memory
        if len(s) != len(t):
            return False

        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1

        for val in count:
            if val != 0:
                return False
        return True
