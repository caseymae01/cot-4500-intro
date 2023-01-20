import sys
import numpy as np

def create_matrix(rows, columns):
    new_matrix = np.zeros((rows, columns), dtype=int)
    for row in range(rows):
        for column in range(columns):
            if row == column:
                new_matrix[row, column] = 1
    return new_matrix

def print_matrix(matrix_to_print):
    np.savetxt(sys.stdout, matrix_to_print, fmt="%i")
    print("")

def adding_numbers(matrix_to_change, number_to_add):
    rows = len(matrix_to_change)
    columns = len(matrix_to_change[0])
    for row in range(rows):
        for column in range(columns):
            if row != column:
                matrix_to_change[row, column] += number_to_add
    return matrix_to_change

def remove_end_column(matrix_to_change):
    remove_column = len(matrix_to_change[0]) - 1
    matrix_to_change = matrix_to_change[:, 0:remove_column]
    return matrix_to_change





def main():
    # Matrix 1
    matrix_1 = create_matrix(3, 3)
    print_matrix(matrix_1)

    # Matrix 2
    matrix_2 = adding_numbers(matrix_1, 3)
    print_matrix(matrix_2)

    # Matrix 3
    matrix_3 = remove_end_column(matrix_2)
    print_matrix(matrix_3)



if __name__ == "__main__":
    main()