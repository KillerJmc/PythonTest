import turtle

colors = 'black' ,'yellow', 'red', 'orange', 'green', 'blue', 'purple'

def draw_circles(t, colors, n, r):
    t = turtle.Pen()
    t.speed(0)
    t.width(3)
    for i in range(n):
        t.penup()
        t.goto(0, -i *  r)
        t.color(colors[i % len(colors)])
        t.pendown()
        t.circle((i + 1) * r)
        
        
draw_circles(turtle, colors, 10, 50)

# pause when accomplished
turtle.done() 