from tkinter import *


class Application(Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        self['bg'] = 'white'
        self.pack()
        
        self.create_widgets()
        
    
    def create_widgets(self):
        # anchor(锚): southeast
        self.btn01 = Button(self, text = 'OKSir', width = 10, height = 2, anchor = SE)
        self.btn01.pack()
        
        
root = Tk()
root['bg'] = 'white'

app = Application(master = root)

root.mainloop()