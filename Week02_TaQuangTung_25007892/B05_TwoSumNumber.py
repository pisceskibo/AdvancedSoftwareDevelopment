""" BÀI 5: BÀI TOÁN TÌM CẶP SỐ CÓ TỔNG BẰNG K (TWO SUM)
Nhập vào 1 dãy số nguyên (cách nhau bởi khoảng trắng) và một số mục tiêu K.
Tìm cặp số đầu tiên có tổng bằng K.
+ INPUT: dãy số string và số mục tiêu K
+ OUTPUT: tuple cặp số đầu tiên có tổng bằng K

VD1: 2 7 11 15 và K = 9 => (2, 7)
VD2: 1 4 3 2 và K = 5 => (1, 4)
"""

def find_pair_with_sum(nums, k):
    for i in range(len(nums)):
        temp_array = nums.copy()
        temp_array.remove(nums[i])

        searched_number = k - nums[i]
        if searched_number in temp_array:
            return (nums[i], searched_number)

    return ()

nums_str = input("Enter string array: ").strip()
nums_array = [int(x) for x in nums_str.split(" ")]
k = int(input("Ennter target number: "))
tuple_of_pair_number = find_pair_with_sum(nums_array, k)
print(f"{k} = {tuple_of_pair_number}")