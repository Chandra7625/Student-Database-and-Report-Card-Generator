#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
df=pd.read_csv("D:\VIT Chennai\Python\Python Maam Project\Student Database.csv")
df


# In[1]:


import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import pandas as pd

url="D:\VIT Chennai\Python\Python Maam Project\Student Database.csv"

def submit():
    df=pd.read_csv(url)
    enroll=enroll_entry.get()
    name=name_entry.get()
    d = dict(zip(df['Enrollment Number'], df['Name']))
    def check(enrollment,name):
        df=pd.read_csv(url)
        enrollment_present = df['Enrollment Number'].eq(enroll).any()
        name_present = df['Name'].eq(name).any()
        if not enrollment_present and not name_present:
            print(f"Both Enrollment Number {enroll} and Name {name} don't exist in the student database.")
            messagebox.showerror(title="ERROR!",message="Enrollment number and name doesn\'t exist",icon='error')
        elif not enrollment_present:
            print(f"Enrollment Number {enroll} doesn't exist in the student database.")
            messagebox.showerror(title="ERROR!",message="Enrollment number doesn\'t exist",icon='error')
        elif not name_present:
            print(f"Name {name} doesn't exist in the student database.")
            messagebox.showerror(title="ERROR!",message="Name doesn\'t exist",icon='error')
        else:
            def present(enrollment,name):
                is_present = (df['Enrollment Number'] == enroll) & (df['Name'] == name)
                return is_present.any()
            result = present(enroll, name)
            if result:
                details = df[df['Enrollment Number'] == enroll]
                print(f"{enroll} and {name} are present in the student database.")
                print(f"Details for Enrollment Number {enroll}:\n{details}")
            else:
                print(f"{enroll} and {name} exist independently but they do not correspond to each other.")
                messagebox.showerror(title="ERROR!",message="Mismatch",icon='error')
    check(enroll,name)  

# Creating a window
window=tk.Tk()
window.geometry("1000x700")
window.title("School Database")

# Creating an image
image = Image.open("D:\VIT Chennai\Project\sch.png")
resize_image = image.resize((200, 200))
img = ImageTk.PhotoImage(resize_image)

# Creating a label widget
School=Label(window,text="School",font=("Arial",40,"bold"),fg='black',bg="#5DF1A7",image=img,compound='bottom',padx=100,pady=20)
School.pack()
window.config(background="#5DF1A7")

# Creating enrollment number and name label widget
Enroll_Id=Label(window, text="Enrollment Number:",font=("Arial",20,"bold"))
Name=Label(window,text="Name:",font=("Arial",20,"bold"))
Enroll_Id.pack()
Enroll_Id.place(x=200,y=400)
Name.pack()
Name.place(x=383,y=450)

# Creating enrollment number and name entry widget
enroll_entry=Entry(window,font=("Arial",20))
enroll_entry.pack()
enroll_entry.place(x=500,y=400)
name_entry=Entry(window,font=("Arial",20))
name_entry.pack()
name_entry.place(x=500,y=450)

# Creating a submit button
submit_button=Button(window,text="Submit",command=submit)
submit_button.pack()
submit_button.place(x=465,y=550)

# Displays our window
window.mainloop()


# In[6]:


import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import pandas as pd


url="D:\VIT Chennai\Python\Python Maam Project\Student Database.csv"

def submit():
    df=pd.read_csv(url)
    enroll=enroll_entry.get()
    name=name_entry.get()
    d = dict(zip(df['Enrollment Number'], df['Name']))
    def check(enrollment,name):
        df=pd.read_csv(url)
        enrollment_present = df['Enrollment Number'].eq(enroll).any()
        name_present = df['Name'].eq(name).any()
        """def marksheet():
            print(f"The report card of {name}, enrollment number {enroll} is:")
            print(f"{details}")"""
        if not enrollment_present and not name_present:
            print(f"Both Enrollment Number {enroll} and Name {name} don't exist in the student database.")
            messagebox.showerror(title="ERROR!",message="Enrollment number and name doesn\'t exist",icon='error')
        elif not enrollment_present:
            print(f"Enrollment Number {enroll} doesn't exist in the student database.")
            messagebox.showerror(title="ERROR!",message="Enrollment number doesn\'t exist",icon='error')
        elif not name_present:
            print(f"Name {name} doesn't exist in the student database.")
            messagebox.showerror(title="ERROR!",message="Name doesn\'t exist",icon='error')
        else:
            def present(enrollment,name):
                is_present = (df['Enrollment Number'] == enroll) & (df['Name'] == name)
                return is_present.any()
            result = present(enroll, name)
            if result:
                details = df[df['Enrollment Number'] == enroll]
                dictionary=dict(details)
                print(f"{enroll} and {name} are present in the student database.")
                print(f"Report card of name {name}, Enrollment Number {enroll}:\n{details}")
                messagebox.showinfo(title="Report card",message=(f"{details}"))
                detail=tk.Tk()
                detail.geometry("1000x700")
                detail.title("Report card of the student")
                for key, value in dictionary.items():
                    label = Label(detail, text=f"{key}: {value}",font=("Arial",10,"bold"))
                    label.pack(pady=5)

            else:
                print(f"{enroll} and {name} exist independently but they do not correspond to each other.")
                messagebox.showerror(title="ERROR!",message="Mismatch",icon='error')
    check(enroll,name)  


