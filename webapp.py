pip install tkinter
import tkinter
from tkinter import ttk
from tkinter import messagebox
#from tkinter import messagebox
import os
#import openpyxl
window = tkinter.Tk()
window.title("Registration Form")

frame = tkinter.Frame(window)
frame.pack()

#USer info
user_info_frame = tkinter.LabelFrame(frame, text="User information")
user_info_frame.grid(row=0, column=0)


first_name_label = tkinter.Label(user_info_frame, text="First Name")
first_name_label.grid(row=0, column=0)

Last_name_label = tkinter.Label(user_info_frame, text="Last Name")
Last_name_label.grid(row=0, column=1)

frist_name_entry = tkinter.Entry(user_info_frame)
Last_name_entry = tkinter.Entry(user_info_frame)
frist_name_entry.grid(row=1, column=0)
Last_name_entry.grid(row=1, column=1)
title_label = tkinter.Label(user_info_frame,text="Title")
title_Combobox = ttk.Combobox(user_info_frame,values =["","Mr.","Ms.","Dr"])
title_label.grid(row=0,column=2)
title_Combobox.grid(row=1,column=2)


Age_label = tkinter.Label(user_info_frame, text="Age")
Age_label.grid(row=2, column=0)
Age_Spinbox = tkinter.Spinbox(user_info_frame, from_= 18, to=110)
Age_Spinbox.grid(row=3, column=0)

Nationality_label = tkinter.Label(user_info_frame,text="Nationality")
Nationality_lbel_Combobox = ttk.Combobox(user_info_frame,values =["Hyderabd","Banglore","Siddipet"])
Nationality_label.grid(row=2, column=1)
Nationality_lbel_Combobox.grid(row=3, column=1)
for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)
courses_frame = tkinter.LabelFrame(frame)
courses_frame.grid(row=1, column=0, sticky="news", padx=10, pady=5)

registered_label = tkinter.LabelFrame(courses_frame, text="Registration Status")
registered_check = tkinter.Checkbutton(courses_frame,text="Currently Registered")
registered_label.grid(row=0, column=0)
registered_check.grid(row=1, column=0)

Completed_label_Status = tkinter.Label(courses_frame,text="Registered &Completed")
Completed_label_Status = tkinter.Spinbox(courses_frame, from_= 0, to=110)
Completed_label_Status_Combobox = ttk.Combobox(courses_frame,values =["Registered & complete"])
InComplete_label_Status_Combobox = ttk.Combobox(courses_frame,values =["Registered & Incomplete"])
Completed_label_Status.grid(row=1, column=1)
Completed_label_Status_Combobox.grid(row=3, column=0)
InComplete_label_Status_Combobox.grid(row=3, column=0)
InComplete_label_Status_Combobox.grid(row=3, column=1)
for widget in courses_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Accept terms
terms_frame = tkinter.LabelFrame(frame, text="Terms & Conditions")
terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

accept_var = tkinter.StringVar(value="Not Accepted")
terms_check = tkinter.Checkbutton(terms_frame, text="I accept the terms and conditions.",
                                  variable=accept_var, onvalue="Accepted", offvalue="Not Accepted")
terms_check.grid(row=0, column=0)

# Button
button = tkinter.Button(frame, text="Enter data", command="enter_data")
button.grid(row=3, column=0, sticky="news", padx=20, pady=10)

window.mainloop()
