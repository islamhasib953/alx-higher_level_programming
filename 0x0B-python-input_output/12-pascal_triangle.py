#!/usr/bin/python3
"""
12-pascal_triangle
"""


def pascal_triangle(n):
    """pascal_triangle"""
    if n <= 0:
        return []
    pascal_triangle = [[1]]
    for i in range(n - 1):
        row_list = [1]
        for j in range(i):
            row_list.append(pascal_triangle[i][j] + pascal_triangle[i][j + 1])
        row_list.append(1)
        pascal_triangle.append(row_list)
    return pascal_triangle
