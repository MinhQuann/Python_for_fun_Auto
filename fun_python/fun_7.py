'''
    Build trò chơi đoán từ
    Ý tưởng:
        - 1 từ bí mật
        - 1 số gợi ý để đưa ra dự đoán
        - Ng dùng nhập nhiều lần
'''
secret_word = "Đẹp trai"
hint = "Gợi ý: Minh Quân sao nè: "
guess_ans = ""
limit_count  = 0
guess_limit = 3

# print(hint)
# while guess_ans != secret_word:
#     if limit_count < guess_limit:
#             guess_ans = input("Mời nhập câu trả lời: ")
#             limit_count += 1
#     else:
#         break
   

# if guess_ans == secret_word:
#     print("Chúc mừng, bạn đã đoán chính xác")
# else:
#     print("Bạn đã thất bại vì doán sai 3 lần")

print("-------------------------------------------------")

'''
    Build hàm tính lũy thừa
'''
#Hàm tính lũy thừa
#2^3 = 8
#3^2 = 9

def Calculate_power(base_number: int, exponent: int ) -> int:
    result = 1
    for i in range(exponent):
        print(range(exponent))
        result =  result * base_number
        #base number = 2, exponen = 3
        # vòng lặp đầu tiên : result = 1 , base = 2
        # 1 * 2 = 2
        # 2 * 2 = 4
        # 4 * 2 = 8

    return result

print(Calculate_power(3,3))    


'''
Mảng 2 chiều các vòng lặp lồng nhau
'''
#array
number = [1,2,3]

#Ma trận ( Mảng 2 chiều)
#[1,2,3]
#[4,5,6]
#[7,8,9]

Matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(Matrix[1][1])

print("----------------------")

for row in Matrix:
    for col in row:
        print(col)
