"""
Cho hai danh sách đầu vào ans và keys có kiểu dữ liệu string, biết rằng:
+ ans: một chuỗi các câu trả lời trắc nghiệm của sinh viên
+ keys: một chuỗi đáp án tương ứng với mỗi câu hỏi
Với mỗi câu trả lời đúng được tính 5 điểm, sai bị trừ 1 điểm, không trả lời đủ sẽ bị điểm liệt 0 điểm
=> Hãy trả về số điểm của sinh viên?
"""

def check_score_of_ans_keys(ans, keys):
    ans = ans.strip()
    keys = keys.strip()
    score = 0

    if len(ans) != len(keys):
        return 0

    for i in range(len(ans)):
        if ans[i] == keys[i]:
            score += 5
        else:
            score -= 1

    return score

ans = input("Enter student's answer: ")
keys = input("Enter exactly answer: ")
student_score = check_score_of_ans_keys(ans, keys)
print(f"Student's score is: {student_score}")