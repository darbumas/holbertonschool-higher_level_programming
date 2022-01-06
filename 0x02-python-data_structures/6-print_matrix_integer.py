#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for element in range(len(row)):
            print("{}".format(row[element]), end="")
            if element < len(row) - 1:
                print(" ", end="")
        print()
