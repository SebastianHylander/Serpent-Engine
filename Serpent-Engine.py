import tkinter as tk
import Block_module as block

def make_draggable(widget):
    snapped = None
    widget.bind("<Button-1>", on_drag_start)
    widget.bind("<B1-Motion>", on_drag_motion)
    widget.bind("<ButtonRelease-1>", on_drag_stop)

def undraggable(widget):
    widget.unbind("<Button-1>")
    widget.unbind("<B1-Motion>")
    widget.unbind("<ButtonRelease-1>")

def on_drag_start(event):
    widget = event.widget
    widget._drag_start_x = event.x
    widget._drag_start_y = event.y

def on_drag_stop(event):
    global snap_y
    widget = event.widget
    y = widget.winfo_y()
    if snapped == True:
        snap_y = y + 35

def on_drag_motion(event):
    global snapped
    widget = event.widget
    x = widget.winfo_x() - widget._drag_start_x + event.x
    y = widget.winfo_y() - widget._drag_start_y + event.y
    widget.place(x=x, y=y)
    #Make widgets snappable
    snapped = False
    if snap_x-20 <= x <= snap_x+20 and snap_y-20 <= y <= snap_y+20:
        widget.place(x=snap_x, y=snap_y)
        snapped = True

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
