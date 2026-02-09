"""
Cycle sort

- Assuming every number needs to be in its position, with 1-based indexing
  (e.g. [1, 2, 3, 4, 5, ...])
- If nums[i] != nums[correctIndex] where correctIndex is nums[i] - 1 (where the
  nums[i] should be) -> swap nums[i] with nums[correctIndex]
    - If that's the case again, keep swapping -> don't increment i
    - Otherwise, keep going through the list
- Go through for index, num in enumerate(nums)
    - Return index + 1 if num != index + 1 (it's not the num that should be there)
    - If done iterating -> return len(nums) + 1 since it must be the next one
"""
