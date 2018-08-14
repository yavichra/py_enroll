from tkinter import filedialog
from tkinter import Text, Scrollbar, Frame, Tk, Button, LEFT

def quit_app():
    global root
    root.destroy()
    
def loadfile(): 
    global textbox
    filename = filedialog.askopenfile(filetypes = [('*.txt files', '.txt')])
    if filename:
        textbox.delete('1.0', 'end')
        textbox.insert('1.0', open(filename.name, 'rt').read())

def savefile():
    global textbox
    filename = filedialog.asksaveasfile(filetypes = [('*.txt files', '.txt')])
    if filename:
        open(filename.name, 'wt').write(textbox.get('1.0', 'end'))

root = Tk()

panelFrame = Frame(root, height = 60, bg = 'gray')
textFrame = Frame(root, height = 340, width = 600)

panelFrame.pack(side = 'top', fill = 'x')
textFrame.pack(side = 'bottom', fill = 'both', expand = 1)

textbox = Text(textFrame, font='Arial 14', wrap='word')
scrollbar = Scrollbar(textFrame)

scrollbar['command'] = textbox.yview
textbox['yscrollcommand'] = scrollbar.set

textbox.pack(side = 'left', fill = 'both', expand = 1)
scrollbar.pack(side = 'right', fill = 'y')





loadBtn = Button(panelFrame, text = 'Load', command = loadfile)
loadBtn.pack(side=LEFT, padx=(10,5), pady=5)
saveBtn = Button(panelFrame, text = 'Save', command = savefile)
saveBtn.pack(side=LEFT, padx=5, pady=5)
quitBtn = Button(panelFrame, text = 'Quit', command = quit_app)
quitBtn.pack(side=LEFT, padx=5, pady=5)
# loadBtn.bind("<Button-1>", LoadFile)
# saveBtn.bind("<Button-1>", SaveFile)
# quitBtn.bind("<Button-1>", Quit)


# loadBtn.place(x = 10, y = 10, width = 40, height = 40)
# saveBtn.place(x = 60, y = 10, width = 40, height = 40)
# quitBtn.place(x = 110, y = 10, width = 40, height = 40)

root.mainloop()
