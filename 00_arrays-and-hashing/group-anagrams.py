"""
Iterate through every string, populating counts (just like in Valid Anagram) -> append it to the res defaultdict(list) at the index of the tuple of the counts. So, anagrams will be grouped in a hashmap of the indexes being tuples of counts (i.e. {[1, 1, 1, 0, ..., 0]: 'cab', 'acb'})

Therefore, return [res.values()] since the values will be the word groups

Remember to do res[tuple(count)] as the index, not res[list(count)] since indexes have to be immutable.
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # to avoid issues with unknown indexes
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            
            res[tuple(count)].append(s)
        return list(res.values())
