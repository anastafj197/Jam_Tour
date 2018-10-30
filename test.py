from tkinter import *
from PIL import ImageTK, Image

master = TK()
canvas = Canvas(root, width = 500, height = 500)
canvas.pack()
img = ImageTK.PhotoImage(Image.open(states.png))
canvas.create_image(20, 20, anchor=NW, image=img)  
root.mainloop() 
