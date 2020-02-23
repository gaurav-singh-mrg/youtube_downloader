import subprocess
from select import poll
from subprocess import call
from tkinter import filedialog
from tkinter import *
import threading
import os
import sys
from PIL import Image, ImageTk
from tkinter import messagebox

root=Tk()
root.title("YouTube Downloader")
#root.iconbitmap("icon.png")
root.geometry("500x400")
root.configure()
#root.resizable(0,0)
photo=PhotoImage(file=r"icons/logo.png")

global b
global m
global l
global a
b=0
m=0
l=0
a=0

''' Comments
--write-thumbnail                Write thumbnail image to disk
--write-all-thumbnails           Write all thumbnail image formats to disk
--list-thumbnails                Simulate and list all available thumbnail
                                 formats'''
def btn_configure(num):
    global best
    global medium
    global low
    global audio
    global b
    global m
    global l
    global a
    if(num == 1):
        best.configure(state="active")
        medium.configure(state="normal")
        low.configure(state="normal")
        audio.configure(state="normal")
        b=1
        m=0
        l=0
        a=0
    elif(num==2):
        best.configure(state="normal")
        medium.configure(state="active")
        low.configure(state="normal")
        audio.configure(state="normal")
        b=0
        m=1
        l=0
        a=0
    elif(num==3):
        best.configure(state="normal")
        medium.configure(state="normal")
        low.configure(state="active")
        audio.configure(state="normal")
        b=0
        m=0
        l=1
        a=0
    else:
        best.configure(state="normal")
        medium.configure(state="normal")
        low.configure(state="normal")
        audio.configure(state="active")
        b=0
        m=0
        l=0
        a=1

def on_download():
    global b
    global m
    global l
    global a
    if(b==1):
        thread_download=threading.Thread(target=b_download())
        thread_download.start()
    elif(m==1):
        thread_download=threading.Thread(target=m_download())
        thread_download.start()
    elif(l==1):
        thread_download=threading.Thread(target=l_download())
        thread_download.start()
    elif(a==1):
        thread_download=threading.Thread(target=a_download())
        thread_download.start()



def show_thumbnail():
    global inputPath
    global best
    global medium
    global low
    global audio
    for imageName in os.listdir():
        inputPath=os.fsdecode(imageName)
        if inputPath.endswith(".jpg") or  inputPath.endswith(".png"):
            image=os.fsdecode(inputPath)
            print(inputPath)
    clear()
    photo_label=Label(image=photo)
    photo_label.grid(row=0,column=0,columnspan=4)
    Label(text="Select Download Quality:").grid(row=1,column=0,columnspan=4,pady=(30))
    best = Button(text="Best",
           padx=25,
           fg="green",
           width=8,
           state="active",
                  command=lambda :btn_configure(1)
          )
    best.grid(row=2, column=0)
    medium=Button(text="Medium",
           padx=25,
           fg="green",
           width=8,
                  command=lambda: btn_configure(2)
           )
    medium.grid(row=2,column=1)
    low=Button(text="Low",
           padx=25,
           fg="green",
           width=8,
               command=lambda: btn_configure(3)
           )
    low.grid(row=2,column=2)
    audio=Button(text="Audio",
           padx=25,
           fg="green",
           width=8,
                 command=lambda: btn_configure(4)
           )
    audio.grid(row=2,column=3)
    back=Button(text="Back",
           padx=25,
           fg="green",
           font=("Helvetica"),
           command=on_start
           )
    back.grid(row=3,column=0,pady=(30),sticky=SW)
    download=Button(text="Download",
           padx=25,
           fg="green",
           font=("Helvetica"),
           command=on_download
           )
    download.grid(row=3,column=3,pady=(30),sticky=SE)

def thumbnail():
    print(e1.get())
    command="youtube-dl "+e1.get()+"  --write-thumbnail  --skip-download  --no-check-certificate"
    web=call(command.split(), shell=False)
    if web == 0:
        print("Thumbnail Downloaded")
        show_thumbnail()
    else:
        print(web)
        messagebox.showerror('Error', "Something Went Wrong,Please contact Developer")
        dbtn.config(text="Download", state=ACTIVE)

def waithere():
    global board
    var = IntVar()
    root.after(3000, var.set, 1)
    print("waiting...")
    board.wait_variable(var)



def b_download():
    global e1
    command="youtube-dl -f bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best  --no-check-certificate "+e1.get()
    #command="youtube-dl "+e1.get()+"--skip-download  --no-check-certificate "
    print("b_Downloded")
    trigger=call(command.split(), shell=False)
    if(trigger==0):
        print("Downloded")

def m_download():
    global e1
    command="youtube-dl -f 'bestvideo[height<=480]+bestaudio/best[height<=480]'  --no-check-certificate "+e1.get()
    #command="youtube-dl "+e1.get()+"--skip-download  --no-check-certificate "
    print("m_Downloded")
    trigger=call(command.split(), shell=False)
    if(trigger==0):
        print("Downloded")

def l_download():
    global e1
    command="youtube-dl -f 'bestvideo[height<=480]+bestaudio/best[height<=240]' --no-check-certificate "+e1.get()
    #command="youtube-dl "+e1.get()+"--skip-download  --no-check-certificate "
    print("L_Downloded")
    trigger=call(command.split(), shell=False)
    if(trigger==0):
        print("Downloded")

def a_download():
    global e1
    command="youtube-dl --extract-audio --no-check-certificate "+e1.get()
    #command="youtube-dl "+e1.get()+"--skip-download  --no-check-certificate "
    print("a_Downloded")
    trigger=call(command.split(), shell=False)
    if(trigger==0):
        print("Downloded")



def initilize():
    try:
        setting=open("setting.txt","r")
    except:
        setting=open("setting.txt","w+")
        setting.write("1. Only_audio = %d \n 2. Quality = %d")
    #Force_Resume = 0(--continue/-c)
    #No_Force_Resume = 0(--no-continue)
    #Write_Description =0 (--write-description)
    #Disable_Caching = 0(--no-cache-dir)
    #Clear_All_Caching_Data =0(--rm-cache-dir)
    #Best_Quality = HD/SD
    #Retries = 0 (default = 10)
    #Updates = (youtube-dl,pip)




def on_start():
    initilize()
    clear()
    photo_label=Label(image=photo)
    photo_label.grid(row=0,column=0,columnspan=4)
    global e1
    global dbtn
    e1=Entry(root,width=40)
    e1.grid(row=1,column=0,columnspan=4)
    dbtn=Button(text="Download",padx=30, command=on_click_download)
    dbtn.grid(row=2, column =1,columnspan=2)

def clear():
    list=root.grid_slaves()
    for l in list:
        l.destroy()

def on_click_download():
    global dbtn
    dbtn.config(text="Please Wait..", state=DISABLED)
    global thread_thumbnail
    thread_thumbnail = threading.Thread(target=thumbnail)
    thread_thumbnail.start()



on_start()
root.mainloop()

