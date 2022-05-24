import numpy as np


# def
def new_line():
    print("-------------------------------------------")


def new_2line():
    print()
    new_line()


def print_all(*objs):
    for o in objs:
        print(o)
        

a = np.arange(10)
print(type(a))
print(np.sqrt(a))
new_line()


a = np.array([[1, 2, 3, 4], [3, 4]])
print(a)
print(type(a))
new_line()


# dtype
d = np.array(range(10), dtype = float)
print(d)
print(type(d))
new_line()


# ndmin
d = np.array(range(10), dtype = float, ndmin = 3)
print(d)
new_line()


# arange
a = np.arange(10, dtype = float)
print(a)
new_line()


# random
a = np.random.random(size = 5)
print(a)
new_line()


# 3行4列
a = np.random.random(size = (3, 4))
print(a)
new_line()


# 2个
a = np.random.random(size = (2, 3, 4))
print(a)
new_line()


# random int 三维
a = np.random.randint(5, 10, size = (2, 2, 10))
print(a, a.dtype)
new_line()


# 标准的正态分布：期望为0，方差为1
# 二维：2个3行4列
a = np.random.randn(2, 3, 4)
print(a)
new_line()


# 指定期望和方差的正态分布
# 默认期望loc  = 0.0，方差scale = 1.0 
a = np.random.normal(size = 5)
print(a)

b = np.random.normal(loc = 2, scale = 3, size = (3, 4))
print(b)
new_line()

# 都赋值为0
a = np.zeros(5)
print(a)
a = np.zeros((3, 4), dtype = int)
print(a)
b = np.ones((5, 3))
print(b)
# 是原先内存里的值，未初始化
c = np.empty((4, 3))
print(c)
new_line()

# 等差数列
# 3rd parm default: size = 50
a = np.linspace(1, 10)
print(a)
a = np.linspace(1, 9, 5)
print(a)
# 不包括最末尾的数
b = np.linspace(1, 9, 5, endpoint = False)
print(b)
new_line()

# 等比数列
# base：公比(底数)
# 2的0~9次方 底数为2（公比为2的倍数），生成含有4个元素的等比数列
a = np.logspace(0, 9, 4, base = 2)
print(a)
a = np.logspace(0, 9, 10, base = 3, dtype = int)
print(a)
new_line()

# 切片
print(a[5::3])
print(a[::-1])
new_line()

a = np.arange(1, 13)
# 修改形状(维度)(4 * 3 = 12)
a = a.reshape(4, 3)
print(a)
print(a[2])
print(a[2][1])
new_line()

# 对行，列进行切片
print(a[:,:])
print()
# 第二列
print(a[:,1])
print()
# 第一，二列
print(a[:,0:2])
print()
# 奇数行第一，二列
print(a[::2,0:2])
# eq: a[3][2]
print(a[3, 2])
new_line()

print(np.array([a[1, 2], a[2, 0]]))
print(a[(1, 2), (2, 0)])
new_line()

# 行倒序
print(a[::-1])
# 行，列倒序
print(a[::-1,::-1])
new_line()

# 复制
a = np.arange(1, 13).reshape((3, 4))
print(a)
# 浅拷贝
sub_a = a[:2,:2]
print(sub_a)
# eq: sub_a[0][0] = 100
sub_a[0, 0] = 100
print(sub_a)
print(a)
new_line()

# 深拷贝
sub_aa = np.copy(a[:2,:2])
print(sub_aa)
sub_aa[0, 0] = 1
print(sub_aa)
print(a)
new_line()

# 修改维度
a = np.arange(1, 25)
print(a)
print()
print(a.reshape(2, 3, 4))
print()
b =np.reshape(a, (3, 8))
print(b)
print()
# 将二维改成一维
print(b.reshape(b.size))
a = b.reshape(-1)
# eq:
a = b.ravel()
# eq:
a = b.flatten()
print(a)
new_line()

# 拼接（stack：堆，叠放）
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[11, 12, 13], [14, 15, 16]])
h= np.hstack((a, b))
print(h)
v = np.vstack((a, b))
print(v)
new_line()

# concatenate级联：多维数组连接
# 对上述2维数组：axis(轴)为0时为竖直堆放（行），为1时为横向堆放
a = np.arange(1, 13).reshape(1, 2, 6)
b = np.arange(101, 113).reshape(1, 2, 6)
print(a, a.shape)
print(b, b.shape)

r1 = np.concatenate((a, b), axis = 0)
r2 = np.concatenate((a, b), axis = 1)
r3 = np.concatenate((a, b), axis = 2)
print(r1, r1.shape)
print(r2, r2.shape)
print(r3, r3.shape)
new_line()

x = np.arange(1, 9)
a = np.split(x, 4)
for i in a:
    print(i)

# 0, 1一份，2, 3, 4, 5一份，6及之后一份
a = np.split(x, [2, 6])
for i in a:
    print(i)
    
new_line()

# 竖直
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
r, w = np.split(a, 2, axis = 1)
print_all(r, w)
new_line()

# 0, 1一份，2一份，3及之后一份
r, w, k = np.split(a, [2, 3], axis = 1)
print_all(r, w, k)
new_line()

# hsplit: axis = 1
# 向水平方向平移
r, w = np.hsplit(a, [3])
print_all(r, w)
new_line()

# vsplit: axis = 0
# 向竖直方向平移
r, w = np.vsplit(a, [3])
print_all(r, w)
new_line()

# 转置(倒置)
a = np.arange(1, 25).reshape(8, 3)
b = a.transpose()
b =np.transpose(a)
b = a.T
print(b, b.shape)
new_line()

a = a.reshape(2, 3, 4)
b = np.transpose(a)
print(b, b.shape)
new_line()

# (1, 2, 0)表示按照第2, 3, 1维度顺序
c = np.transpose(a, (1, 2, 0))
print(c, c.shape)
new_line()

a = np.arange(9).reshape(3, 3)
b = np.array([100])

print(a + b)
print(a - b)

print(np.add(a, b))
print(np.subtract(a, b))
new_line()

# out参数使用
y = np.empty((3, 3), dtype = int)
np.multiply(a, 10, out = y)
print(a)
print(y)
new_line()

# 三角函数
a = np.array([0, 30, 60, 90])
print(np.sin(a / 180 * np.pi))
print(np.pi)
new_line()

# 四舍五入
a = np.array([1.0, 123, 4.55, 3.467])
print(a)
print(np.around(a))
print(np.ceil(a))
# just like in Java
print(np.floor(a))
new_line()

# 幂运算
a = np.arange(12).reshape(3, 4)
print(a)
print(np.power(a, 3))

a = a.reshape(-1)
b = np.zeros(24)
np.power(a, 2, out = b[:12])
print(b)
new_line()

# 中位数
a = b[:12]
print(a)
print(np.median(a))

a = a.reshape(3, 4)
print(a)
print(np.median(a, axis = 0))
print(np.median(a, axis = 1))
new_line()

# 平均值
print(np.mean(a))
print(np.mean(a, axis = 0))
new_line()

# 最值
print(a.max(), a.min(), a.sum())
# 返回最值下标
print(a.argmax(), a.argmin())






