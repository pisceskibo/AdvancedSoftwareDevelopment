""" BÀI 7: BANK ACCOUNT QUERY
Viết chương trình tính số tiền thực của một tài khoản ngân hàng dựa trên nhật ký giao dịch có định dạng như sau:
D <số tiền gửi vào>
W <số tiền rút ra>

Lưu ý: đầu vào nhập trên từng dòng, việc nhập kết thúc nếu gặp dòng trống
"""

def calculate_balance():
    balance_money = 0
    print("Giao dịch (D <số tiền gửi> hoặc W <số tiền rút>):")

    while True:
        line = input()

        if not line.strip():
            break

        parts_history = line.split()

        # Phải đủ loại giao dịch
        if len(parts_history) != 2:
            continue

        action = parts_history[0].upper()
        value_score = int(parts_history[1])

        if action == "D":
            balance_money += value_score
        elif action == "W":
            balance_money -= value_score

    return balance_money


if __name__ == "__main__":
    final_balance = calculate_balance()
    print(f"Final real score is: {final_balance}")