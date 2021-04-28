import tkinter as tk
import Block_module as block

blocks = []

snap_x = 100
snap_y = 100



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

def add_print(event):
    x = event.widget.canvasx(event.x)
    y = event.y_root - root.winfo_y() - event.widget.winfo_height()
    blocks.append(block.Print(root,(x, y)))
    make_draggable(blocks[-1].canvas)
    blocks[-1].canvas.bind("<Button-3>",delete_block)

def add_forloop(event):
    x = event.widget.canvasx(event.x)
    y = event.y_root - root.winfo_y() - event.widget.winfo_height()
    blocks.append(block.Forloop(root,(x, y)))
    make_draggable(blocks[-1].canvas)
    blocks[-1].canvas.bind("<Button-3>",delete_block)

def add_lavvar(event):
    x = event.widget.canvasx(event.x)
    y = event.y_root - root.winfo_y() - event.widget.winfo_height()
    blocks.append(block.Lav_var(root,(x, y)))
    make_draggable(blocks[-1].canvas)
    blocks[-1].canvas.bind("<Button-3>",delete_block)

def add_sætvar(event):
    x = event.widget.canvasx(event.x)
    y = event.y_root - root.winfo_y() - event.widget.winfo_height()
    blocks.append(block.Sæt_var(root,(x, y)))
    make_draggable(blocks[-1].canvas)
    blocks[-1].canvas.bind("<Button-3>",delete_block)

def delete_block(event):
    for block in blocks:
        if block.canvas == event.widget:
            block.canvas.destroy()
            blocks.remove(block)





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

print_block = block.Print(scroll_frame,(8,0))
print_block.canvas.bind("<Button-1>", add_print)

forloop_block = block.Forloop(scroll_frame,(8,50))
forloop_block.canvas.bind("<Button-1>", add_forloop)

lavvar_block = block.Lav_var(scroll_frame,(8,100))
lavvar_block.canvas.bind("<Button-1>", add_lavvar)

sætvar_block = block.Sæt_var(scroll_frame,(8,150))
sætvar_block.canvas.bind("<Button-1>", add_sætvar)

start_block = block.Start(root)




sidebar.configure(scrollregion=sidebar.bbox('all'),yscrollcommand = scroll_y.set)


scroll_y.pack(side=tk.LEFT, fill = tk.Y)

root.mainloop()
