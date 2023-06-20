
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

window.geometry("1280x832+350+100")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 832,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)

window.mainloop()