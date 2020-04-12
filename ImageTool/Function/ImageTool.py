
# importing tkinter and tkinter.ttk 
# and all their functions and classes 
from tkinter import * 
from tkinter.ttk import *
from PIL import Image, ImageTk

from tkinter import messagebox as mb

import subprocess
import Colour
# importing askopenfile function 
# from class filedialog 
from tkinter.filedialog import askopenfile
import os 
  
root = Tk() 
root.title("Kavya Didi")
root.geometry('2000x2000') 


  
# This function will be used to browse files and get its path
# file in read mode and only CSV files 
# will be opened 
def LoadImage():
	global ImageFile
	global width
	global height
	file = askopenfile(mode ='r', filetypes =[('Python Files', '*')]) 
	ImageFile=file.name 
	load = Image.open(ImageFile)
	render = ImageTk.PhotoImage(load)
	img = Label(root, image=render)
	img.image = render
	img.place(x=200, y=0)
	width, height = load.size

# Run Button 
def RunButton():
	global ImageFile
	global width
	Colour.ColorThreshold(ImageFile,int(RedScale.get()),int(BlueScale.get()),int(GreenScale.get()),int(SkipX.get()),int(SkipY.get()),Black.get(),White.get())
	load = Image.open('geeks.bmp')
	render = ImageTk.PhotoImage(load)
	img = Label(root, image=render)
	img.image = render
	img.place(x=250+width,y=0)
	
  

#For the Image Load
TypeText = Label(root,text="Load The Image")
TypeText.pack()
TypeText.place(x=0,y=0)
TypeBrowse = Button(root, text ='Open', command = lambda:LoadImage()) 
TypeBrowse.pack(side = TOP, pady = 10) 
TypeBrowse.place(x=110,y=0)

#Get Red Threshold Value
TypeText = Label(root,text="Red Threshold ")
TypeText.pack()
TypeText.place(x=0,y=30)
RedScale = Scale(root, from_=0, to=255,orient=HORIZONTAL)
RedScale.pack()
RedScale.place(x=0,y=60)

#Get Blue Threshold Value
TypeText = Label(root,text="Blue Threshold ")
TypeText.pack()
TypeText.place(x=0,y=90)
BlueScale = Scale(root, from_=0, to=255,orient=HORIZONTAL)
BlueScale.pack()
BlueScale.place(x=0,y=120)

#Get Green Threshold Value
TypeText = Label(root,text="Green Threshold ")
TypeText.pack()
TypeText.place(x=0,y=150)
GreenScale = Scale(root, from_=0, to=255,orient=HORIZONTAL)
GreenScale.pack()
GreenScale.place(x=0,y=180)

#Get Skip X
TypeText = Label(root,text="Skip X")
TypeText.pack()
TypeText.place(x=0,y=210)
SkipX = Entry(root, width=10)
SkipX.pack()
SkipX.place(x=110,y=210)

#Get Skip Y
TypeText = Label(root,text="Skip Y")
TypeText.pack()
TypeText.place(x=0,y=240)
SkipY = Entry(root, width=10)
SkipY.pack()
SkipY.place(x=110,y=240)

#Get Black
TypeText = Label(root,text="Black")
TypeText.pack()
TypeText.place(x=0,y=270)
Black = Entry(root, width=10)
Black.pack()
Black.place(x=110,y=270)

#Get White
TypeText = Label(root,text="White")
TypeText.pack()
TypeText.place(x=0,y=300)
White = Entry(root, width=10)
White.pack()
White.place(x=110,y=300)

#Build/Run Button
Run = Button(root, text ="Run", command = RunButton)
Run.pack()
Run.place(x=110,y=330)

mainloop()
