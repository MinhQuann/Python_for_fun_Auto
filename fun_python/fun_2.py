# num1 = input("Nhập số thứ nhất: ")
# num2 = input("Nhập số thứ hai: ")
num1 = 2
num2 = 3

sum = num1 + num2
print(sum)

# Chuyển biến num1-num2 thành số
sum2 = float(num1) + float(num2)
print(sum2)

# String format
number = 2
text = " là số người yêu mà tôi từng có"

print(str(number) + text )
print(f"{number}{text}")

#hàm format
number_temp = 4
text_temp = "{} là số người yêu mà tôi từng có"

print(text_temp.format(number_temp))

#Có thể dùng nhiều dấu {} trong String để gắn vào String này
number_temp1 = 2
number_temp1_real = 0

text_temp1 = "{} là số người yêu, nhưng {} đây là số người yêu thực tế"
print(text_temp1.format(number_temp1, number_temp1_real))

text_temp2 = "{1} là số người yêu, nhưng {0} đây là số người yêu thực tế"
print(text_temp2.format(number_temp1, number_temp1_real))



#Dữ liệu danh sách (List)
#cần làm việc với danh sách dữ liệu...
teams = ["REAL","BARCA", "MU", "MC", "CHEL", "ARS", "LIVER", "TOT"]
#           0   1           2   3       4       5       6      7      
teams_add = "Bayern"
teams[7] = "Thư"

print(teams)
print(teams[0])
print(teams[-2])
print(teams[5:])
print(teams[1:4])

print("mới nè: " + str(teams[7]))

teams.append(teams_add)
print("đây nè: " + str(teams))

# def appendFUNC(text:str) -> list[str]:
#     mem = ["Quân", "nè", "Tèo"]
#     if text not in mem:
#         mem.append(text)
#     else:
#         print("Exist")
#     return mem


# print(appendFUNC("Tèo"))




#Các hàm thao tác với list
student_names = ["Quân", "Hưng", "Nam", "Hoài"]
match_score = [10, 9 ,8, 7]


student_names.extend(match_score)  #nối 2 danh sách lại với nhau
print(student_names)


student_names_memor = ["Quân", "Hưng", "Nam", "Hoài", "Nghĩa"]
#                        0      1        2     3       4  
print(student_names_memor)

#Hàm Insert cần có index
student_names_memor.insert(1, "Dũng")
print("Chèn 'Dũng'vào list vị trí số 1: "+ str(student_names_memor))

student_names_memor.remove("Nghĩa")
print("xóa Nghĩa khỏi danh sách" + str(student_names_memor))

student_names_memor.clear()
print("Xóa hết phần tử trong list: " + str(student_names_memor))

student_names_memor_new = ["Quân", "Thư", "Bơ"]
student_names_memor_new.pop() #Loại bỏ phần tử cuối cùng
print(student_names_memor_new)

#trả ra vị trí của phần tử
student_names_memor_new.index("Quân")
print(student_names_memor_new.index("Quân"))



#Đếm số phần tử xuất hiện trong danh sách
list_abc = ["a", "b" ,"c", "d", "a", "a", "c", "a", "b"]
print("Số lần xuất hiện: " + str(list_abc.count("a")))


# def count_elements(data: list[str]) -> dict[str, int]:
#     counts: dict[str, int] = {}
#     for item in data:
#         if item in counts:
#             counts[item] += 1
#         else:
#             counts[item] = 1
#     return counts         

# res = count_elements(list_abc)
# for k,v in res.items():
#     print(f"{k}: {v}")


list_abc.sort()
print("Sort list: " + str(list_abc))

list_score = [10, 9 ,5,7,8,3]

list_score.sort()
print("Sort number: " + str(list_score))

list_score.reverse()
print("Reverse: " + str(list_score))


list_score2 = [10, 9 ,5,7,8,3]
list_temp = list_score2.copy()
print("Copy: " + str(list_temp))






