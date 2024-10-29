import customtkinter
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
from heart_attack import heartAttack

def getInput():
    val1 = entry_of_age.get()
    val2 = entry_of_gender.get()
    val3 = entry_of_impulse.get()
    val4 = entry_of_ph.get()
    val5 = entry_of_pl.get()
    val6 = entry_of_glucose.get()
    val7 = entry_of_kcm.get()
    val8 = entry_of_troponin.get()

    if(val1 == ''or val2 == ''or val3 == ''or val4 == ''or val5 == ''or val6 == ''or val7 == ''or val8 == ''):
       messagebox.showerror("Error", "Please fill all Entries")
       return
    
    if(val1.isalpha() == True):
       messagebox.showerror("Error", "Age must be Number")
       return

    if(val2 == 'M' or val2 == 'F' or val2 == "m" or val2 == 'f'):
       if(val2 == 'M' or val2 == 'm'):
          val2 = 1
       else:
          val2 = 0
       
    else:
       messagebox.showerror("Error", "Gender must be M or F")
       return
       
    
    if(val3.isalpha() == True):
       messagebox.showerror("Error", "Impulse must be Number")
       return
    
    
    if(val4.isalpha() == True):
       messagebox.showerror("Error", "Pressure High must be Number")
       return
    
    
    if(val5.isalpha() == True):
       messagebox.showerror("Error", "Pressure Low must be Number")
       return
    
    
    if(val6.isalpha() == True):
       messagebox.showerror("Error", "Glucose must be Number")
       return
    
    
    if(val4.isalpha() == True):
       messagebox.showerror("Error", "KCM must be Number")
       return
    
    
    if(val4.isalpha() == True):
       messagebox.showerror("Error", "Troponin must be Number")
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
    value = heartAttack(list)

    if(value == 0):
       messagebox.showinfo("Success","You do not have Heart Attack Problem")
    else:
       messagebox.showerror("Success","You may have Heart Attack Problem")

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")

app = customtkinter.CTk()
app.geometry("1366x550+0+0")
app.resizable(FALSE,FALSE)

image1=ImageTk.PhotoImage(Image.open("img/img2.jpg"))
label1=customtkinter.CTkLabel(master=app,image=image1,text="")
label1.pack()

text = customtkinter.CTkLabel(app, text="Heart Attack Prediction",font=('Century Gothic',25),bg_color="light blue",text_color="red")
text.place(relx=0.48, rely=0.08)

entry_of_age=customtkinter.CTkEntry(master=app, height=35 ,width=320, placeholder_text='Age',font=('Century Gothic',25),bg_color="light blue",fg_color="light blue",placeholder_text_color="blue",text_color="blue")
entry_of_age.place(x=350, y=110)

entry_of_gender=customtkinter.CTkEntry(master=app, height=35 ,width=320, placeholder_text='Gender : M/F ',font=('Century Gothic',25),bg_color="light blue",fg_color="light blue",placeholder_text_color="blue",text_color="blue")
entry_of_gender.place(x=850, y=110)

entry_of_impulse=customtkinter.CTkEntry(master=app, height=35 ,width=320, placeholder_text='Impulse',font=('Century Gothic',25),bg_color="light blue",fg_color="light blue",placeholder_text_color="blue",text_color="blue")
entry_of_impulse.place(x=350, y=190)

entry_of_ph=customtkinter.CTkEntry(master=app, height=35 ,width=320, placeholder_text='Pressue High',font=('Century Gothic',25),bg_color="light blue",fg_color="light blue",placeholder_text_color="blue",text_color="blue")
entry_of_ph.place(x=850, y=190)

entry_of_pl=customtkinter.CTkEntry(master=app, height=35 ,width=320, placeholder_text='Pressure Low',font=('Century Gothic',25),bg_color="light blue",fg_color="light blue",placeholder_text_color="blue",text_color="blue")
entry_of_pl.place(x=350, y=270)

entry_of_glucose=customtkinter.CTkEntry(master=app, height=35 ,width=320, placeholder_text='Glucose',font=('Century Gothic',25),bg_color="light blue",fg_color="light blue",placeholder_text_color="blue",text_color="blue")
entry_of_glucose.place(x=850, y=270)

entry_of_kcm=customtkinter.CTkEntry(master=app, height=35 ,width=320, placeholder_text='KCM',font=('Century Gothic',25),bg_color="light blue",fg_color="light blue",placeholder_text_color="blue",text_color="blue")
entry_of_kcm.place(x=350, y=350)

entry_of_troponin=customtkinter.CTkEntry(master=app, height=35 ,width=320, placeholder_text='Troponin',font=('Century Gothic',25),bg_color="light blue",fg_color="light blue",placeholder_text_color="blue",text_color="blue")
entry_of_troponin.place(x=850, y=350)


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