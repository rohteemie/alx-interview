#!/usr/bin/python3
"""
contains the Pascal's Triangle function
"""


def pascal_triangle(n):
    """ returns a list of lists of integers representing
        the Pascal’s triangle of size n
        row_index = row element
        col_index = column element
    """
    tStack = []

    for row_index in range(1, n+1):#create a stack of size n
        #the list below will be created n times
        #we should append a list inside this list below
        row_char = []

        #row_index is each number from the range above which is 1, 2, 3, n
        for col_index in range(row_index):
            if col_index == 0 or col_index == row_index-1:
                n = 1
                row_char.append(n)
            else:
                n = tStack[row_index-2][col_index-1] + tStack[row_index-2][col_index]
                row_char.append(n)

        tStack.append(row_char)
    return tStack

