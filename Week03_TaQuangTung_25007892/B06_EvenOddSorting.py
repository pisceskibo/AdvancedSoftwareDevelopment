""" BÀI 6: SẮP XẾP CHẴN LẺ
Sắp xếp các phần tử trong mảng theo thứ tự sau:
+ Các phần tử chẵn tăng dần nằm ở bên trái
+ Các phần tử lẻ giảm dần nằm ở bên phải
"""

def customSort(a):
    even_array = []
    odd_array = []

    for item in a:
        if item % 2 == 0:
            even_array.append(item)
        else:
            odd_array.append(item)

    even_array = sorted(even_array)
    odd_array = sorted(odd_array, reverse=True)

    return even_array + odd_array


if __name__ == "__main__":
    array_input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    new_array = customSort(array_input)

    print(f"Sorted array = {new_array}")