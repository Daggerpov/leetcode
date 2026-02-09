class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        curPartitions = [] # partitions of current recursive stack calls

        def backtrack(i): 
            # once done
            if i >= len(s):
                res.append(curPartitions.copy())
                return

            # for however many choices are left, 
            for charIndex in range(i, len(s)): # 0, max index 
                if self.isPalindrome(s, i, charIndex):
                    curPartitions.append(s[i: charIndex + 1])
                    backtrack(charIndex + 1)
                    curPartitions.pop()

        backtrack(0)

        return res

    def isPalindrome(self, s, l, r):
        if l >= r:
            return True # I'll have checked every start<-> end pair of chars
        if s[l] != s[r]:
            return False # not a palindrome, stop looking
        return self.isPalindrome(s, l + 1, r - 1)
