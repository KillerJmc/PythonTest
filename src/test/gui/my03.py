import os
from tkinter import *


class Application(Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        self['bg'] = 'white'
        self.pack()
        
        self.create_widgets()
        
    
    def create_widgets(self):
        self.label01 = Label(self, text = 'OKSir', width = 10, height = 2, bg = 'black', fg = 'white')
        self.label01.pack()
        
        self.label02 = Label(self, text = 'NB克拉斯', width = 10, height = 2, bg = 'blue', fg = 'white', font = ('黑体', 30))
        self.label02.pack()
        
        # 显示图像
        os.chdir('../../../temp')
        # 把photo声明为全局变量，如果为局部变量，本方法执行完毕后，图像对象销毁，窗口显示不出来
        global photo 
        photo = PhotoImage(file = 'logo.gif')
        self.label03 = Label(self, image = photo)
        self.label03.pack()
        
        # relief: 边界效果
        self.label04 = Label(self, text = '我觉得\n很OK\n你觉得呢', borderwidth = 1, relief = 'solid', justify = 'right', bg = 'white')
        self.label04.pack()
        
        
root = Tk()
root['bg'] = 'white'

app = Application(master = root)

root.mainloop()