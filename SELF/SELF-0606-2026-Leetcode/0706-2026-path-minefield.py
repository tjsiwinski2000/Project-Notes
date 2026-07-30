# You are given an m x n binary matrix grid and an integer health.

# You start on the upper-left corner (0, 0) and would like to get to the lower-right corner (m - 1, n - 1).

# You can move up, down, left, or right from one cell to another adjacent cell as long as your health remains positive.

# Cells (i, j) with grid[i][j] = 1 are considered unsafe and reduce your health by 1.

# Return true if you can reach the final cell with a health value of 1 or more, and false otherwise.

#0706-2026
# https://leetcode.com/problems/find-a-safe-walk-through-a-grid/description/?envType=daily-question&envId=2026-06-18
#
# 0710-2026 taking a breek on this one, a little perplexing. 
#           slight update on foo.py

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        pass
    

# TJS: idea
# -- iterate thr. every option
# -- if reach final cell with health value=1, break loop, return true
# -- after loop complete [no solution found] return false [default]

