
from pathlib import Path
# from tkinter import *
# Explicit imports to satisfy Flake8
import tkinter as tk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage ,Label ,messagebox ,Frame
from tkinter import ttk
from docxtpl import DocxTemplate
import datetime
import sqlite3
import time
from PIL import Image, ImageTk
import customtkinter

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\MYM\dashborad\dashboead-MYM\build\assets\frame0")


qty2=10
qty1=200
qty=200


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1440x1024")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 1024,
    width = 1440,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    720.0,
    512.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    149.0,
    519.0,
    image=image_image_2
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=47.0,
    y=771.0,
    width=253.0,
    height=36.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=47.0,
    y=717.0,
    width=253.0,
    height=36.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=55.0,
    y=897.0,
    width=181.0,
    height=72.0
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    145.0,
    70.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    118.0,
    219.0,
    image=image_image_4
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=39.0,
    y=271.0,
    width=154.0,
    height=42.0648193359375
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
button_5.place(
    x=45.0,
    y=417.0,
    width=152.0,
    height=40.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="flat"
)
button_6.place(
    x=45.0,
    y=489.0,
    width=157.0,
    height=44.0
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_7 clicked"),
    relief="flat"
)
button_7.place(
    x=42.0,
    y=565.0,
    width=126.0,
    height=41.0
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_8 clicked"),
    relief="flat"
)
button_8.place(
    x=40.0,
    y=638.0,
    width=150.0,
    height=41.0
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    1349.0,
    60.0,
    image=image_image_5
)

canvas.create_text(
    1230.0,
    72.0,
    anchor="nw",
    text="Admin",
    fill="#21222D",
    font=("Poppins Regular", 14 * -1)
)

canvas.create_text(
    1230.0,
    48.0,
    anchor="nw",
    text="Admin Name",
    fill="#034488",
    font=("Poppins Medium", 16 * -1)
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    1184.0,
    70.0,
    image=image_image_6
)

button_image_9 = PhotoImage(
    file=relative_to_assets("button_9.png"))
button_9 = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_9 clicked"),
    relief="flat"
)
button_9.place(
    x=1010.0,
    y=46.0,
    width=48.0,
    height=48.0
)

button_image_10 = PhotoImage(
    file=relative_to_assets("button_10.png"))
button_10 = Button(
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_10 clicked"),
    relief="flat"
)
button_10.place(
    x=1082.0,
    y=46.0,
    width=48.0,
    height=48.0
)

button_image_11 = PhotoImage(
    file=relative_to_assets("button_11.png"))
button_11 = Button(
    image=button_image_11,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_11 clicked"),
    relief="flat"
)
button_11.place(
    x=39.0,
    y=345.0,
    width=163.0,
    height=40.0
)


Dashboard_Frame = Frame( window,bg='#F4F7FE')

# Create a photoimage object of the image in the path
Dashboard_Frame.place(x=295,y=112,width=1150,height=912)

dashboarsd_back_Image = Image.open(r'D:\MYM\dashborad\dashboead-MYM\assets\dashboard_frame.png')
dashboarsd_back = ImageTk.PhotoImage(dashboarsd_back_Image)


LOGOIN = Label(Dashboard_Frame,image=dashboarsd_back).place(
     x=0,
     y=0,
    
 )

#total empl
total_emp_Image = Image.open(r'D:\MYM\dashborad\dashboead-MYM\assets\total_Empl_bg.png')
total_emp_bg= ImageTk.PhotoImage(total_emp_Image)
total_emp = Label(Dashboard_Frame,background="#F4F7FE",image=total_emp_bg).place(
    x=52,
    y=42,
    
)

total_emp_Image = Image.open(r'D:\MYM\dashborad\dashboead-MYM\assets\total_Empl_bg.png')
total_emp_bg= ImageTk.PhotoImage(total_emp_Image)
total_emp = Label(Dashboard_Frame,background="#F4F7FE",image=total_emp_bg).place(
    x=52,
    y=42,
    
)

Total_Emp_Icon = Image.open(r'D:\MYM\dashborad\dashboead-MYM\assets\total_empl_icon.png')
Total_Emp= ImageTk.PhotoImage(Total_Emp_Icon)
TotalEmp = Label(Dashboard_Frame,background="white",image=Total_Emp).place(
    x=76,
    y=66,
    
)

emp_NUM= Label(Dashboard_Frame,text = qty ,bg='white',font="Poppins 24")
emp_NUM.place(
    x=76,
    y=160,
    ) 

Totalemp_NUM= Label(Dashboard_Frame,text = qty1 ,bg='white',font="Poppins 18")
Totalemp_NUM.place(
    x=140,
    y=170,
    ) 

total_emp_Image = Image.open(r'D:\MYM\dashborad\dashboead-MYM\assets\total_Empl_bg.png')
total_emp_bg= ImageTk.PhotoImage(total_emp_Image)
total_emp = Label(Dashboard_Frame,background="#F4F7FE",image=total_emp_bg).place(
    x=52,
    y=42,
    
)

total_emp_Image = Image.open(r'D:\MYM\dashborad\dashboead-MYM\assets\total_Empl_bg.png')
total_emp_bg= ImageTk.PhotoImage(total_emp_Image)
total_emp = Label(Dashboard_Frame,background="#F4F7FE",image=total_emp_bg).place(
    x=52,
    y=42,
    
)

