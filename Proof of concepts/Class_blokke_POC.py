import tkinter as tk
import time

root = tk.Tk()
root.geometry("600x400") #size of window

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

class Blok:

    def __init__(self,name,x,y,category):
        self.name = name
        self.x = x
        self.y = y

        if category == "n":
            self.w = 150
            self.h = 30
            self.canvas = tk.Canvas(root,width=self.w,height=self.h,bd=1, cursor="fleur")
            self.canvas.pack()

            shape = self.canvas.create_rectangle(self.x, self.y, self.x+self.w, self.y+self.h, fill='lightblue')
            label = self.canvas.create_text((10, self.h/2), text="Box text", anchor=tk.W)
            
            entry1 = tk.Entry(self.canvas) 
            self.entry = self.canvas.create_window(self.w/2, self.h/2, width= 20, window=entry1)
            
blok1 = Blok("blok1",0,0,"n")
make_draggable(blok1.canvas)

blok2 = Blok("blok2",0,0,"n")
make_draggable(blok2.canvas)

root.mainloop()