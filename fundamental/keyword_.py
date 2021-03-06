import keyword
print(keyword.kwlist)

import random
for i in range(10):
    compute = random.randint(1, 10)
    print("第%d号随机数为：%d" % (i, compute))
