import tkinter as tk

class Start:
    def __init__(self,root):
        self.x = 312
        self.y = 35
        self.w = 150
        self.h = 30
        self.root = root

        self.canvas = tk.Canvas(self.root,width=self.w,height=self.h,bd=0, bg="grey")
        self.canvas.place(x=self.x, y=self.y)

        self.canvas.create_text((self.w/2, self.h/2), text="START", anchor=tk.CENTER)

class Print:

    def __init__(self,root,startpos):
        self.x = startpos[0]
        self.y = startpos[1]
        self.w = 150
        self.h = 30
        self.root = root
        self.canvas = tk.Canvas(self.root,width=self.w,height=self.h,bd=0, cursor="fleur", bg="orange")
        self.canvas.place(x=self.x, y=self.y)

        self.canvas.create_text((10, self.h/2), text="Skriv", anchor=tk.W)

        self.entry1 = tk.Entry(self.canvas) 
        entry = self.canvas.create_window(40, self.h/2, width=105, window=self.entry1, anchor=tk.W)
    
    def translate(self):
        entry = self.entry1.get()

        if '{' in entry and '}' in entry:

            code = 'print(f"{}")'.format(entry)
        else:
            code = 'print("{}")'.format(entry)

        return code,0

class Forloop:

    def __init__(self,root,startpos):
        self.x = startpos[0]
        self.y = startpos[1]
        self.w = 150
        self.h = 30
        self.root = root
        self.canvas = tk.Canvas(self.root,width=self.w,height=self.h,bd=0, cursor="fleur", bg="cyan")
        self.canvas.place(x=self.x, y=self.y)

        self.canvas.create_text((10, self.h/2), text="Gentag", anchor=tk.W)
        self.canvas.create_text((80, self.h/2), text="gange", anchor=tk.W)

        self.entry1 = tk.Entry(self.canvas) 
        entry = self.canvas.create_window(50, self.h/2, width=25, window=self.entry1, anchor=tk.W)

    def translate(self):
        code = "for i in range({}):".format(self.entry1.get())
        return code,1

class Forloopslut:

    def __init__(self,root,startpos):
        self.x = startpos[0]
        self.y = startpos[1]
        self.w = 150
        self.h = 30
        self.root = root
        self.canvas = tk.Canvas(self.root,width=self.w,height=self.h,bd=0, cursor="fleur", bg="cyan")
        self.canvas.place(x=self.x, y=self.y)

        self.canvas.create_text((10, self.h/2), text="Stop gentag", anchor=tk.W)

    def translate(self):

        return "#Gentag slut",-1

class Lav_var:

    def __init__(self,root,startpos):
        self.x = startpos[0]
        self.y = startpos[1]
        self.w = 150
        self.h = 30
        self.root = root
        self.canvas = tk.Canvas(self.root,width=self.w,height=self.h,bd=0, cursor="fleur", bg="yellow")
        self.canvas.place(x=self.x, y=self.y)

        self.canvas.create_text((10, self.h/2), text="Ny variabel, navn:", anchor=tk.W)

        self.entry1 = tk.Entry(self.canvas) 
        entry = self.canvas.create_window(105, self.h/2, width=40, window=self.entry1, anchor=tk.W)

    def translate(self):
        
        code = '{} = None'.format(self.entry1.get())
        return code,0


class Sæt_var:

    def __init__(self,root,startpos):
        self.x = startpos[0]
        self.y = startpos[1]
        self.w = 150
        self.h = 30
        self.root = root
        self.canvas = tk.Canvas(self.root,width=self.w,height=self.h,bd=0, cursor="fleur", bg="yellow")
        self.canvas.place(x=self.x, y=self.y)

        self.canvas.create_text((10, self.h/2), text="Sæt", anchor=tk.W)

        self.entry1 = tk.Entry(self.canvas) 
        entry = self.canvas.create_window(35, self.h/2, width=40, window=self.entry1, anchor=tk.W)

        self.canvas.create_text((80, self.h/2), text="til", anchor=tk.W)

        self.entry2 = tk.Entry(self.canvas) 
        entry = self.canvas.create_window(95, self.h/2, width=40, window=self.entry2, anchor=tk.W)

    def translate(self):
        code = '{} = {}'.format(self.entry1.get(),self.entry2.get())
        return code,0