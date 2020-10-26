import tkinter
from tkinter import *
import tkinter as tk
import webbrowser
import speedtest

root=tk.Tk()
root.title("Network Speed Test | Manjunathan")
root.geometry("550x500")
root.iconphoto(True,tk.PhotoImage(file="icon.png"))
root.config(bg="#15d798")
photo = PhotoImage(file = "button.png")

def getNetSpeed():
	speedTestHelper = speedtest.Speedtest()

	speedTestHelper.upload()

	upload=speedTestHelper.upload()/1000000

	download=speedTestHelper.download()/1000000

	labelUploadSpeed=Label(root,text="{:.2f}".format(upload)+" MB/S",font=("font awesome",15,"bold italic"),bg="#15d798",fg="white")
	labelUploadSpeed.place(x=340,y=200)
	
	labelDownloadSpeed=Label(root,text="{:.2f}".format(download)+" MB/S",font=("font awesome",15,"bold italic"),bg="#15d798",fg="white")
	labelDownloadSpeed.place(x=340,y=300)

def clear():
	pass

buttonCheck=Button(root, image = photo,bd=0,borderwidth=0,bg="#15d798",activebackground="#15d798",highlightthickness = 0,command=getNetSpeed)
buttonCheck.place(x=220,y=50)

labelUpload=Label(root,text="Upload Speed   	: ",font=("font awesome",15,"bold italic"),bg="#15d798",fg="white")
labelUpload.place(x=40,y=200)

labelDownload=Label(root,text="Download Speed   	: ",font=("font awesome",15,"bold italic"),bg="#15d798",fg="white")
labelDownload.place(x=40,y=300)

buttonExit=Button(root,text="Exit",fg="#15d798",bg="#ffffff",font=("courier",15,"bold italic"),width=7,borderwidth=6,command=root.destroy)
buttonExit.place(x=120,y=400)

buttonContact=Button(root,text="Contact",fg="#15d798",bg="#ffffff",font=("courier",15,"bold italic"),width=7,borderwidth=6,command=lambda: webbrowser.open("https://github.com/cmanjunathan45/"))
buttonContact.place(x=300,y=400)


root.mainloop()
