class TrieNode:
    def __init__(self):
        self.children = [None] * 26 # storing children as indexes in array as opposed to hashmap for O(26) = O(1) instead of O(n) memory
        self.idx = -1 # index in the array of words input
        self.refs = 0 # how many children are in this trie node, to avoid extra searches

    def addWord(self, word, i):
        cur = self
        cur.refs += 1
        for c in word:
            index = ord(c) - ord('a')
            if not cur.children[index]:
                cur.children[index] = TrieNode()
            cur = cur.children[index]
            cur.refs += 1 # refers to an extra word now
        cur.idx = i # index of word in input array of words

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for i in range(len(words)):
            root.addWord(words[i], i)

        ROWS, COLS = len(board), len(board[0])
        res = []

        # helper for getting index in array from char
        def getIndex(c):
            index = ord(c) - ord('a')
            return index

        def dfs(r, c, node):
            # bounds check, ensure not visited ("*"), ensure in children array
            if (r < 0 or c < 0 or r >= ROWS or
                c >= COLS or board[r][c] == '*' or
                not node.children[getIndex(board[r][c])]):
                return

            tmp = board[r][c]
            board[r][c] = '*' # set visited
            prev = node
            node = node.children[getIndex(tmp)] # move pointer forward in trie
            if node.idx != -1:
                res.append(words[node.idx]) # found word
                node.idx = -1
                node.refs -= 1 # decrease refs, since this word now doesn't need to be found
                if not node.refs:
                    prev.children[getIndex(tmp)] = None
                    node = None
                    board[r][c] = tmp
                    return

            dfs(r + 1, c, node)
            dfs(r - 1, c, node)
            dfs(r, c + 1, node)
            dfs(r, c - 1, node)

            board[r][c] = tmp

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root)

        return res
