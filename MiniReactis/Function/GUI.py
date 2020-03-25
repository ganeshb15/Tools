
# importing tkinter and tkinter.ttk 
# and all their functions and classes 
from tkinter import * 
from tkinter.ttk import *


from tkinter import messagebox as mb
import TestCreation
import subprocess
  
# importing askopenfile function 
# from class filedialog 
from tkinter.filedialog import askopenfile
import os 
  
root = Tk() 
root.title("MiniReactis")
root.geometry('200x200') 


  
# This function will be used to browse files and get its path
# file in read mode and only CSV files 
# will be opened 
def OpenFile_Type():
	global TypeFile
	file = askopenfile(mode ='r', filetypes =[('Python Files', '*.csv')]) 
	TypeFile=file.name 
	#print(TypeFile)

def OpenFile_CSV():
	global CSV
	file = askopenfile(mode ='r', filetypes =[('Python Files', '*.csv')]) 
	CSV=file.name 
	#print(CSV)
def OpenFile_File():
	global CFile
	file = askopenfile(mode ='r', filetypes =[('Python Files', '*.c')]) 
	CFile=file.name 
	#print(CSV)

# Run Button 
def RunButton():
	global CSV
	global TypeFile
	global CFile
	TestCreation.testFunction(CSV,TypeFile,FunctionName.get(),HeaderName.get(),OutputName.get(),CFile)
	
	CFile_Split = os.path.split(CFile) 
	GccOutput="gcc "+CFile_Split[0]+"/demofile2.c "+CFile+" -o "+CFile_Split[0]+"/outputfile"
	
	GccTerminal=subprocess.getstatusoutput(GccOutput)
	os.remove(CFile_Split[0]+"/demofile2.c")
	Satus=0
	if GccTerminal[0] !=0:
		mb.showinfo('Output Status 1', 'Following is the ERROR while Building:'+GccTerminal[1])
				
	else:
		Satus=1
		mb.showinfo('Output Status 1', 'Succesfully Outputfile Built')

	cwd = os.getcwd()
		
	if Satus==1:
		GccOutput='cd '+CFile_Split[0]+'; ./outputfile; cd '+cwd
		GccTerminal=subprocess.getstatusoutput(GccOutput)
		
		if GccTerminal[0] !=0:
			mb.showinfo('Output Status 2', 'Following is the ERROR while Execution:'+GccTerminal[1])
		else:
			mb.showinfo('Output Status 2', 'Succesfully Outputfile Created ')

	
  

#For the Type File
TypeText = Label(root,text="Type File ")
TypeText.pack()
TypeText.place(x=0,y=0)
TypeBrowse = Button(root, text ='Open', command = lambda:OpenFile_Type()) 
TypeBrowse.pack(side = TOP, pady = 10) 
TypeBrowse.place(x=110,y=0)


#For the Type File
TypeText = Label(root,text="CSV Test File ")
TypeText.pack()
TypeText.place(x=0,y=30)
TypeBrowse = Button(root, text ='Open', command = lambda:OpenFile_CSV()) 
TypeBrowse.pack(side = TOP, pady = 10) 
TypeBrowse.place(x=110,y=30)

#Get Function Name
TypeText = Label(root,text="Function Name")
TypeText.pack()
TypeText.place(x=0,y=60)
FunctionName = Entry(root, width=10)
FunctionName.pack()
FunctionName.place(x=110,y=60)

#Get File  Name
TypeText = Label(root,text="CFile Name ")
TypeText.pack()
TypeText.place(x=0,y=85)
FileName = Button(root, text ='Open', command = lambda:OpenFile_File()) 
FileName.pack(side = TOP, pady = 10) 
FileName.place(x=110,y=85)


#Get Header Name
TypeText = Label(root,text="Header Name")
TypeText.pack()
TypeText.place(x=0,y=110)
HeaderName = Entry(root, width=10)
HeaderName.pack()
HeaderName.place(x=110,y=110)

#Get OutputFile Name
TypeText = Label(root,text="Output csvName")
TypeText.pack()
TypeText.place(x=0,y=135)
OutputName = Entry(root, width=10)
OutputName.pack()
OutputName.place(x=110,y=135)

#Build/Run Button
Run = Button(root, text ="Run", command = RunButton)
Run.pack()
Run.place(x=110,y=160)

mainloop()
