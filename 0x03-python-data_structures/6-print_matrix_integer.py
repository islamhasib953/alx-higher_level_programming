#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for i in matrix:
            for j in i:
                print("{:d}".format(j), end=" ")
            print("\n")


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print_matrix_integer(matrix)
print("--")
print_matrix_integer()
