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



#Các hàm thao tác với list
student_names = ["Quân", "Hưng", "Nam", "Hoài"]
match_score = [10, 9 ,8, 7]


student_names.extend(match_score)  #nối 2 danh sách lại với nhau
print(student_names)

student_names.append("Thắng")
print(student_names)




