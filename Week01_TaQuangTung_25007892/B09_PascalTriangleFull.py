"""
Cho một số nguyên numRows, hãy trả về numRows dòng đầu tiên của tam giác Pascal?

VD: numRows = 5 => [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
"""

def get_pascal_triangle(num_rows):
    pascal_triangle = []

    for i in range(num_rows):
        row = [1] * (i + 1)

        for j in range(1, i):
            row[j] = pascal_triangle[i - 1][j - 1] + pascal_triangle[i - 1][j]

        pascal_triangle.append(row)

    return pascal_triangle

num_rows = int(input("Enter row number of Pascal Triangle: "))
pascal_triangle = get_pascal_triangle(num_rows)
print(f"PascalTriangle = {pascal_triangle}")