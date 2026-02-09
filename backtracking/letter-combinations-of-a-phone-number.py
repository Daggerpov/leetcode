class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        if not digits:
            return res

        def backtrack(i, curStr):
            if len(curStr) == len(digits): # done
                res.append(curStr)
                return
            else:
                for char in digitToChar[digits[i]]:
                    backtrack(i + 1, curStr + char)
        backtrack(0, "")

        return res
