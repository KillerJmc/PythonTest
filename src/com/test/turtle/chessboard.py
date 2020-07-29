import turtle


t = turtle.Pen()
t.width(3)
t.speed(0)

# y(500 ~ -500)
y = [i for i in range(500, -550, -50)]
# x(-500 ~ 500)
x = y[::-1]

# draw horizontal lines
for i in y:
    t.penup()
    t.goto(-500, i)
    t.pendown()
    t.goto(500, i)

# draw vertical lines
for i in x:
    t.penup()
    t.goto(i, 500)
    t.pendown()
    t.goto(i, -500)
    
# draw numbers
count = 1
for x in range(-510, 490 + 50, 50): 
    t.penup()
    t.goto(x, 500)
    t.write(count % 10)
    t.goto(x, -550)
    t.write(count % 10)
    count += 1
    
count = 1
for y in range(473, -527 - 50, -50):
    t.penup()
    t.goto(-530, y)
    t.write(count % 10)
    t.goto(510, y)
    t.write(count % 10)
    count += 1
t.write(1)
    
def sw(x, y):
    """放白棋子，x, y 属于[1, 21]"""
    t.penup()
    t.goto(50 * y - 550, -50 * x + 526)
    t.pendown()
    t.circle(25)

def sk(x, y):
    """放黑棋子"""
    sw(x, y)
    for r in range(1, 25):  
        t.circle(r)
     
def do():
    print()
    sk(11, 11)
    sw(12, 12)
    sk(11, 12)
    sw(11, 10)
    sk(12,11)
    sw(10, 11)
    sk(9, 12)
    sw(13, 10)
    sk(10, 10)
    sw(12, 9)
    sk(13, 9)
    sw(13, 8)
    sk(14, 7)
    sw(11, 8)
    sk(14, 11)
    sw(10, 7)
    sk(9, 6)
    sw(12, 8)
    sk(13, 11)
    sw(15, 11)
    sk(14, 8)
    sw(10, 8)
    sk(9, 8)
    sw(12, 10)
    sk(14, 9)
    sw(14, 10)
    sk(15, 10)
    sw(12, 7)
    sk(12, 6)
    sw(13, 6)
    sk(14, 5)
    sw(14, 6)
    sk(13, 7)
    sw(15, 9)
    sk(9, 7)
    sw(9, 5)
    sk(10, 4)
    sw(11, 5)
    sk(10, 6)
    sw(11, 6)
    sk(11, 9)
    sw(10, 5)
    sk(12, 5)
    sw(9, 4)
              
do()
turtle.done()