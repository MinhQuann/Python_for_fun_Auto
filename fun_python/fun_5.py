'''
Calculator

cải tiến
'''



num1 = float(input("Nhập số thứ nhất: "))
operator = input("Nhập toán tử: ")
num2 =  float(input("Nhập số thứ hai: "))

if (operator == "+"):
    print(num1 + num2)
elif (operator == "-"):
    print(num1 - num2)
elif (operator == "*"):
    print(num1 * num2)
elif (operator == "/"):
    print(num1 / num2)
else:
    print("toán tử không hợp lệ!")