import tkinter
from tkinter import messagebox
from tkinter import ttk
import __dbconn__ as db

def inputs():
    fname = fname_entry.get()
    mname = mname_entry.get()
    lname = lname_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    e_password = e_password_entry.get()

    db.Login(fname , mname , lname ,email, phone , e_password)    


win = tkinter.Tk()
win.title("Category and Subcategory by M. Shariq Shafiq")
win.configure(bg='Black')
win.geometry("920x550")

frame = tkinter.Frame(win , bg='Black')
frame.pack(fill='both')

#Heading
category_info = tkinter.LabelFrame(frame , text="Login Form to See BSIT Data Site" , font=("Courier 20 bold"))
category_info.configure(bg='Black' , fg='white')
category_info.grid(row=0 ,column=0 )

#Labels Headings 
fname_label = tkinter.Label(category_info, text="Enter First Name : " , font=("Courier 15 bold"))
fname_label.configure(bg='Black' , fg='white')
fname_label.grid(row=0 , column=0)

mname_label = tkinter.Label(category_info , text="Enter Middle Name : " , font=("Courier 17 bold"))
mname_label.configure(bg='Black' , fg='white')
mname_label.grid(row=0 , column=1)
    
lname_label = tkinter.Label(category_info , text="Enter Last Name : " , font=("Courier 17 bold"))
lname_label.configure(bg='Black' , fg='white')
lname_label.grid(row=0 , column=2)
    
email_label = tkinter.Label(category_info , text="Enter Email Address : " , font=("Courier 17 bold"))
email_label.configure(bg='Black' , fg='white')
email_label.grid(row=3 , column=0)
    
email_label = tkinter.Label(category_info , text="Enter Email Address : " , font=("Courier 17 bold"))
email_label.configure(bg='Black' , fg='white')
email_label.grid(row=3 , column=0)

    
phone_label = tkinter.Label(category_info , text="Enter Phone Number : " , font=("Courier 17 bold"))
phone_label.configure(bg='Black' , fg='white')
phone_label.grid(row=4 , column=0)
    
phone_label = tkinter.Label(category_info , text="Enter Phone Number : " , font=("Courier 17 bold"))
phone_label.configure(bg='Black' , fg='white')
phone_label.grid(row=4 , column=0)
    
e_password_label = tkinter.Label(category_info , text="Enter Password : " , font=("Courier 17 bold"))
e_password_label.configure(bg='Black' , fg='white')
e_password_label.grid(row=5 , column=0)

    #Entry Bars
fname_entry = tkinter.Entry(category_info)
mname_entry = tkinter.Entry(category_info)
lname_entry = tkinter.Entry(category_info)
email_entry = tkinter.Entry(category_info)
phone_entry = tkinter.Entry(category_info)
e_password_entry = tkinter.Entry(category_info)
fname_entry.grid(row=1 , column=0)
fname_entry.configure(bg='white' , fg='black')
mname_entry.grid(row=1 , column=1)
mname_entry.configure(bg='white' , fg='black')
lname_entry.grid(row=1 , column=2)

lname_entry.configure(bg='white' , fg='black')
email_entry.grid(row=3 , column=1)
email_entry.configure(bg='white' , fg='black')
phone_entry.grid(row=4 , column=1)
phone_entry.configure(bg='white' , fg='black')
e_password_entry.grid(row=5 , column=1)
e_password_entry.configure(bg='white' , fg='black')
    
button1 = tkinter.Button(frame , text="Click to Login" , command=inputs)
button1.configure(bg='green' , fg='aqua')
button1.grid(row=7 , column=0 , sticky="news" , padx=5 , pady=5)

win.mainloop()

db.showData()
