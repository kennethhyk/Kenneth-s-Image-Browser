from tkinter import *
from os import listdir
from os.path import isfile, join
import os
from PIL import Image, ImageTk
import math

L = []
info=[0,0,0]##info, info, previous, next

for f in listdir(os.getcwd()):
	if isfile(join(os.getcwd(),f)):
		L.append(f)
		
x=len(L)-1
for i in reversed(L):
	print(x)
	print(L[x])
	if ('.gif' not in i) and ('.jpg' not in i) and ('.jpeg' not in i):
		print('poped',L.pop(x))
	x=x-1

root = Tk()
###
def gotoP():
	print('p')
	info[1]=1
	rsizeH=0
	rsizeW=0
	info[0]=info[0]-1
	if info[0]<0:
		c=0-info[0]
		info[0]=len(L)-c
	image1=Image.open(L[info[0]])
	if image1.size[0]>1025 and image1.size[0]<2049:
		rsizeH=math.trunc(image1.size[0]*0.6)
		rsizeW=math.trunc(image1.size[1]*0.6)
	elif image1.size[0]>2049 and image1.size[0]<5000:
		rsizeH=math.trunc(image1.size[0]*0.2)
		rsizeW=math.trunc(image1.size[1]*0.2)
	elif image1.size[0]>5000:
		rsizeH=math.trunc(image1.size[0]*0.01)
		rsizeW=math.trunc(image1.size[1]*0.01)
	else:
		rsizeH=image1.size[0]
		rsizeW=image1.size[1]
	image1 = image1.resize((rsizeH, rsizeW), Image.ANTIALIAS) 
	photo1=ImageTk.PhotoImage(image1)
	label1=Label(root,image=photo1)
	"""photo1=PhotoImage(file=L[info[0]])
	label1=Label(root,image=photo1)"""
	label1.image = photo1
	label1.grid(row=0,columnspan=2)
###
def gotoN():
	print('n')
	info[2]=1
	rsizeH=0
	rsizeW=0
	info[0]=info[0]+1
	if info[0]>len(L)-1:
		info[0]=info[0]%len(L)
	image2=Image.open(L[info[0]])
	if image2.size[0]>1025 and image2.size[0]<2048:
		rsizeH=math.trunc(image2.size[0]*0.6)
		rsizeW=math.trunc(image2.size[1]*0.6)
	else:
		rsizeH=image2.size[0]
		rsizeW=image2.size[1]
	image2 = image2.resize((rsizeH, rsizeW), Image.ANTIALIAS) 
	photo2=ImageTk.PhotoImage(image2)
	label2=Label(root,image=photo2)
	label2.image = photo2
	label2.grid(row=0,columnspan=2)

def main():
	print(L)
	root.wm_title("Kenneth's Image Browser")
	previous=Button(root,text='Previous',command=gotoP)
	previous.grid(row=3,column=0,sticky=E)
	next=Button(root,text='Next',command=gotoN)
	next.grid(row=3,column=1,sticky=W)
	root.mainloop()

main()
