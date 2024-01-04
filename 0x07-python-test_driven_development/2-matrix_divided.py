#!/usr/bin/python3
""" Division elements of matrix """


def matrix_divided(matrix, div):
    """
    Division all elements of matrix
    Args:
    matrix (int or float) is a list of list
    div: number for division elements matrix by it
    Returns: new matrix after division by div
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_sz = len(matrix[0])
    for row in matrix:
        if len(row) != row_sz:
            raise TypeError("Each row of the matrix must have the same size")

    for i in matrix:
        for j in i:
            if not isinstance(j, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats"
                )

    return [[round(x / div, 2) for x in row] for row in matrix]


if __name__ == "__main__":
    import doctest

    doctest.testfile("tests/2-matrix_divided.txt")