Total_Emp_Icon = Image.open(r'D:\MYM\dashborad\dashboead-MYM\assets\total_empl_icon.png')
Total_Emp= ImageTk.PhotoImage(Total_Emp_Icon)
TotalEmp = Label(Dashboard_Frame,background="white",image=Total_Emp).place(
    x=76,
    y=66,
    
)

emp_NUM= Label(Dashboard_Frame,text = qty ,bg='white',font="Poppins 24")
emp_NUM.place(
    x=76,
    y=160,
    ) 


Totalemp_NUM= Label(Dashboard_Frame,text = qty1 ,bg='white',font="Poppins 18")
Totalemp_NUM.place(
    x=150,
    y=170,
    ) 

back_slash= Label(Dashboard_Frame,text = "/" ,bg='white',font="Poppins 18")
back_slash.place(
    x=140,
    y=169,
    ) 


# on leave 

Onleave_Image = Image.open(r'D:\MYM\dashborad\dashboead-MYM\assets\Onleave_bg.png')
Onleave_bg= ImageTk.PhotoImage(Onleave_Image)
Onleave = Label(Dashboard_Frame,background="#F4F7FE",image=Onleave_bg).place(
    x=321,
    y=43,
    
)

Onleave_Icon = Image.open(r'D:\MYM\dashborad\dashboead-MYM\assets\Onleave_icon.png')
Onleave_bg_Icon= ImageTk.PhotoImage(Onleave_Icon)
Onleave_Ico = Label(Dashboard_Frame,background="white",image=Onleave_bg_Icon).place(
    x=345,
    y=67,
    
)

onleave_NUM= Label(Dashboard_Frame,text = qty2 ,bg='white',font="Poppins 24")
onleave_NUM.place(
    x=345,
    y=161,
    ) 

Totaonleave_NUM= Label(Dashboard_Frame,text = qty1 ,bg='white',font="Poppins 18")
Totaonleave_NUM.place(
    x=400,
    y=169,
    ) 

back_slash1= Label(Dashboard_Frame,text = "/" ,bg='white',font="Poppins 18")
back_slash1.place(
    x=390,
    y=169,
    ) 

# traners 
traners_Image = Image.open(r'D:\MYM\dashborad\dashboead-MYM\assets\trainers.png')
traners_bg= ImageTk.PhotoImage(traners_Image)
traners = Label(Dashboard_Frame,background="#F4F7FE",image=traners_bg).place(
    x=596,
    y=44,
    
)

traner_Icon = Image.open(r'D:\MYM\dashborad\dashboead-MYM\assets\trainers_icon.png')
traner_bg_Icon= ImageTk.PhotoImage(traner_Icon)
traner_Ico = Label(Dashboard_Frame,background="white",image=traner_bg_Icon).place(
    x=620,
    y=68,
    
)

traner_NUM= Label(Dashboard_Frame,text = qty2 ,bg='white',font="Poppins 24")
traner_NUM.place(
    x=620,
    y=161,
    )

traner_NUM= Label(Dashboard_Frame,text = qty1 ,bg='white',font="Poppins 18")
traner_NUM.place(
    x=680,
    y=169,
    ) 

back_slash2= Label(Dashboard_Frame,text = "/" ,bg='white',font="Poppins 18")
back_slash2.place(
    x=670,
    y=169,
    ) 


# projects 



projects_Image = Image.open(r'D:\MYM\dashborad\dashboead-MYM\assets\projects.png')
projects_bg= ImageTk.PhotoImage(projects_Image)
projects = Label(Dashboard_Frame,background="#F4F7FE",image=projects_bg).place(
    x=52,
    y=592,
    
)

ongoing_Icon = Image.open(r'D:\MYM\dashborad\dashboead-MYM\assets\ongoingtasks_Icon.png')
ongoing_bg_Icon= ImageTk.PhotoImage(ongoing_Icon)
ongoing_Ico = Label(Dashboard_Frame,background="white",image=ongoing_bg_Icon).place(
    x=402,
    y=662,
    
)

upcoming_Icon = Image.open(r'D:\MYM\dashborad\dashboead-MYM\assets\upcomingtasks_Icon.png')
upcoming_bg_Icon= ImageTk.PhotoImage(upcoming_Icon)
upcoming_Ico = Label(Dashboard_Frame,background="white",image=upcoming_bg_Icon).place(
    x=641,
    y=662,
    
)

completedtaskes_Icon = Image.open(r'D:\MYM\dashborad\dashboead-MYM\assets\completedtasks_Icon.png')
completedtaskes_bg_Icon= ImageTk.PhotoImage(completedtaskes_Icon)
completedtaskes = Label(Dashboard_Frame,background="white",image=completedtaskes_bg_Icon).place(
    x=895,
    y=662,
    
)

# traner_NUM= Label(Dashboard_Frame,text = qty2 ,bg='white',font="Poppins 24")
# traner_NUM.place(
#     x=620,
#     y=161,
#     )

# traner_NUM= Label(Dashboard_Frame,text = qty1 ,bg='white',font="Poppins 18")
# traner_NUM.place(
#     x=680,
#     y=169,
#     ) 

# back_slash2= Label(Dashboard_Frame,text = "/" ,bg='white',font="Poppins 18")
# back_slash2.place(
#     x=670,
#     y=169,
#     ) 

window.resizable(False, False)
window.mainloop()
