# Implement the RandomizedSet class:

# RandomizedSet() Initializes the RandomizedSet object.

# bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise. -> was present

# bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.

# int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.

# You must implement the functions of the class such that each function works in average O(1) time complexity.

# --------

# set = {1, 5, 3, 9} -> 25 % chance of getting any one of them

# can use random 

# insert: check if exists, O(1) -> insert O(1)

# remove: check if exists, O(1) -> remove O(1)

# getRandom(): compute a random number, assigning probabilities for each num in set -> O(1), lookup O(1)

# random.randint(0, len(set)) -> 

# naive solution:

# getRandom() -> loop through the set, O(n) -> computed index to pick the num

import random

class RandomizedSet:
    def __init__(self):
        self.random_set = set()
        self.vals_array = []
        
        # other DS:
        # array, hashmap, or hashset for O(1) lookup
        
    # O(1)
    def insert(self, val: int) -> bool:
        # insert at end

        if val in self.random_set:
            return False
        self.random_set.add(val)
        return True
        
    # O(1)
    def remove(self, val: int) -> bool:
        # swap removal element with last good element
        # keep track of index of last good element

        # pop last
        if val in self.random_set:
            self.random_set.remove(val)
            return True
        return False

    # O(n) -> loop through set
    def getRandom(self) -> int:
        vals = []
        length = 0 
        # ensured uniqueness, therefore probability
        for val in self.random_set:
            vals.append(val)
            length += 1
        
        return vals[random.randint(0, length)]

# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
param_1 = obj.insert(1)
print(param_1) # true
param_1 = obj.insert(1)
print(param_1) # false
param_2 = obj.remove(1) # true
param_2 = obj.remove(1) # false
param_3 = obj.getRandom()

# feedback

# - constraints
# - 

# range of vals
# if nulls
# number of operations per function -> optimization focus
# {} 
