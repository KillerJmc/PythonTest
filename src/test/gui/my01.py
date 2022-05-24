from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('我的第一个GUI程序')
# 500x300，距左边100距上面200
root.geometry('500x300+100+200')

btn01 = Button(root)
btn01['text'] = '点我就送花'

btn01.pack()

def deliver_flowers(e):
    """e: event object"""
    messagebox.showinfo('Message!', '送你一朵花')
    print('送你花了')
    

btn01.bind('<Button-1>', deliver_flowers)
    

# 进入组件的事件循环
root.mainloop()