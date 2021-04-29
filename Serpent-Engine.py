import tkinter as tk
import Block_module as block

Block_class = ["Print", "Forloop", "Forloopslut", "Lav_var", "Sæt_var"]

blocks = []

program_blocks = []

snap_x = 312
snap_y = 35 + 35

def make_draggable(widget):
    snapped = None
    widget.bind("<Button-1>", on_drag_start)
    widget.bind("<B1-Motion>", on_drag_motion)
    widget.bind("<ButtonRelease-1>", on_drag_stop)

def undraggable(widget):
    widget.unbind("<Button-1>")
    widget.unbind("<B1-Motion>")
    widget.unbind("<ButtonRelease-1>")
    widget.unbind("Button-3")

def on_drag_start(event):
    global snap_y
    widget = event.widget
    widget._drag_start_x = event.x
    widget._drag_start_y = event.y
    if len(program_blocks) > 0:
        if program_blocks[-1] == widget:
            program_blocks.remove(widget)
            if len(program_blocks) > 0:
                make_draggable(program_blocks[-1])
                program_blocks[-1].bind("<Button-3>",delete_block)
    snap_y = 35 + 35 + len(program_blocks)*35
    
def on_drag_stop(event):
    widget = event.widget
    if snapped == True:
        program_blocks.append(widget)
        if len(program_blocks) > 1:
            undraggable(program_blocks[-2])
        
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

def add_block(event, blocktype):
    x = event.widget.canvasx(event.x)
    y = event.y_root - root.winfo_y() - event.widget.winfo_height()
    eval("blocks.append(block.{}(root,(x, y)))".format(blocktype))
    make_draggable(blocks[-1].canvas)
    blocks[-1].canvas.bind("<Button-3>",delete_block)

def delete_block(event):
    widget = event.widget
    for block in blocks:
        if block.canvas == widget:
            block.canvas.destroy()
            blocks.remove(block)
            if len(program_blocks) > 0:
                if program_blocks[-1] == widget:
                    program_blocks.remove(widget)

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

sidebar_blocks = []
for i in range(len(Block_class)):
    new_block_y = 50 * i
    sidebar_blocks.append(eval("block.{}(scroll_frame,(8,{}))".format(Block_class[i],new_block_y)))

sidebar_blocks[0].canvas.bind("<Button-1>", lambda event: add_block(event,Block_class[0]))
sidebar_blocks[1].canvas.bind("<Button-1>", lambda event: add_block(event,Block_class[1]))
sidebar_blocks[2].canvas.bind("<Button-1>", lambda event: add_block(event,Block_class[2]))
sidebar_blocks[3].canvas.bind("<Button-1>", lambda event: add_block(event,Block_class[3]))
sidebar_blocks[4].canvas.bind("<Button-1>", lambda event: add_block(event,Block_class[4]))

start_block = block.Start(root)

sidebar.configure(scrollregion=sidebar.bbox('all'),yscrollcommand = scroll_y.set)

scroll_y.pack(side=tk.LEFT, fill = tk.Y)

def run():
    newfile = "{}.py".format(filename.get())
    tab = 0
    with open(newfile,'w') as f:
        for codeblock in program_blocks:
            for block in blocks:
                if  block.canvas == codeblock:
                    code,inc = block.translate()
                    f.write(tab * "    " + code)
                    f.write('\n')
                    tab = tab + inc

filenamecanvas = tk.Canvas(root, width = 150, height = 10)
filenamecanvas.place(x =314, y = 20)

filename = tk.Entry(root) 
filenamecanvas.create_window(0,0, width=150, window=filename, anchor=tk.W)
filename.insert(0, "filename")

button = tk.Button(root,text="MAKE PROGRAM",command=run, bg="lime")
button.place(x=480,y=10)

root.mainloop()