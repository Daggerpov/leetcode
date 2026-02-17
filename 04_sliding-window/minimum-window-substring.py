"""
Initialize the countT hashmap of counts for each character by countT[c] = 1 + countT.get(c, 0)

Initially, before looping through the s with left and right pointers, we have 0 of the char counts
we need (e.g. we need 2 'X's. Increment the current char count of our window's char counts,
window[c] = 1 + window.get(c, 0). Then, see if that character we just added is needed (in countT)
and window[c] == countT[c], meaning we have all of it that we need → increment have += 1.
While we have the characters we need:

- found = True
- We can overwrite our resLen if our current substring length, r - l + 1 is less, as well as
  our res = [l, r] pointers
- If the left-most char is required to keep up the condition
  if s[l] in countT and window[s[l]] < countT[s[l]], then have -= 1
- we can shrink down the window size from incrementing the left pointer.

At the end, we're returning the subString from s[l: r+1] if found (if we ever had what we
needed (len(countT))).
"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT, window = {}, {}
        # construct T counts
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        # we need all chars in count t (ignoring count of char)
        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")
        found = False
        l = 0
        for r in range(len(s)):
            # get the char at r's position in s, and
            # increase that char's count in window counts
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            # if we've got as many of c as we need
            if c in countT and window[c] == countT[c]:
                have += 1

            # while we've got everything we need
            # try to shrink the window
            while have == need:
                found = True
                # overwrite resLen if smaller
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                # try to shrink window from left
                window[s[l]] -= 1
                # if we no longer have as many of s[l] as
                # we need in the window
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l : r + 1] if found else ""
