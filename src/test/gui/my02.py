"""测试一个经典的GUI程序写法，采用面向对象的方式"""


from tkinter import *
from tkinter import messagebox


class Application(Frame):
    """一个经典的程序的类的写法"""
    
    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        self.pack()
        
        self.create_widgets()
        
    
    def create_widgets(self):
        self.btn01 = Button(self)
        self.btn01['text'] = '点击送花'
        self.btn01['command'] = self.send_flowers
        self.btn01.pack()
        
        # create quit btn
        self.btnQuit = Button(self, text='退出', command = self.master.destroy)
        self.btnQuit.pack()
        
        
    def send_flowers(self):
        messagebox.showinfo('Send flowers', '送你一朵玫瑰花')
        
        
root = Tk()
root.geometry('500x300+200+100')
root.title('一个经典的GUI程序类的测试')
app = Application(master = root)

root.mainloop()