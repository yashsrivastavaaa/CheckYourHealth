import tkinter as tk
from tkinter import *
import customtkinter
from PIL import ImageTk,Image
import os
def diabetes1():
    app.destroy()
    os.system('pythonw diabetes/diabetes_gui.pyw')
def heart():
    app.destroy()
    os.system('pythonw heart/heartattack_gui.pyw')

def lungs():
    app.destroy()
    os.system('pythonw lungs/lungcancer_gui.pyw')
    
def breast():
    app.destroy()
    os.system('pythonw breast_cancer/breast_cancer.pyw')
        
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")

app = customtkinter.CTk()
app.geometry("1366x550+0+0")
app.title("CheckYourHealth")
app.resizable(FALSE,FALSE)

image1=ImageTk.PhotoImage(Image.open("img/img2.jpg"))
label1=customtkinter.CTkLabel(master=app,image=image1,text="")
label1.pack()
btnimg1 = customtkinter.CTkImage(Image.open("img/dbt.png"), size=(100, 100))
btn1 = customtkinter.CTkButton(
    master=label1,
    text="   Diabetes",
    width=350,
    height=200,
    fg_color="navy blue",  # Makes the button background transparent
    bg_color="navy blue",
    text_color="red",   # Text color
    command=lambda : diabetes1(),     # Function to call on click
    hover_color="navy blue",
    image = btnimg1,
    
    font=('Century Gothic',25)
)

btn1.place(relx=0.40, rely=0.25, anchor='center')

btnimg2 = customtkinter.CTkImage(Image.open("img/lungs.png"), size=(100, 100))
btn2 = customtkinter.CTkButton(
    master=label1,
    text="   Lungs Cancer",
    width=350,
    height=200,
    fg_color="navy blue",  # Makes the button background transparent
    bg_color="navy blue",
    text_color="red",   # Text color
    command=lambda : lungs(),     # Function to call on click
    hover_color="navy blue",
    image = btnimg2,
    
    font=('Century Gothic',25)
)

btn2.place(relx=0.80, rely=0.25, anchor='center')


btnimg3 = customtkinter.CTkImage(Image.open("img/breastcancer.png"), size=(100, 100))
btn3 = customtkinter.CTkButton(
    master=label1,
    text="   Breast Cancer",
    width=350,
    height=200,
    fg_color="navy blue",  # Makes the button background transparent
    bg_color="navy blue",
    text_color="red",   # Text color
    command=lambda:breast(),     # Function to call on click
    hover_color="navy blue",
    image = btnimg3,
    
    font=('Century Gothic',25)
)

btn3.place(relx=0.40, rely=0.7, anchor='center')

btnimg2 = customtkinter.CTkImage(Image.open("img/heart.png"), size=(100, 100))
btn2 = customtkinter.CTkButton(
    master=label1,
    text="   Heart Attack",
    width=350,
    height=200,
    fg_color="navy blue",  # Makes the button background transparent
    bg_color="navy blue",
    text_color="red",   # Text color
    command=lambda:heart(),     # Function to call on click
    hover_color="navy blue",
    image = btnimg2,
    
    font=('Century Gothic',25)
)

btn2.place(relx=0.80, rely=0.7, anchor='center')

app.mainloop()
