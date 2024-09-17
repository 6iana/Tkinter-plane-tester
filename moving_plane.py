# Import the required libraries

from tkinter import *

from PIL import Image, ImageTk

 

# Create an instance of tkinter frame

root = Tk()

 

# Set the size of the tkinter window

root.geometry("700x350")

 

# Define a Canvas widget

c = Canvas(root, width=600, height=400, bg="white")

c.pack(pady=20)

 

# Add Images to Canvas widget

image = ImageTk.PhotoImage(Image.open('plane.png'))

img = c.create_image(250, 120, anchor=NW, image=image)

 

 

def left(e):

    x = -20

    y = 0

    c.move(img, x, y)

 

def right(e):

   x = 20

   y = 0

   c.move(img, x, y)

 

def up(e):

   x = 0

   y = -20

   c.move(img, x, y)

 

def down(e):

   x = 0

   y = 20

   c.move(img, x, y)

 

# Bind the move function

root.bind("<Left>", left)

root.bind("<Right>", right)

root.bind("<Up>", up)

root.bind("<Down>", down)

 

root.mainloop()