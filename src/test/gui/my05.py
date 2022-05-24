import sys


sys.path.append('../')


from ..main.tools import Tools
from tkinter import *
from tkinter import messagebox


class Application(Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        self['bg'] = 'white'
        self.pack()

        self.create_widgets()


    def create_widgets(self):
        self.label01 = Label(self, text = '用户名', width = 100, font = ('宋体', 15), bg = 'white')
        self.label01.pack()

        # sv变量绑定到指定的组件
        v1 = StringVar()
        self.entry01 = Entry(self, textvariable = v1, font = ('宋体', 15))
        self.entry01.pack()
        v1.set('admin')
        #Tools.printToTemp(v1.get())
        #Tools.printToTemp(self.entry01.get())

        self.label02 = Label(self, text = '密码', width = 100, font = ('宋体', 15), bg = 'white')
        self.label02.pack()

        v2 = StringVar()
        self.entry02 = Entry(self, textvariable = v2, font = ('宋体', 15), show = '*')
        self.entry02.pack()

        Button(self, text = '登录', width = 10, command = self.login).pack()


    def login(self):
        uname = self.entry01.get()
        pwd = self.entry02.get()

        if uname == 'Jmc' and pwd == '123':
            messagebox.showinfo('System', '登录成功，欢迎' + uname + '回来')
        else:
            messagebox.showinfo('System', '登录失败！账号或密码错误。')

        Tools.printToTemp('用户名：'\
        + uname + '\n密码：' + pwd)



root = Tk()
root['bg'] = 'white'

app = Application(master = root)

root.mainloop()
