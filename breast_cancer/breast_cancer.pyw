import customtkinter
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
from cancer import b_cancer

def getInput():
    val1 = entry_1.get()
    val2 = entry_2.get()
    val3 = (entry_3.get())
    val4 = entry_4.get()
    val5 = entry_5.get()
    val6 = entry_6.get()
    val7 = entry_7.get()
    val8 = entry_8.get()
    val9 = entry_9.get()
    val10 = entry_10.get()

    if(val1 == ''or val2 == ''or val3 == ''or val4 == ''or val5 == ''or val6 == ''or val7 == ''or val8 == '' or val9 == '' or val10 ==''):
       messagebox.showerror("Error", "Please fill all Entries")
       return
    
    if(val1.isalpha() == True):
       messagebox.showerror("Error", "Texture Mean must be Number")
       return
    if(val2.isalpha() == True):
       messagebox.showerror("Error", "Area Mean must be Number")
       return
    if(val3.isalpha() == True):
       messagebox.showerror("Error", "Concavity Mean must be Number")
       return
    if(val4.isalpha() == True):
       messagebox.showerror("Error", "Area se must be Number")
       return
    if(val5.isalpha() == True):
       messagebox.showerror("Error", "Concavity se must be Number")
       return
    if(val6.isalpha() == True):
       messagebox.showerror("Error", "Fractal Dimension se must be Number")
       return
    if(val7.isalpha() == True):
       messagebox.showerror("Error", "Smoothness Worst must be Number")
       return
    if(val8.isalpha() == True):
       messagebox.showerror("Error", "Concavity Worst must be Number")
       return
    if(val9.isalpha() == True):
       messagebox.showerror("Error", "Symmetry Worst must be Number")
       return
    if(val10.isalpha() == True):
       messagebox.showerror("Error", "Fractal Dimension Worst must be Number")
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
    list.append(val9)
    list.append(val10)
    value = b_cancer(list)

    if(value == 0):
       messagebox.showinfo("Success","You May have Benign Cancer")
    else:
       messagebox.showinfo("Success","You may have Malignant Cancer")

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")

app = customtkinter.CTk()
app.geometry("1366x550+0+0")
app.resizable(FALSE,FALSE)

image1=ImageTk.PhotoImage(Image.open("img/img2.jpg"))
label1=customtkinter.CTkLabel(master=app,image=image1,text="")
label1.pack()

text = customtkinter.CTkLabel(app, text="Breast Cancer Prediction",font=('Century Gothic',25),bg_color="light blue",text_color="red")
text.place(relx=0.48, rely=0.08)

entry_1=customtkinter.CTkEntry(master=app, height=35 ,width=320, placeholder_text='Texture Mean',font=('Century Gothic',25),bg_color="light blue",fg_color="light blue",placeholder_text_color="blue",text_color="blue")
entry_1.place(x=350, y=110)

entry_2=customtkinter.CTkEntry(master=app, height=35 ,width=320, placeholder_text='Area Mean',font=('Century Gothic',25),bg_color="light blue",fg_color="light blue",placeholder_text_color="blue",text_color="blue")
entry_2.place(x=850, y=110)

entry_3=customtkinter.CTkEntry(master=app, height=35 ,width=320, placeholder_text='Concavity Mean',font=('Century Gothic',25),bg_color="light blue",fg_color="light blue",placeholder_text_color="blue",text_color="blue")
entry_3.place(x=350, y=180)

entry_4=customtkinter.CTkEntry(master=app, height=35 ,width=320, placeholder_text='Area se',font=('Century Gothic',25),bg_color="light blue",fg_color="light blue",placeholder_text_color="blue",text_color="blue")
entry_4.place(x=850, y=180)

entry_5=customtkinter.CTkEntry(master=app, height=35 ,width=320, placeholder_text='Concavity se',font=('Century Gothic',25),bg_color="light blue",fg_color="light blue",placeholder_text_color="blue",text_color="blue")
entry_5.place(x=350, y=250)

entry_6=customtkinter.CTkEntry(master=app, height=35 ,width=320, placeholder_text='Fractal Dimension se',font=('Century Gothic',25),bg_color="light blue",fg_color="light blue",placeholder_text_color="blue",text_color="blue")
entry_6.place(x=850, y=250)

entry_7=customtkinter.CTkEntry(master=app, height=35 ,width=320, placeholder_text='Smoothness Worst',font=('Century Gothic',25),bg_color="light blue",fg_color="light blue",placeholder_text_color="blue",text_color="blue")
entry_7.place(x=350, y=320)

entry_8=customtkinter.CTkEntry(master=app, height=35 ,width=320, placeholder_text='Concavity Worst',font=('Century Gothic',25),bg_color="light blue",fg_color="light blue",placeholder_text_color="blue",text_color="blue")
entry_8.place(x=850, y=320)

entry_9=customtkinter.CTkEntry(master=app, height=35 ,width=320, placeholder_text='Symmetry Worst',font=('Century Gothic',25),bg_color="light blue",fg_color="light blue",placeholder_text_color="blue",text_color="blue")
entry_9.place(x=350, y=390)

entry_10=customtkinter.CTkEntry(master=app, height=35 ,width=320, placeholder_text='Fractal Dimension Worst',font=('Century Gothic',25),bg_color="light blue",fg_color="light blue",placeholder_text_color="blue",text_color="blue")
entry_10.place(x=850, y=390)


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

btn3.place(relx=0.55, rely=0.87, anchor='center')

app.mainloop()