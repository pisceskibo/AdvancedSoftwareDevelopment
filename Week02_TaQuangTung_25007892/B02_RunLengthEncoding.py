""" BÀI 2: NÉN CHUỖI CƠ BẢN (RUN-LENGTH ENCODING)
Nhập một chuỗi có các ký tự lặp lại liên tiếp nhau. Hãy nén chuỗi đó theo quy tắc: [Ký tự][số lần lặp]
+ INPUT: string
+ OUTPUT: string được xếp theo quy tắc [Ký tự][số lần lặp]

VD1: aaabbcccc => a3b2c4
VD2: aabbbba => a2b4a1
"""

def run_length_encoding(input_string):
    result_array = []
    count = 1

    for i in range(len(input_string) - 1):
        if input_string[i] == input_string[i + 1]:
            count += 1
        else:
            group_string = input_string[i] + str(count)
            result_array.append(group_string)

            count = 1

    # The last item
    final_group_string = input_string[-1] + str(count)
    result_array.append(final_group_string)

    final_join_string = "".join(result_array)
    return final_join_string

input_string = input("Enter string: ")
encoded_string = run_length_encoding(input_string)
print(f"{input_string} is converted to {encoded_string}")