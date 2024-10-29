import customtkinter
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
from diabetesPredict import diabeties_test

def getInput():
    val1 = entry_of_pregnency.get()
    val2 = entry_of_glucose.get()
    val3 = entry_of_bp.get()
    val4 = entry_of_skin.get()
    val5 = entry_of_insulin.get()
    val6 = entry_of_bmi.get()
    val7 = entry_of_dbt.get()
    val8 = entry_of_age.get()

    if(val1 == ''or val2 == ''or val3 == ''or val4 == ''or val5 == ''or val6 == ''or val7 == ''or val8 == ''):
       messagebox.showerror("Error", "Please fill all Entries")
       return

    if(val1.isalpha() == True):
       messagebox.showerror("Error", "No. of pregnency must be Number")
       return
    
    if(val2.isalpha() == True):
       messagebox.showerror("Error", "Glucose must be Number")
       return
    if(val3.isalpha() == True):
       messagebox.showerror("Error", "Blood Pressure must be Number")
       return
    
    if(val4.isalpha() == True):
       messagebox.showerror("Error", "Skin Thickness must be Number")
       return
    
    if(val5.isalpha() == True):
       messagebox.showerror("Error", "Insulin must be Number")
       return
    
    if(val6.isalpha() == True):
       messagebox.showerror("Error", "BMI must be Number")
       return
    
    if(val7.isalpha() == True):
       messagebox.showerror("Error", "Pedigree Function must be Number")
       return
    
    if(val8.isalpha() == True):
       messagebox.showerror("Error", "Age must be Number")
       return
    
    list = []
    list.append(val1)
    list.append(val2)
    list.append(val3)
    list.append(val4)
    list.append(val5)
    list.append(val6)
    list.append(val7)
    list.append(val8)
    value = diabeties_test(list)

    if(value == 0):
       messagebox.showinfo("Success","You do not have Diabetes")
    else:
       messagebox.showerror("Success","You may have diabetes")

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")

app = customtkinter.CTk()
app.geometry("1366x550+0+0")
app.resizable(FALSE,FALSE)

image1=customtkinter.CTkImage(Image.open("img/img2.jpg"),size = (1366,550))
label1=customtkinter.CTkLabel(master=app,image=image1,text="")
label1.pack()

text = customtkinter.CTkLabel(app, text="Diabetes Prediction",font=('Century Gothic',25),bg_color="light blue",text_color="red")
text.place(relx=0.48, rely=0.08)

entry_of_pregnency=customtkinter.CTkEntry(master=app, height=35 ,width=320, placeholder_text='No. of Pregencies',font=('Century Gothic',25),bg_color="light blue",fg_color="light blue",placeholder_text_color="blue",text_color="blue")
entry_of_pregnency.place(x=350, y=110)

entry_of_glucose=customtkinter.CTkEntry(master=app, height=35 ,width=320, placeholder_text='Glucose',font=('Century Gothic',25),bg_color="light blue",fg_color="light blue",placeholder_text_color="blue",text_color="blue")
entry_of_glucose.place(x=850, y=110)

entry_of_bp=customtkinter.CTkEntry(master=app, height=35 ,width=320, placeholder_text='Blood Pressure',font=('Century Gothic',25),bg_color="light blue",fg_color="light blue",placeholder_text_color="blue",text_color="blue")
entry_of_bp.place(x=350, y=190)

entry_of_skin=customtkinter.CTkEntry(master=app, height=35 ,width=320, placeholder_text='Skin Thickness',font=('Century Gothic',25),bg_color="light blue",fg_color="light blue",placeholder_text_color="blue",text_color="blue")
entry_of_skin.place(x=850, y=190)

entry_of_insulin=customtkinter.CTkEntry(master=app, height=35 ,width=320, placeholder_text='Insulin',font=('Century Gothic',25),bg_color="light blue",fg_color="light blue",placeholder_text_color="blue",text_color="blue")
entry_of_insulin.place(x=350, y=270)

entry_of_bmi=customtkinter.CTkEntry(master=app, height=35 ,width=320, placeholder_text='BMI',font=('Century Gothic',25),bg_color="light blue",fg_color="light blue",placeholder_text_color="blue",text_color="blue")
entry_of_bmi.place(x=850, y=270)

entry_of_dbt=customtkinter.CTkEntry(master=app, height=35 ,width=320, placeholder_text='Pedigree Function',font=('Century Gothic',25),bg_color="light blue",fg_color="light blue",placeholder_text_color="blue",text_color="blue")
entry_of_dbt.place(x=350, y=350)

entry_of_age=customtkinter.CTkEntry(master=app, height=35 ,width=320, placeholder_text='Age',font=('Century Gothic',25),bg_color="light blue",fg_color="light blue",placeholder_text_color="blue",text_color="blue")
entry_of_age.place(x=850, y=350)


btn3 = customtkinter.CTkButton(
    master=label1,
    text="Check Now",
    width=150,
    height=50,
    fg_color="navy blue",  # Makes the button background transparent
    bg_color="navy blue",
    text_color="red",   # Text color
    command=getInput,     # Function to call on click
    hover_color="blue",
    
    font=('Century Gothic',25)
)

btn3.place(relx=0.55, rely=0.85, anchor='center')

app.mainloop()