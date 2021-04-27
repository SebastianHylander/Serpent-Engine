import tkinter as tk
import Block_module as block

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

root = tk.Tk()
root.geometry("600x400")

root.wm_iconbitmap("logo.ico")
root.wm_title("Serpent Enigne")

sidebar = tk.Canvas(root, width=175, bg='grey', height=400, borderwidth=2)
sidebar.pack(fill='both', side='left')

scroll_frame = tk.Frame(sidebar, height = 2000, width = 175)
scroll_y = tk.Scrollbar(root, command = sidebar.yview)





sidebar.create_window(0,0, window = scroll_frame, anchor = "nw")
sidebar.update_idletasks()

sidebar.configure(scrollregion=sidebar.bbox('all'),yscrollcommand = scroll_y.set)


scroll_y.pack(side=tk.LEFT, fill = tk.Y)

root.mainloop()
