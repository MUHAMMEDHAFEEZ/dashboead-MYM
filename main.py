
from pathlib import Path
import tkinter as tk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage ,Label ,messagebox ,Frame
from tkinter import ttk
from docxtpl import DocxTemplate
import datetime
import sqlite3
import time
from PIL import Image, ImageTk
import customtkinter

window = Tk()

window.geometry("1440x1024+0+0")
window.configure(bg = "#F4F7FE")


canvas = Canvas(
    window,
    bg = "#F4F7FE",
    height = 832,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)

Side_Bar_Image = Image.open(r'D:\MYM\dashborad\dashboead-MYM\assets\SideBar.png')
Side_Bar = ImageTk.PhotoImage(Side_Bar_Image)
SideBar_Label = Label(window,background="white",image=Side_Bar).place(
    x=0,
    y=0,
    
)

Logo_Image = Image.open(r'D:\MYM\dashborad\dashboead-MYM\assets\logo.png')
Logo = ImageTk.PhotoImage(Logo_Image)
Logo_Label = Label(window,background="white",image=Logo).place(
    x=74,
    y=49,
    
)

Dashborad_Sidbar_Image = Image.open(r'D:\MYM\dashborad\dashboead-MYM\assets\Dashboard_sidebar.png')
Dashborad_Sidbar = ImageTk.PhotoImage(Dashborad_Sidbar_Image)
Dashborad_Sidbar_Label = Label(window,background="white",image=Dashborad_Sidbar).place(
    x=33,
    y=168,
    
)
#bgImage = ImageTk.PhotoImage(Image.open(r"D:\MYM\dashborad\dashboead-MYM\assets\Dashboard_sidebar.png"))
image = customtkinter.CTkImage(Image.open(r"D:\MYM\dashborad\dashboead-MYM\assets\Dashboard_sidebar.png"))

Dashborad_Sidbar = customtkinter.CTkButton(master=window,
                                #  width=253,
                                #  height=36,
                                 fg_color=("#FFFFFF","#FFFFFF"),
                                 image=image,
                                 #border_width=0,
                                 #corner_radius=20,
                                 text="",
                                 command=lambda: print("dashnboard"))
Dashborad_Sidbar.place(x=850,y=510)
window.mainloop()