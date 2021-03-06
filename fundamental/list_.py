name_list = ['aaa','bbb','cc']
print(name_list.index('cc'))

name_list[1] = '李斯'
print(name_list)

tmp_list = ['孙悟空', '唐僧']
name_list.extend(tmp_list)
print(name_list)


print(name_list.pop())
print(name_list)

# del关键字用于将变量从内存中删除，删除后，后续的代码就不能再使用了
del name_list[1]
print(name_list)


for str in name_list:
    print(str)
    # if str == '孙悟空':
    #     break
else:
    print('python中for可以接着else，else中的语句只有在for遍历了【所有的】元素后才会执行（break跳出后不执行）')
print('for循环完毕')