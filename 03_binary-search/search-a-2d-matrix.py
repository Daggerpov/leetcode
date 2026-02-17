class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 1. Find which sub-array the target is in, so binary search 
        # using the first element of each sub-array

        # Notes: 
        # - matrix implies that each sub-array is of the same length
        # - target is reasonable int

        left, right = (0, len(matrix) - 1) 

        sub_list_index = 0
        
        while left <= right:
            median_index = (left + right) // 2 # represents subList index
            
            # matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
            # target = 5

            # -> median_index = 1 ([4, 5, 6])

            if matrix[median_index][0] > target: # 
                # need to look only at the current median sublist and left of that
                # therefore, we can adjust the right pointer to the median sublist
                right = median_index - 1
            elif matrix[median_index][-1] < target: # 
                # need to look only at the current median sublist and right of that
                # therefore, we can adjust the left pointer to the median sublist
                left = median_index + 1
            else:
                sub_list_index = median_index # target must be in this sublist, if it does exist
                break

        # returns whether the target is in the sublist
        # since, we could've found earlier that it should be 
        # in this sublist but aren't actually sure if it is
        left, right = 0, len(matrix[sub_list_index]) - 1

        while left <= right:
            median_index = (left + right) // 2 # represents subList index

            cur_element = matrix[sub_list_index][median_index] 

            if cur_element > target: # 
                right = median_index - 1
            elif cur_element < target: # 
                left = median_index + 1
            else:
                if cur_element == target:
                    return True
                else:
                    return False
        
        return False

# Alternative solution:

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        l, r = 0, ROWS * COLS - 1
        while l <= r:
            m = l + (r - l) // 2
            row, col = m // COLS, m % COLS
            if target > matrix[row][col]:
                l = m + 1
            elif target < matrix[row][col]:
                r = m - 1
            else:
                return True
        return False
