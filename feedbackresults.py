from asyncio.windows_events import NULL
import tkinter as tk
import os 
from tkinter import *
from tkinter import ttk
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import csv
    
if __name__=="__main__":
    cred = credentials.Certificate("student-registration-for-165c2-firebase-adminsdk-9u24d-dbcf08f98a.json")
    firebase_admin.initialize_app(cred)
    db = firestore.client()
    college_data=db.collection('StudentFeedback').get() 
    #Fields
    Name=''
    Semester=''
    USN=''
    Branch=''
    Feedback=''
    #CSV File Open
    F=open('Feedback.csv','w')
    #Create CSV File object
    writer=csv.writer(F)
    #Top row fields
    fields=['Name','Semester','USN','Branch','Feedback']
    rows=[]
    for each_student_feedback in college_data:
        Name=each_student_feedback.get('Name')
        Semester=each_student_feedback.get('Semester')
        USN=each_student_feedback.get('USN')
        Branch=each_student_feedback.get('Branch')
        Feedback=each_student_feedback.get('Feedback')
        rows.append([Name,Semester,USN,Branch,Feedback])
        
    print(rows)
    writer.writerow(fields)
    writer.writerows(rows)
    F.close()

    
