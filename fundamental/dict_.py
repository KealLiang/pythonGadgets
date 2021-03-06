# 字典是【无序】的集合
person_dict = {
    "name": "小明",
    "age": 18,
    "height": 175
}
print(person_dict)

person_dict.pop('age')

print(person_dict)


tmp_dict = {
    "age": 20,
    "weight": 140
}
person_dict.update(tmp_dict)
print(person_dict)
print(tmp_dict)

# 遍历字典
for k in person_dict:
    print(k, '========>', person_dict.get(k))

print('-'*50)

for (k, v) in person_dict.items():
    print('key=%s  value=%s' % (k, v))