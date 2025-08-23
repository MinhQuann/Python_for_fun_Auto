# biến và kiểu dữ liệu
import math
from tkinter import N


name = "minh quân"

print("Hello World")
print(f"{name} nè, tôi 20 tuổi ")

# với biến name khi nằm trước print(f "" thì sẽ dăn theo biến name đó)
name = "minh quân"
print(f"hello {name}")

name = "minh quân2"
print(f"hello {name}")

# kiểu dữ liệu
# string
name = "minh quân"

# number
age = 20

# boolean
is_student = True
is_student2 = False


# Thao tác với String
print("Minh Quân là tôi nè nha hehehe")

# xuống dòng
print("Minh Quân \nlà tôi nè nha hehehe")

print("""Minh Quân 
là tôi nè nha hehehe""")

# muốn tôi nè trong dấu ngoặc kép
print("Minh Quân là \"tôi nè nha he\" hehe")

# nối chuỗi
channel_name = "Minh Quân_channelname"
print(channel_name + " là tôi nè nha hehehe")

# Hàm thao tác với String
channel_name2 = "Minh Quân_channelname2"
print(channel_name2.upper())
print(channel_name2.lower())
print(channel_name2.isupper()) #trả False
print(channel_name2.upper().isupper()) #trả True
print(len(channel_name2)) #tính độ dài String

channel_name3 = "Minh Quân_channelname"
print(channel_name3[5]) #in ra ký tự trong String này  

print(channel_name.index("Quân")) #trả ra vị trí chữ Q

print(channel_name3.replace("Quân","Tối"))

# Dữ liệu Number

print(2)
print(3.145)
print(3 + 4)
print(2 * (3 + 4))


print(5 % 2) #lấy phần dư = 1

number = 2
print(number)

# chuyển number thành chuổi
number2  = -3
print(type(str(number2))) #trả ra dạng string

print(str(number2) + " là số người yêu tôi từng có")

print(abs(number2)) 

print(pow(2,10)) #mũ 2^10

print(max(2,10)) #lấy số max
print(min(2,10)) #lấy số min

number_2_7 = 2.7
print(round(number_2_7)) #làm tròn


print( "làm tròn xuống " + str(math.floor(number_2_7))) #làm tròn bằn thư viện math
print("làm tròn lên " + str(math.ceil(number_2_7))) #làm tròn lên

sqr_number = 36
print(math.sqrt(sqr_number)) #căn bậc 2 = 6.0

print(round(math.sqrt(sqr_number))) #căn bậc 2 = 6


#Nhận dữ liệu người dùng nhập vào
name = input("Nhập tên: ")
age = input("Nhập tuổi: ")

print(f"Xin chào, {name} năm nay bạn {age}")










