"""
Keep track of highest frequency character, maxF. Keep a hashMap of char counts in counts = {},
and for each char seen by r pointer, counts[s[r]] = 1 + counts.get(s[r], 0). Then, see if that
char count, counts[s[r]] overwrites maxF. If the length of the current substring - maxF exceeds k,
that means we've had to make too many swaps (what we calculated is otherCharCount) → therefore,
we need to move the left pointer rightward and remove its char from counts. After checking that,
it's guaranteed to be a valid substring with at most k swaps, so possibly check to overwrite longest
"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charCounts = defaultdict(int)

        l = 0
        maxf = 0
        longest = 0
        for rIndex, rChar in enumerate(s):
            charCounts[rChar] += 1
            maxf = max(maxf, charCounts[rChar])

            # maxf is essentially the allowance of how
            # many swaps we can make, since it's the
            # charCounts of the most frequent element
            if (rIndex - l + 1) - maxf > k:
                # if we've 'ran out of swaps'
                # shrink window from left
                charCounts[s[l]] -= 1
                l += 1

            subStringSize = rIndex - l + 1
            longest = max(subStringSize, longest) # + 1 - 1 is redundant, but for clarity that it's size

        return longest
