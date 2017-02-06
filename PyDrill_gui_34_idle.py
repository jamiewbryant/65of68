import shutil, sys, time, os
from tkinter import *
import tkinter as tk 
from tkinter import Button
class App:
  
  def __init__(self, master):
    
    def fromSource(): # defines an event function - for click of button
        sourcePath = tk.filedialog.askdirectory()
        print(sourcePath)
    def toReceive(): # defines an event function - for click of button
        receivePath = tk.filedialog.askdirectory()
        print(receivePath)
    def fileMove():
        source = 'c:/Users/Bryant/Desktop/DailyFiles/'
        dest = 'c:/Users/Bryant/Desktop/HomeOffice/'
        files = os.listdir(source)

        now = time.time()
        for f in files:
            src = source+f
            dst = dest+f
            if os.stat(src).st_mtime > now - 1 * 86400:
                if os.path.isfile(src):
                    shutil.move(src, dst)
                    print("File move is Alright, Alright, Alright")
    frame = Frame(master)
    frame.pack()
    self.button = Button(frame, 
                         text="Source", fg="red",
                         command=fromSource)
    self.button.pack(side=LEFT)
    self.slogan = Button(frame,
                         text="Receive", fg="green",
                         command=toReceive)
    self.slogan.pack(side=LEFT)
    self.button = Button(frame, 
                         text="Move", fg="black",
                         command=fileMove)
    self.button.pack(side=LEFT)
  

root = Tk()
app = App(root)
root.mainloop()
