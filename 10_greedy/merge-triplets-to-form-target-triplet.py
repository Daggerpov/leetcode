"""
- Go through triplets
- Firstly, disqualify any triplet that has any value that's greater than the target's
  value at that index, since if it's had an operation applied to it max(triplet1,
  triplet2), then it'll yield a value that won't ever be reversible in leading to the
  target
- Then, see if that triplet has a useful value, a.k.a. a value that's equal to the
  target's value at that index
- Add that index to our set (must be a set to handle duplicates) of good indices
- If len(goodIndices) == 0 at the end of all iterations through triplets, then we've
  found the triplets we need to form target through this maximizing operation
"""
