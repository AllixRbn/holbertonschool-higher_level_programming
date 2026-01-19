#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for idx in range(len(matrix)):
        for idx2 in range(len(matrix[idx])):
            if idx2 == len(matrix[idx]) - 1:
                print("{}".format(matrix[idx][idx2]), end="")
            else:
                print("{}".format(matrix[idx][idx2]), end=" ")
        print("")
