""" BÀI 4: LOẠI BỎ PHẦN TỬ TRÙNG LẶP NHƯNG GIỮ NGUYÊN THỨ TỰ (DUPLICATE STRING)
Nhập vào một dãy số hoặc một chuỗi. Hãy loại bỏ các phần tử đã xuất hiện trước đó nhưng phải giữ nguyên thứ tự xuất hiện ban đầu của các phần từ còn lại.
+ INPUT: string
+ OUTPUT: string bỏ các phần tử trùng lặp

VD1: google => gole
VD2: 1,2,2,3,1,4 => 1,2,3,4
"""

def remove_duplicated_string(data_str):
    unique_data = dict.fromkeys(data_str)
    if "," in unique_data.keys():
        del unique_data[","]

    return "".join(unique_data)

data_str = input("Enter string: ")
final_string = remove_duplicated_string(data_str)
print(f"{data_str} => {final_string}")