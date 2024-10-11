from tkinter import * 
from tkinter.ttk import *
from tkinter import messagebox as mb
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from tkinter import messagebox
import os
root = Tk() 
root.title("Create_SRT")
root.geometry('200x200')

def convert(seconds):
	seconds = seconds % 3600
	hour = int(seconds/3600)
	seconds = seconds%3600
	minutes = int(seconds/60)
	seconds %= 60
	return str('{:02}'.format(hour))+':'+str('{:02}'.format(minutes))+':'+str('{:02}'.format(seconds))

def CreatSRT(CSV_In,Label_In):
	head_tail = os.path.split(CSV_In)
	f = open(Label_In, "r")
	Text=f.read()
	f.close()
	Line=Text.split('\n')
	Start=[]
	Stop=[]
	Lable=[]
	for i in Line:
		t1 = i
		t2 = t1.split('\t')
		if len(t2)>=3:
			Start.append(convert(int(float(t2[0]))))
			Stop.append(convert(int(float(t2[1]))))
			Lable.append(t2[2])
	f = open(CSV_In, "r")
	CSV=f.read()
	f.close()
	CSVLine=CSV.split('\n')
	STR=''
	for i in range(0,len(CSVLine)):
		CSVTemp=CSVLine[i].split(',')
		if len(CSVTemp)>=2:
			STR=STR+str(i+1)+'\n'+Start[i]+' --> '+Stop[i]+'\n'+CSVTemp[1]+'\n\n'		
	f = open(head_tail[0]+"/Output.srt", "w")
	f.write(STR)
	f.close()
	messagebox.showinfo("Information", "Done")


def OpenFile():
	global HTMLFile
	file = askopenfile(mode ='r', filetypes =[('Label Files', '*')]) 
	HTMLFile=file.name
	TypeText = Label(root,text=HTMLFile)
	TypeText.pack()
	TypeText.place(x=100,y=0)

def OpenFile1():
	global HTMLFile1
	file = askopenfile(mode ='r', filetypes =[('CSV Files', '*')]) 
	HTMLFile1=file.name
	TypeText = Label(root,text=HTMLFile1)
	TypeText.pack()
	TypeText.place(x=100,y=30)

TypeBrowse = Button(root, text ='Label File', command = lambda:OpenFile()) 
TypeBrowse.pack(side = TOP, pady = 10) 
TypeBrowse.place(x=0,y=0)

TypeText = Label(root,text="Type File ")
TypeText.pack()
TypeText.place(x=100,y=0)

TypeBrowse = Button(root, text ='CSV File', command = lambda:OpenFile1()) 
TypeBrowse.pack(side = TOP, pady = 10) 
TypeBrowse.place(x=0,y=30)

TypeText = Label(root,text="Type File ")
TypeText.pack()
TypeText.place(x=100,y=30)

cwd = os.getcwd()

TypeBrowse1 = Button(root, text ='Run',command=lambda:CreatSRT(HTMLFile1, HTMLFile) ) 
TypeBrowse1.pack(side = TOP, pady = 10) 
TypeBrowse1.place(x=0,y=60)


mainloop()

