

class Matrix:
    def __init__(self, *values):
        self.values = values

    def add(self, matrix_to_add):
        if not self.check_dimensions(matrix_to_add):
            print("Different dimensions")
            return None

        new_matrix = self.create_new_matrix(matrix_to_add)
        return new_matrix


    def check_dimensions(self, matrix_to_add):
        if len(self.values) == len(matrix_to_add.values):
            return True
        return False

    def create_new_matrix(self, matrix_to_add):
        new_matrix = []
        for i in range(len(matrix_to_add.values)):
            val = matrix_to_add.values[i] + self.values[i]
            new_matrix.append(val)
        return Matrix(new_matrix)
    
    def print_matrix(self):
        for i in self.values:
            print(i, end=' ')




def main():
    matrix1 = Matrix(1, 2, 3, 4)
    matrix2 = Matrix(1, 1, 1, 1)
    matrix3 = matrix1.add(matrix2)
    matrix3.print_matrix()


if __name__ == "__main__":
    main()