# Define
# Sử dụng dấu {}, trong đó có các cặp key:value cách nhau bởi dấu ','
Diem_thi = {'sv01':0, 'sv02':9}
# Khai báo từ điển rỗng
DicNull = {}


# Truy cập value của 1 key
print(Diem_thi['sv01']) #0

# Thêm cặp key-value
# Sử dụng phép gán dic[new_key] = new_value 
Diem_thi['sv03'] = 7

# Sử value của key -> gán value mới cho key
Diem_thi['sv01'] = 5

# Xóa cặp key-value -> sử dụng hàm del
del Diem_thi['sv02'] # xóa sv02 ra khỏi dic
# sử dụng hàm pop trong trường hợp ko chắc có key trong dict -> chương trình ko bị dừng lại do error
value_sv2 = Diem_thi.pop('sv02', 'notfound') # return value của key sv02


# Dict có thể lưu trữ 1 loại thông tin về nhiều đối tượng -> key hay value của dict có thể là 1 collection
Diem_thi['sv00'] = {'toan': 9, 'ly': 8, 'hoa':10}

# Nếu sử dụng truy cập = key -> sẽ có lỗi nếu chưa có key, để giải quyết vấn đề này
# ta sử dụng method get(key,'not found key') để đảm bảo chương trình ko bị dừng
print(Diem_thi.get('sv05', 'Not found'))

# Duyệt value toàn bộ từ điển -> dùng method values để lấy list value dưới dạng 1 object, dùng for để duyệt
# từng value trong list
for value in Diem_thi.values():
    print(value)


# Thêm các cặp key-value từ dict1 vào dict -> sử dụng method update (method void)
dict = {'key1':1, 'key2':2}
dict1 = {'key3':3, 'key4':4}
dict.update(dict1)
print(dict)

# nén và giải nén arguments
# sử dụng toán tử * để giải nén list, toán từ ** để giải nén dict
# sử dụng nén để kết hợp 2 dict với nhau
dict = {'key1':1, 'key2':2}
dict1 = {'key3':3, 'key4':4}
new_dict = {**dict, **dict1}

# sử dụng in/ not in để kiểm tra 1 object có trong collection hay không

# sử dụng zip để tạo dict mới từ 2 list
key_list = ['sv001', 'sv002', 'sv003']
key_value = [3, 9, 10]

dict = dict(zip(key_list, key_value))
print(dict)

# lặp qua các cặp key_value của dict thông qua hàm items()
for key, val in Diem_thi.items():
    print(key, end='')
    print(val, end='')

# lặp qua các keys trong dict bằng hàm keys()
# Lặp lại các key của dict sắp xếp theo key
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.") 