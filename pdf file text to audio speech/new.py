from tkinter import *
from tkinter import filedialog

import pyttsx3
import PyPDF2
from tkinter import *

Window = Tk()
Window.geometry('500x350')
Window.config(bg="orange")
Window.title("Convert PDF File Text to Audio Speech by TechVidvan")

page1= Label(Window, text=" Enter starting page number")
startingpagenumber = Entry(Window)
page1.place(relx=0.02,rely=0.1)
startingpagenumber.place(relx=0.6,rely=0.1)

label = Label(Window, text="Select the book you want to read.")
label.place(relx=0.3,rely=0.2)
def file():
    path = filedialog.askopenfilename()
    book = open(path, 'rb')
    pdfreader = PyPDF2.PdfFileReader(book)
    pages = pdfreader.numPages
    speaker = pyttsx3.init()
    
    for i in range(int(startingpagenumber.get()), pages):
        page = pdfreader.getPage(i) 
        txt = page.extractText()
        speaker.say(txt)
        speaker.runAndWait()

B=Button(Window, text="Choose  the Book", command=file)
B.place(relx=0.4,rely=0.3)

mainloop()