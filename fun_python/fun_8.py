phone_book = open("phone_book.txt", "r", encoding="utf-8") #Chế độ r
#w chế độ write


print(phone_book.readable()) #Kiểm tra có đọc file được không

# print(phone_book.read())
for persion in phone_book.readlines():
    persion = persion.replace("\n", "")
    print(persion)

phone_book.close()

'''
Ghi dữ liệu vào file
'''
with open("phone_book.txt", "a", encoding="utf-8") as f:
    f.write("\nSang - 098123XXX")
    f.write("\nTeo - 098125XXX")
    print(f)

with open("new_phone_book.txt", "w", encoding="utf-8") as f:
    f.write("Haha - Quân nè")



