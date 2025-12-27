""" BÀI 6: CHUYỂN ĐỔI SỐ LA MÃ SANG SỐ NGUYÊN (ROMAN NUMBER)
Nhập vào một chuỗi ký tự đại diện cho số La Mã (I, V, X, L, C, D, M) và chuyển nó thành số nguyên tương ứng?
Quy tắc: I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, M = 1000
+ INPUT: chuỗi ký tự bất kỳ nằm trong (I, V, X, L, C, D, M)
+ OUTPUT: số nguyên tương ứng với chuỗi đố

VD1: XIV => 14
VD2: MIX => 1009
"""

def roman_to_int(roman_string, roman_map):
    total_value = 0

    for i in range(len(roman_string)):
        if roman_string[i] not in roman_map.keys():
            return None

        current_value = roman_map[roman_string[i]]

        if i + 1 < len(roman_string) and current_value < roman_map[roman_string[i + 1]]:
            total_value -= current_value
        else:
            total_value += current_value

    return total_value

roman_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
roman_input = input("Enter roman number: ").strip().upper()
integer_roman = roman_to_int(roman_input, roman_map)

print(f"{roman_input} = {integer_roman}")