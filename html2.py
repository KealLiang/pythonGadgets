d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }
def generate_tr(name, score):
    return '<tr><td>%s</td><td%s>%s</td></tr>' % (name, ' style="color:red"' if score < 60 else '', score)

tds = [generate_tr(name, score) for name, score in d.items()]

print (tds)

print ('<table border="1">')
print ('<tr><th>Name</th><th>Score</th><tr>')
print ('\n'.join(tds))
print ('</table>')


flag = True
num = 10.5

print(flag + num)

# first_name = input('请输入名字：')
# last_name = '欧阳'
# print((last_name + first_name + ' ') * 10)

# num = input("请输入金额：")
# print(type(num))
# num = float(num)
# print(num)
# print(type(num))

fruit = "苹果"
price = 10.0
weight = 20
print("%s的单价是%0.2f元一斤，购买了%6d斤，总价%0.2f元" % (fruit, price, weight, (price * weight)))
