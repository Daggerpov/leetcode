class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False # state for if we're at a word? 

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for character in word:
            if character not in cur.children:
                cur.children[character] = TrieNode()
            cur = cur.children[character]
        
        cur.word = True

    def search(self, word: str) -> bool:
        def dfs(j, root):
            cur = root

            # iterate through remaining chars in word
            # from current index, j
            for i in range(j, len(word)):
                curChar = word[i]
                if curChar == ".":
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            # found exact word
                            return True
                    return False
                else:
                    if curChar not in cur.children:
                        return False
                    cur = cur.children[curChar]
            return cur.word
        
        return dfs(0, self.root)