# Creating a window
window=tk.Tk()
window.geometry("1000x700")
window.title("School Database")

# Creating an image
image = Image.open("D:\VIT Chennai\Project\sch.png")
resize_image = image.resize((200, 200))
img = ImageTk.PhotoImage(resize_image)

# Creating a label widget
School=Label(window,text="School",font=("Arial",40,"bold"),fg='black',bg="#5DF1A7",image=img,compound='bottom',padx=100,pady=20)
School.pack()
window.config(background="#5DF1A7")

# Creating enrollment number and name label widget
Enroll_Id=Label(window, text="Enrollment Number:",font=("Arial",20,"bold"))
Name=Label(window,text="Name:",font=("Arial",20,"bold"))
Enroll_Id.pack()
Enroll_Id.place(x=200,y=400)
Name.pack()
Name.place(x=383,y=450)

# Creating enrollment number and name entry widget
enroll_entry=Entry(window,font=("Arial",20))
enroll_entry.pack()
enroll_entry.place(x=500,y=400)
name_entry=Entry(window,font=("Arial",20))
name_entry.pack()
name_entry.place(x=500,y=450)

# Creating a submit button
submit_button=Button(window,text="Submit",command=submit)
submit_button.pack()
submit_button.place(x=465,y=550)

# Displays our window
window.mainloop()


# In[5]:


import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import pandas as pd


url="D:\VIT Chennai\Python\Python Maam Project\Student Database.csv"

def submit():
    df=pd.read_csv(url)
    enroll=enroll_entry.get()
    name=name_entry.get()
    d = dict(zip(df['Enrollment Number'], df['Name']))
    def check(enrollment,name):
        df=pd.read_csv(url)
        enrollment_present = df['Enrollment Number'].eq(enroll).any()
        name_present = df['Name'].eq(name).any()
        if not enrollment_present and not name_present:
            print(f"Both Enrollment Number {enroll} and Name {name} don't exist in the student database.")
            messagebox.showerror(title="ERROR!",message="Enrollment number and name doesn\'t exist",icon='error')
        elif not enrollment_present:
            print(f"Enrollment Number {enroll} doesn't exist in the student database.")
            messagebox.showerror(title="ERROR!",message="Enrollment number doesn\'t exist",icon='error')
        elif not name_present:
            print(f"Name {name} doesn't exist in the student database.")
            messagebox.showerror(title="ERROR!",message="Name doesn\'t exist",icon='error')
        else:
            def present(enrollment,name):
                is_present = (df['Enrollment Number'] == enroll) & (df['Name'] == name)
                return is_present.any()
            result = present(enroll, name)
            if result:
                details = df[df['Enrollment Number'] == enroll]
                dictionary=dict(details)
                print(f"{enroll} and {name} are present in the student database.")
                print(f"Details for Enrollment Number {enroll}:\n{details}")
                messagebox.showinfo(title="Report card",message=(f"{details}"))
                detail=tk.Tk()
                detail.geometry("1000x700")
                detail.title("Details of the student")
                for key, value in dictionary.items():
                    label = Label(detail, text=f"{key}: {value}",font=("Arial",10,"bold"))
                    label.pack(pady=5)

            else:
                print(f"{enroll} and {name} exist independently but they do not correspond to each other.")
                messagebox.showerror(title="ERROR!",message="Mismatch",icon='error')
    check(enroll,name)  


# Creating a window
window=tk.Tk()
window.geometry("1000x700")
window.title("School Database")

# Creating an image
image = Image.open("D:\VIT Chennai\Project\sch.png")
resize_image = image.resize((200, 200))
img = ImageTk.PhotoImage(resize_image)

# Creating a label widget
School=Label(window,text="School",font=("Arial",40,"bold"),fg='black',bg="#5DF1A7",image=img,compound='bottom',padx=100,pady=20)
School.pack()
window.config(background="#5DF1A7")

# Creating enrollment number and name label widget
Enroll_Id=Label(window, text="Enrollment Number:",font=("Arial",20,"bold"))
Name=Label(window,text="Name:",font=("Arial",20,"bold"))
Enroll_Id.pack()
Enroll_Id.place(x=200,y=400)
Name.pack()
Name.place(x=383,y=450)

# Creating enrollment number and name entry widget
enroll_entry=Entry(window,font=("Arial",20))
enroll_entry.pack()
enroll_entry.place(x=500,y=400)
name_entry=Entry(window,font=("Arial",20))
name_entry.pack()
name_entry.place(x=500,y=450)

# Creating a submit button
submit_button=Button(window,text="Submit",command=submit)
submit_button.pack()
submit_button.place(x=465,y=550)

# Displays our window
window.mainloop()


# In[ ]:




