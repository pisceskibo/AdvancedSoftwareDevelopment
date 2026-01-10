""" BÀI 2: MA TRẬN MA PHƯƠNG
Ma trận ma phương là ma trận có tổng các hàng, các cột, các đường chéo bằng nhau.
+ isMagicSquare(): kiểm tra tính chất ma phương của ma trận
+ inputMatrix(): nhập và trả về ma trận dạng mảng 2 chiều

Lưu ý: mỗi hàng nhập trên một dòng, mỗi số cách nhau bởi dấu tab (\t)
"""

def isMagicSquare(matrix):
    n = len(matrix)
    if n == 0 or any(len(row) != n for row in matrix):
        return False

    # Target value
    target_sum = sum(matrix[0])

    # 1. Kiểm tra tổng các hàng:
    for row in matrix:
        if sum(row) != target_sum:
            return False

    # 2. Kiểm tra tổng các cột:
    for j in range(n):
        col_sum = sum(matrix[i][j] for i in range(n))
        if col_sum != target_sum:
            return False

    # 3. Kiểm tra đường chéo chính:
    if sum(matrix[i][i] for i in range(n)) != target_sum:
        return False

    # 4. Kiểm tra đường chéo phụ:
    if sum(matrix[i][n - 1 - i] for i in range(n)) != target_sum:
        return False

    return True

def inputMatrix():
    m = []
    print("Create matrix (tab):")
    while True:
        line = input()

        if not line.strip():
            break

        row = [int(x) for x in line.split("\t") if x.strip()]
        m.append(row)

    return m


if __name__ == "__main__":
    try:
        matrix = inputMatrix()

        is_magical_matrix = isMagicSquare(matrix)
        print(f"{matrix} is magic square? - {is_magical_matrix}")
    except ValueError:
        print("Input numbers is value error")