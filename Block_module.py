import tkinter as tk

root = tk.Tk()
root.geometry("600x400")

def make_draggable(widget):
    widget.bind("<Button-1>", on_drag_start)
    widget.bind("<B1-Motion>", on_drag_motion)

def on_drag_start(event):
    widget = event.widget
    widget._drag_start_x = event.x
    widget._drag_start_y = event.y

def on_drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget._drag_start_x + event.x
    y = widget.winfo_y() - widget._drag_start_y + event.y
    widget.place(x=x, y=y)

class Print:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.w = 150
        self.h = 30
        self.canvas = tk.Canvas(root,width=self.w,height=self.h,bd=0, cursor="fleur", bg="orange")
        self.canvas.place(x=self.x, y=self.y)

        self.canvas.create_text((10, self.h/2), text="Skriv", anchor=tk.W)

        self.entry1 = tk.Entry(self.canvas) 
        entry = self.canvas.create_window(40, self.h/2, width=105, window=self.entry1, anchor=tk.W)

class Forloop:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.w = 150
        self.h = 30
        self.canvas = tk.Canvas(root,width=self.w,height=self.h,bd=0, cursor="fleur", bg="cyan")
        self.canvas.place(x=self.x, y=self.y)

        self.canvas.create_text((10, self.h/2), text="Gentag", anchor=tk.W)
        self.canvas.create_text((80, self.h/2), text="gange", anchor=tk.W)

        self.entry1 = tk.Entry(self.canvas) 
        entry = self.canvas.create_window(50, self.h/2, width=25, window=self.entry1, anchor=tk.W)

class Lav_var:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.w = 150
        self.h = 30
        self.canvas = tk.Canvas(root,width=self.w,height=self.h,bd=0, cursor="fleur", bg="yellow")
        self.canvas.place(x=self.x, y=self.y)

        self.canvas.create_text((10, self.h/2), text="Ny variabel, navn:", anchor=tk.W)

        self.entry1 = tk.Entry(self.canvas) 
        entry = self.canvas.create_window(105, self.h/2, width=40, window=self.entry1, anchor=tk.W)

class Sæt_var:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.w = 150
        self.h = 30
        self.canvas = tk.Canvas(root,width=self.w,height=self.h,bd=0, cursor="fleur", bg="yellow")
        self.canvas.pack()
        self.canvas.place(x=self.x, y=self.y)

        self.canvas.create_text((10, self.h/2), text="Sæt", anchor=tk.W)
        self.canvas.create_text((10, self.h/2), text="til", anchor=tk.W)

        self.entry1 = tk.Entry(self.canvas) 
        entry = self.canvas.create_window(50, self.h/2, width=25, window=self.entry1, anchor=tk.W)
        self.entry2 = tk.Entry(self.canvas) 
        entry = self.canvas.create_window(50, self.h/2, width=25, window=self.entry2, anchor=tk.W)

def run():
    print(a.entry1.get())

button = tk.Button(root,text="fun :)",command=run)
button.pack()

a = Forloop()
b = Print()
c = Lav_var()
make_draggable(a.canvas)
make_draggable(b.canvas)
make_draggable(c.canvas)
root.mainloop()