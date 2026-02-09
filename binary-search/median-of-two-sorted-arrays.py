class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        len1, len2 = len(nums1), len(nums2)
        i = j = 0
        median1 = median2 = 0

        for count in range((len1 + len2) // 2 + 1):
            # in event-length len1 + len2 case
            median2 = median1
            if i < len1 and j < len2:
                # grab min
                # and shift that list's pointer
                if nums1[i] > nums2[j]:
                    median1 = nums2[j]
                    j += 1
                else:
                    median1 = nums1[i]
                    i += 1
            # if j has reached len2
            elif i < len1:
                median1 = nums1[i]
                i += 1
            # if i has reached len1
            else:
                median1 = nums2[j]
                j += 1

        if (len1 + len2) % 2 == 1:
            return float(median1)
        else:
            return (median1 + median2) / 2.0

# Alternative solution:

class Solution:
    def get_kth(self, a: List[int], m: int, b: List[int], n: int, k: int, a_start: int = 0, b_start: int = 0) -> int:
        if m > n:
            return self.get_kth(b, n, a, m, k, b_start, a_start)
        if m == 0:
            return b[b_start + k - 1]
        if k == 1:
            return min(a[a_start], b[b_start])

        i = min(m, k // 2)
        j = min(n, k // 2)

        if a[a_start + i - 1] > b[b_start + j - 1]:
            return self.get_kth(a, m, b, n - j, k - j, a_start, b_start + j)
        else:
            return self.get_kth(a, m - i, b, n, k - i, a_start + i, b_start)

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        left = (len(nums1) + len(nums2) + 1) // 2
        right = (len(nums1) + len(nums2) + 2) // 2
        return (self.get_kth(nums1, len(nums1), nums2, len(nums2), left) +
                self.get_kth(nums1, len(nums1), nums2, len(nums2), right)) / 2.0
