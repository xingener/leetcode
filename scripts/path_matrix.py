import numpy as np
from typing import List
from copy import deepcopy

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        len_word = len(word)
        if len_word <= 0:
            return False
        a_board = np.array(board) # prepare board matrix
        l_j, l_i = np.where(a_board == word[0]) #find locations of 1st letter
        if l_i.size:
            word = word[1:]
            for j, i in zip(l_j, l_i):
                loc = [j, i] # prepare loc
                result = self._find_next(a_board, loc, word)
                # print(result)
                if result == True:
                    return result
        return False


    def _find_next(self, a_board: np.array, loc: List, word: str) -> bool:
        if len(word) <= 0: return True
        
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
                a_board_n = deepcopy(a_board) # update a_board
                a_board_n[j, i] = ''
                # print(a_board)
                if ix == 0:
                    loc = [j-1, i] # update loc
                elif ix == 1:
                    loc = [j, i+1]
                elif ix == 2:
                    loc = [j+1, i]
                elif ix == 3:
                    loc = [j, i-1]
                word_n = word[1:] # update word
                result = self._find_next(a_board_n, loc, word_n) # find next letter
                if result == True:
                    return result
        return False
