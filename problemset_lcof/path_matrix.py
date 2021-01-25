import numpy as np
from typing import List

class Solution:
    """
        origin url: https://leetcode-cn.com/problems/ju-zhen-zhong-de-lu-jing-lcof/
    """
    def exist(self, board: List[List[str]], word: str) -> bool:
        len_word = len(word)
        if len_word <= 0:
            return Fasle
        a_board = np.array(board) # prepare board matrix
        l_j, l_i = np.where(a_board == word[0]) #find locations of 1st letter
        if l_i.size:
            word = word[1:]
            for j, i in zip(l_j, l_i):
                print('new start')
                loc = [j, i] # prepare loc
                result = self._find_next(a_board, loc, word)
                if result == True:
                    return result
        return False


    def _find_next(self, a_board: np.array, loc: List, word: str) -> bool:
        if len(word) <= 0: return True
        print(loc)
        print(a_board)
        j, i = loc
        tmp_l = list('    ') #prepare tmp list to store lets near the let in loc
        if j > 0:
            tmp_l[0] = a_board[j-1, i]
        if j < a_board.shape[0] - 1:
            tmp_l[2] = a_board[j+1, i]
        if i < a_board.shape[1] - 1:
            tmp_l[1] = a_board[j, i+1]
        if i > 0:
            tmp_l[3] = a_board[j, i-1]
        # find next let's location
        for ix in range(len(tmp_l)):
            let = tmp_l[ix]
            if let == word[0]:
                a_board_n = a_board # update a_board
                a_board_n[j, i] = ''
                # print(a_board)
                if ix == 0:
                    loc_n = [j-1, i] # update loc
                elif ix == 1:
                    loc_n = [j, i+1]
                elif ix == 2:
                    loc_n = [j+1, i]
                elif ix == 3:
                    loc_n = [j, i-1]
                word_n = word[1:] # update word
                result = self._find_next(a_board_n, loc_n, word_n) # find next letter
                if result == True:
                    return result
        return False


if __name__ == "__main__":
    # board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    # word = 'ABCCED'
    board = [["C","A","A"],
             ["A","A","A"],
             ["B","C","D"]]
    word = "AAB"

    s = Solution()
    is_exist = s.exist(board, word)
    print(is_exist)
