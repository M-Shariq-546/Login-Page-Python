import sqlite3 as s3
import tkinter
from tkinter import messagebox
from tkinter import ttk

#This is our main Function for all happening
def Login(fname , mname , lname , email, phone , e_password):
    
    con = s3.connect('Login.db' , timeout=10)
    cur = con.cursor()  

   # fname = fname_entry.get()
   #mname = mname_entry.get()
   # lname = lname_entry.get()
   # email = email_entry.get()
   # phone = phone_entry.get()
   # e_password = e_password_entry.get()
    
    table = '''CREATE TABLE IF NOT EXISTS logins
        (id integer primary key AUTOINCREMENT  ,
        fname varchar(50) , 
        mname varchar(50) ,
        lname varchar(50),
        email text,
        phone number(11) , 
        e_password password
        );'''

    sql = '''insert into logins (fname , mname , lname , email ,phone, e_password) values(?,?,?,?,?,?)'''

    que1 = cur.execute(table)


    data = [(fname , mname , lname , email , phone , e_password)]

    que2 = cur.executemany(sql ,data)

    con.commit()

    cur.close()
    con.close()

def showData():
    con = s3.connect('Login.db' , timeout=10)
    cur = con.cursor()
    que3 = '''select * from logins'''


    que4 = cur.execute(que3)

    result = cur.fetchall()

    print(result)


    con.commit()

    cur.close()
    con.close()