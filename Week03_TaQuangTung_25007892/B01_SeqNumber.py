""" BÀI 1: DÃY SỐ
+ isAlt(a): kiểm tra dãy đan dấu
+ isGrow(a): kiểm tra dãy số tăng
+ isMulti(a): kiểm tra dãy số có là cấp số nhân không
+ isAdd(a): kiểm tra dãy số có là cấp số cộng không
"""

# Kiểm tra dãy đan dấu
def isAlt(a):
    if len(a) < 2:
        return True

    for i in range(len(a) - 1):
        if a[i]*a[i + 1] > 0:
            return False

    return True

# Kiểm tra dãy số tăng
def isGrow(a):
    if len(a) < 2:
        return True

    for i in range(len(a) - 1):
        if a[i] > a[i + 1]:
            return False

    return True

# Kiểm tra cấp số nhân
def isMulti(a):
    if len(a) < 2:
        return True

    if a[0] == 0:
        return all(x == 0 for x in a)
    else:
        q = a[1] / a[0]
        for i in range(len(a) - 1):
            if not abs(a[i + 1] - a[i] * q) < 1e-9:
                return False

        return True

# Kiểm tra cấp số cộng
def isAdd(a):
    if len(a) < 2:
        return True

    d = a[1] - a[0]
    for i in range(len(a) - 1):
        if a[i + 1] - a[i] != d:
            return False

    return True


if __name__ == "__main__":
    n = int(input("Enter length of array: "))
    array_number = []
    for i in range(n):
        item = float(input(f"Item{i} is: "))
        array_number.append(item)

    print(f"Dãy đan dấu: {isAlt(array_number)}")
    print(f"Dãy tăng: {isGrow(array_number)}")
    print(f"Cấp số nhân: {isMulti(array_number)}")
    print(f"Cấp số cộng: {isAdd(array_number)}")