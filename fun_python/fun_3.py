#Cấu trúc dữ liệu Tuple
#Sự khác nhau giữa Tuple và List
"Giá trị của Tuple k thể thay đổi (Immutable), Giá trị Tuple không thế thêm xóa sửa giá trị trong Tuple"

coordinates = (123, 456)
#               0,   1
print(coordinates[0])

"Khi khai báo tạo List = [], Tuple = ()"

coordinates_List_Tuple = [(1,2), (3,4), (4,6)]
print(coordinates_List_Tuple)

"Thao tác với hàm"
"Chỉ định tham số Paremeter"
def say_hello(name):
    "Viết mã thực hiện trong hàm"
    print(f"Chào mừng {name}, Tôi là Quân")

say_hello("Thư")

"Có nhiều tham số sẽ khó nhớ, tối đa hàm là 3 tham số"
"Bạn có thể truyền vô hàm: chuỗi, số nguyên, boolean, list"
def say_hello2(name, email, ):
    print(f"Email của {name} là : {email}")

say_hello2("Quân", "abc@gmail.com")


#Lệnh Return trong hàm
"Khi gọi hàm và muốn nhận thông tin trả về => return"