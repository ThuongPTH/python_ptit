dict ={
    'id1':{
        'name':'hoa',
        'class':'at1'
    },
    'id2':{
        'name':'hoa',
        'class':'at1'
    },
    'id3':{
        'name':'thuong',
        'class':'at1'
    }
}

list_value = []
rs_dict = {}
# for i in dict.keys():
#     if list_value.count(dict[i])==0:
#         rs_dict[i] = dict[i]
#         list_value.append(dict[i])

for key, val in dict.items():
    if val not in list_value:
        rs_dict.append(val)
        rs_dict[key] = val

print(dict)
print(rs_dict)



