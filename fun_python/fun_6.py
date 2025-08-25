'''
Cấu trúc dữ liệu Dictionary
'''


#Dictionary -  Từ điển
# Key           Value
#Hello          Xin Chào
#Bye            Tạm Biệt
#Bread          Bánh mì

englist_vietnamese_dict = {
    "Hello" : "Xin Chào",
    "Bye": "Tạm Biệt",
    "Bread": "Bánh mì",
    "Tea":"Trà",
    "Milk": "Sữa"

    # 0 : "Xin Chào",
    # 1: "Tạm Biệt",
    # 2: "Bánh mì",
    # 3:"Trà",
    # 4: "Sữa"

}

print(englist_vietnamese_dict["Milk"])
print(englist_vietnamese_dict.get("ello", "từ khóa này ko tồn tại"))



''' 
Vòng Lặp While
'''
#While Loop
'''
Sẽ chạy tới khi điều kiện không còn đúng
'''

#Sample
n = 1
while n <= 3:
    print("Meo Meo")
    n += 1
print("được rồi")


'''
    Vòng lặp for

'''
#In ra từng ký tự trong chuỗi
name = 'Bùi Nguyễn Minh Quân'
for char in name:
    print(char)

print("-----------------------------------------")
teams = ["Real", "Barca", "Chel", "Bayern", "MU", "MC"]
for name in teams:
    print(name)

print("-----------------------------------------")
#chạy For qa một mảng số nguyên
for i in range(1, 11):
    if i == 1:
        print("Đây là phần tử đầu tiên trong mảng")
    else:
        print(f"Đây là phần tử ở vị trí thứ {i} trong mảng")


