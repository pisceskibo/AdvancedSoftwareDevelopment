from collections import Counter


def sort_by_frequency(nums):
    # Bước 1: Đếm số lần xuất hiện của mỗi phần tử
    # Ví dụ: {1: 2, 2: 3, 3: 1}
    counts = Counter(nums)

    # Bước 2: Sắp xếp danh sách với key tùy chỉnh
    # -counts[x]: Tần suất giảm dần (dùng dấu âm để đảo ngược thứ tự tăng dần của sort)
    # x: Giá trị tăng dần
    nums.sort(key=lambda x: (-counts[x], x))

    return nums


# --- Xử lý Nhập liệu ---
try:
    input_str = input("Nhập dãy số (cách nhau bởi dấu phẩy hoặc khoảng trắng): ")
    # Thay thế dấu phẩy bằng khoảng trắng để dễ split
    clean_input = input_str.replace(',', ' ')
    nums = [int(x) for x in clean_input.split()]

    result = sort_by_frequency(nums)
    print(f"Output: {', '.join(map(str, result))}")

except ValueError:
    print("Vui lòng nhập các số nguyên hợp lệ.")