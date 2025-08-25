'''
Cho phép chương trình ra quyết định -> thực thi khi ra đúng và khi ra sai
'''

a = 100
b = 100

if a < b:
    print("a nhỏ hơn b")
elif a > b:
    print("a lớn hơn b")
else:
    print("a = b")


'''
   Các toán tử Logic trong python 
'''

a1 = 100
b1 = 50  
c1 = 100

if a1 < b1:
    print("a1 < b1")
elif a1 > b1:
    print("a1 > b1")
else:
    print("a = b")


if a1 > b1 and a1 > c1:
    print("a là sô lớn nhất")

if (a1 == b1) or (a1 == c1):
    print("Có ít nhất một số bằng giá trị với a")

'''
Toán tử Not
'''
a =  True
a2 = 100
b2 = 100
print(not a)
if not a2 > b2:
    print("a ko lớn hơn b")
