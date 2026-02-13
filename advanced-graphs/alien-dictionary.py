from collections import deque
from typing import List


class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        charAdjList = {c: [] for w in words for c in w}
        inDegrees = {c: 0 for c in charAdjList}

        # form adj list
        for i in range(0, len(words) - 1):
            word1, word2 = words[i], words[i+1]

            minLength = min(len(word1), len(word2))

            # explicit exception based on question
            # i.e. can't have word with same prefix but longer length first
            if len(word1) > len(word2) and word1[:minLength] == word2[:minLength]:
                return "" # invalid

            for j in range(minLength):
                # as soon as there's a different char, that's what we compare using
                if word1[j] != word2[j]:
                    charAdjList[word1[j]].append(word2[j])
                    # pointed at
                    inDegrees[word2[j]] += 1
                    break # no longer need to compare

        # keep decreasing indegrees, popping elements that are 
        # no longer being pointed to (in degree == 0)

        q = deque([c for c in inDegrees if inDegrees[c] == 0])
        res = []

        while q:
            curChar = q.popleft()
            res.append(curChar)

            for neighbour in charAdjList[curChar]:
                inDegrees[neighbour] -= 1
                # no longer being pointed to
                if inDegrees[neighbour] == 0:
                    q.append(neighbour)

        if len(res) != len(inDegrees):
            return "" # invalid, since we must've found a cycle
            
        return "".join(res) # 

