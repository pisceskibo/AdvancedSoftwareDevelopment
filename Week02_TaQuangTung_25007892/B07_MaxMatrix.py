""" BÀI 7: TÌM HÀNG CÓ TỔNG LỚN NHẤT TRONG MA TRẬN (MAX MATRIX)
Nhập vào số hàng, số cột và các giá trị của một ma trận.
Hãy cho biết hàng nào có tổng các phần tử lớn nhất?
+ INPUT: số hàng, số cột, các phần tử trong ma trận
+ OUTPUT: hàng có tổng lớn nhất

VD1: Matrix(2, 2) với [[1, 2], [3, 4]] => Tổng = 3 + 4 = 7
VD2: Matrix(2, 2) với [[5, 5], [1, 2]] => Tổng = 5 + 5 = 10
"""

def find_max_row_of_matrix(matrix):
    max_row_value = sum(matrix[0])
    best_index = 1

    for i in range(1, len(matrix)):
        current_row_value = sum(matrix[i])

        if current_row_value > max_row_value:
            max_row_value = current_row_value
            best_index = i + 1

    return best_index, max_row_value

row_input = int(input("Enter number of row: "))
col_input = int(input("Enter number of column: "))

matrix = []
for i in range(row_input):
    row_array = []
    for j in range(col_input):
        value_item = int(input(f"Value with row = {i + 1} and col = {j + 1} is: "))
        row_array.append(value_item)
    matrix.append(row_array)

index_of_row, value_of_row = find_max_row_of_matrix(matrix)
print(f"Row {index_of_row} with max value is {value_of_row}")