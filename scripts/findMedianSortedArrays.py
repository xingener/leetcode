from typing import List


def find_median(nums1: List[int], nums2: List[int]) -> int:
    n1, n2 = len(nums1), len(nums2)

    def get_kth_element(k: int) -> int:
        i1, i2 = 0, 0
        while k != 0:
            if i1 == n1:
                return nums2[i2 + k - 1]
            if i2 == n2:
                return nums1[i1 + k - 1]
            if k == 1:
                return min(nums1[i1], nums2[i2])

            new_i1 = min(i1 + k//2 - 1, n1 - 1)
            new_i2 = min(i2 + k//2 - 1, n2 - 1)
            pivot_1, pivot_2 = nums1[new_i1], nums2[new_i2]
            if pivot_1 <= pivot_2:
                k -= (new_i1 - i1 + 1)
                i1 = new_i1 + 1
            else:
                k -= (new_i2 - i2 + 1)
                i2 = new_i2 + 1

    n = n1 + n2
    if n % 2 == 1:
        return get_kth_element((n+1) // 2)
    else:
        return get_kth_element(n // 2)