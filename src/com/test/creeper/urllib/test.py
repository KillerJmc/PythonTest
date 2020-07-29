from urllib import parse
from urllib import request as req

from com.jmc.io.files import Files


# defs
def new_line():
    print("-------------------------------------------")


def new_2line():
    print()
    new_line()


def print_all(*objs):
    for o in objs:
        print(o)
        
        
def show(pic_f):
    #import matplot好lib.pyplot as plt
    plt = None
    from PIL import Image
    im = Image.open(pic_f)
    plt.imshow(im)
    plt.show()
        

def outh(src):
    out(src.decode('utf-8'), '/sdcard/ok.html')


# init
read = Files.read
out = Files.out


# resp
resp = req.urlopen('http://www.baidu.com')
print(resp.getcode())
# just like a file
# returns a bytes obj
print(resp.readline())
print(resp.read(10))
new_line()


# retrieve(找回)：用于保存网页到文件

req.urlretrieve('http://www.baidu.com', 'baidu.html')
#print(read('baidu.html')[:10])
#new_line()

# 下载文件
jpg_url = read('jpg_url.txt')

req.urlretrieve(jpg_url, 'strawberry.jpg')

# show('strawberry.jpg')
# new_line()


# urlencode
parms = dict(name = '张三', age = 18)
r = parse.urlencode(parms)
print(r)

# apply
# url = 'https://www.baidu.com/s?word=刘德华'
# wrong: encode error
# resp = req.urlopen(url)

url = 'http://www.baidu.com/s?'
ps = dict(word = '刘德华')
r = parse.urlencode(ps)
url += r
print(url)
resp = req.urlopen(url)

# urldecode
print(parse.parse_qs(r))
new_line()


# parse
url = 'http://www.baidu.com/s?word=py&uname=abc#1'
r = parse.urlparse(url)
# 可以用r.获取属性，如r.scheme
print(r)

# 相比以上的没有parms属性
r = parse.urlsplit(url)
print(r)
new_line()


# 请求头

# 不用请求头，部分网页有反爬虫
url = 'https://www.lagou.com/jobs/list_python?labelWords=sug&fromSearch=true&suginput='
resp = req.urlopen(url)
print(resp.read().decode('utf-8')[-100:])
new_line()


# 使用请求头防止反爬虫
headers = {
    'User-Agent' : 'User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36'
}

# 有data可以加上data = parse.urlencode(data).encode('utf-8')
reqs = req.Request(url, headers = headers)
resp = req.urlopen(reqs)
# 成功
#outh(resp.read())
print(resp.read().decode('utf-8')[29800:30000])
new_line()

# 代理
# 没有使用代理
url = 'http://httpbin.org/ip'
resp = req.urlopen(url)
print(resp.read())

#使用代理
handler = req.ProxyHandler({'http': '183.164.238.243:42341'})
opener = req.build_opener(handler)
resp = opener.open(url)
print(resp.read())




