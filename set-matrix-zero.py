#!/usr/bin/python
"""
Given an m x n matrix. If an element is 0, set its entire row and column to 0. Do it in-place.

Follow up:

A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
"""

#matrix = [[1,1,1],[1,0,1],[1,1,1]]
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
zero_index = []
for my_list in range(0,len(matrix)):
        temp_list = matrix[my_list]
        for i in range(0,len(temp_list)):
                if  temp_list[i] == 0:
                        for p in range(0,len(matrix)):
                                zero_index.append([p,i])
                        matrix[my_list] = [0] * len(temp_list)
for index_list in zero_index:
        row_index = index_list[0]
        col_index = index_list[1]
        matrix[row_index][col_index] = 0
print matrix
