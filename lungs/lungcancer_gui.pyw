import customtkinter
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
from lungs import lung_cancer

def getInput():
    val1 = entry_of_gender.get()
    val2 = entry_of_age.get()
    val3 = (entry_of_smoking.get())
    val4 = entry_of_anxiety.get()
    val5 = entry_of_chronic.get()
    val6 = entry_of_breath.get()
    val7 = entry_of_chest.get()
    val8 = entry_of_pain.get()

    if(val1 == ''or val2 == ''or val3 == ''or val4 == ''or val5 == ''or val6 == ''or val7 == ''or val8 == ''):
       messagebox.showerror("Error", "Please fill all Entries")
       return
    
    if(val2.isalpha() == True):
       messagebox.showerror("Error", "Age must be Number")
       return

    if(val1 == 'M' or val1 == 'F' or val1 == "m" or val1 == 'f'):
       if(val1 == 'M' or val1 == 'm'):
          val1 = 1
       else:
          val1 = 0
       
    else:
       messagebox.showerror("Error", "Gender must be M or F")
       return
       
    
    if(val3.isalpha() == True or (int(val3) > 1 or int(val3) < 0)):
       messagebox.showerror("Error", "Smoking must be Number 0 or 1")
       return
    
    
    if(val4.isalpha() == True or (int(val4) > 1 or int(val4) < 0)):
       messagebox.showerror("Error", "Anxiety must be Number 0 or 1")
       return
    
    
    if(val5.isalpha() == True or (int(val5) > 1 or int(val5) < 0)):
       messagebox.showerror("Error", "Chronic must be Number 0 or 1")
       return
    
    
    if(val6.isalpha() == True or (int(val6) > 1 or int(val6) < 0)):
       messagebox.showerror("Error", "Breathing must be Number 0 or 1")
       return
    
    
    if(val7.isalpha() == True or (int(val7) > 1 or int(val7) < 0)):
       messagebox.showerror("Error", "Swallow Chest must be Number 0 or 1")
       return
    
    
    if(val8.isalpha() == True or (int(val8) > 1 or int(val8) < 0)):
       messagebox.showerror("Error", "Chest Pain must be Number 0 or 1")
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
    value = lung_cancer(list)

    if(value == 0):
       messagebox.showinfo("Success","You do not have Lungs Cancer")
    else:
       messagebox.showerror("Success","You may have Lungs Cancer")

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")

app = customtkinter.CTk()
app.geometry("1366x550+0+0")
app.resizable(FALSE,FALSE)

image1=ImageTk.PhotoImage(Image.open("img/img2.jpg"))
label1=customtkinter.CTkLabel(master=app,image=image1,text="")
label1.pack()

text = customtkinter.CTkLabel(app, text="Lung Cancer Prediction",font=('Century Gothic',25),bg_color="light blue",text_color="red")
text.place(relx=0.48, rely=0.08)

entry_of_gender=customtkinter.CTkEntry(master=app, height=35 ,width=320, placeholder_text='Gender M/F',font=('Century Gothic',25),bg_color="light blue",fg_color="light blue",placeholder_text_color="blue",text_color="blue")
entry_of_gender.place(x=350, y=110)

entry_of_age=customtkinter.CTkEntry(master=app, height=35 ,width=320, placeholder_text='Age',font=('Century Gothic',25),bg_color="light blue",fg_color="light blue",placeholder_text_color="blue",text_color="blue")
entry_of_age.place(x=850, y=110)

entry_of_smoking=customtkinter.CTkEntry(master=app, height=35 ,width=320, placeholder_text='Smoking 0/1',font=('Century Gothic',25),bg_color="light blue",fg_color="light blue",placeholder_text_color="blue",text_color="blue")
entry_of_smoking.place(x=350, y=190)

entry_of_anxiety=customtkinter.CTkEntry(master=app, height=35 ,width=320, placeholder_text='Anxiety 0/1',font=('Century Gothic',25),bg_color="light blue",fg_color="light blue",placeholder_text_color="blue",text_color="blue")
entry_of_anxiety.place(x=850, y=190)

entry_of_chronic=customtkinter.CTkEntry(master=app, height=35 ,width=320, placeholder_text='Chronic Disease 0/1 ',font=('Century Gothic',25),bg_color="light blue",fg_color="light blue",placeholder_text_color="blue",text_color="blue")
entry_of_chronic.place(x=350, y=270)

entry_of_breath=customtkinter.CTkEntry(master=app, height=35 ,width=320, placeholder_text='Breathing Issue 0/1',font=('Century Gothic',25),bg_color="light blue",fg_color="light blue",placeholder_text_color="blue",text_color="blue")
entry_of_breath.place(x=850, y=270)

entry_of_chest=customtkinter.CTkEntry(master=app, height=35 ,width=320, placeholder_text='Swallow Chest',font=('Century Gothic',25),bg_color="light blue",fg_color="light blue",placeholder_text_color="blue",text_color="blue")
entry_of_chest.place(x=350, y=350)

entry_of_pain=customtkinter.CTkEntry(master=app, height=35 ,width=320, placeholder_text='Chest Pain 0/1',font=('Century Gothic',25),bg_color="light blue",fg_color="light blue",placeholder_text_color="blue",text_color="blue")
entry_of_pain.place(x=850, y=350)


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