from matrix import Matrix


def main():
    matrix1 = Matrix(1, 2, 3, 4)
    matrix2 = Matrix(1, 1, 1, 1)
    matrix3 = matrix1.add(matrix2)
    matrix3.print_matrix()


if __name__ == "__main__":
    main()