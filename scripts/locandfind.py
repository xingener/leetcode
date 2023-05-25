import numpy as np
from typing import List

class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        am = np.array(matrix)
        if am.size == 0:
            return False

        return self.loc_find(am, target)
        # if a_result.size: return True
        # else: return False

    def loc_find(self, m, target: int) -> List :
        diag = m.diagonal()
        i = np.searchsorted(diag, target)
        # 切出来4个矩阵
        _ = m[:i, :i]
        a = m[i:, i:]
        b = m[:i, i:]
        c = m[i:, :i]

        if a.size:
            if a[0, 0] == target:
                return True

        if b.size:
            r_b = self.loc_find(b, target)
            if r_b:
                return r_b

        if c.size:
            r_c = self.loc_find(c, target)
            if r_c:
                return r_c

        return False

if __name__ == "__main__":
    matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
    target = 13
    s = Solution()
    print(s.findNumberIn2DArray(matrix, target))
