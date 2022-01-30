from asyncio.windows_events import NULL
from operator import ge
import tkinter as tk
import os 
from tkinter import *
from tkinter import ttk
import tkinter
from tkinter import messagebox
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from matplotlib.pyplot import get


def Submit():
    if Name.get()=="" or Semester.get()=="" or USN.get()=="" or Branch.get()=="" or Feedback.get()=="":
        messagebox.showerror("Error","Fields Empty")
        return 

    form=db.collection('StudentFeedback').document()
    form.set({
        'Name':Name.get(),
        'Semester':Semester.get(),
        'USN':USN.get(),
        'Branch':Branch.get(),
        'Feedback':Feedback.get()
    })
    
    Name.set('')
    Semester.set('')
    USN.set('')
    Branch.set('')
    Feedback.set('')

if __name__=="__main__":
    cred = credentials.Certificate("student-registration-for-165c2-firebase-adminsdk-9u24d-dbcf08f98a.json")
    firebase_admin.initialize_app(cred)

    db = firestore.client()
    
    window = tk.Tk()

    Name=tk.StringVar(window)
    USN=tk.StringVar(window)
    Branch=tk.StringVar(window)
    Semester=tk.StringVar(window)
    Feedback=tk.StringVar(window)

    window.title("Student Feedback Form")
    window.geometry('400x400')
    window.configure(background = "grey")

    a = Label(window ,text = "Name").grid(row = 0,column = 0)
    b = Label(window ,text = "Semester").grid(row = 1,column = 0)
    c = Label(window ,text = "USN").grid(row = 2,column = 0)
    d = Label(window ,text = "Branch").grid(row = 3,column = 0)
    e = Label(window ,text = "Feedback").grid(row =4 ,column = 0) 

    NameE = Entry(window,textvariable=Name).grid(row = 0,column = 1)
    SemesterE = Entry(window,textvariable=Semester).grid(row = 1,column = 1)
    USNE = Entry(window,textvariable=USN).grid(row = 2,column = 1)
    BranchE = Entry(window,textvariable=Branch).grid(row = 3,column = 1)
    FeedbackE =Entry(window,textvariable=Feedback).grid(row=4,column=1)
   
    btn = ttk.Button(window ,text="Submit",command=Submit).grid(row=5,column=0)
    window.mainloop()
    
