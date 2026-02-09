class PrefixNode:
    def __init__(self):
        self.end = False
        # representing the possible children of all different letters 
        # self.children = [None] * 26 # [None, None, (x 13)]
        self.children = {} # I like this implementation better than the 26-array

class PrefixTree:
    def __init__(self):
        # not sure
        self.root = PrefixNode()

    def insert(self, word: str) -> None:
        # for char in word:
        #     index = ord(char) - ord('a')
        #     if not self.root.children[index]: # == None
        #         self.root.children[index] = PrefixTreeNode()
        #     self.root =
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = PrefixNode()
            cur: PrefixNode() = cur.children[char] # will be a PrefixNode()
        cur.end = True

    def search(self, word: str) -> bool:
        cur = self.root
        for char in word:
            if char not in cur.children:
                return False
            cur = cur.children[char]
        if cur.end:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for char in prefix:
            if char not in cur.children:
                return False
            cur = cur.children[char]
        return True
