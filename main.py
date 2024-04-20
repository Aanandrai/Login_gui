from tkinter import *   #use to import the liberary
# import PIL
from PIL import ImageTk
from PIL import Image
from tkinter import messagebox
root=Tk()   #make root object of TK class
root.title("Login form")  #use to change the title of window
root.iconbitmap('icon.ico')  #used to set icon of window

def handle_login():
    email=email_input.get()
    password=password_input.get()

    if(email=='aanand@gmail.com' and password=='1234'):
        messagebox.showinfo("Yeep login successful")

    else:
        messagebox.showerror("login failed")



# use to define min and max size
# root.minsize(500, 400)
# root.maxsize(500, 700)

root.geometry('350x500')  #use to give fixed geometry
root.maxsize(350,600)

root.configure(background='#0096DC')   #used to set the background of window

img=Image.open('flipkart-icon.png')   #used to open a image
resize_img=img.resize((100,100))     #used to resize the image
img=ImageTk.PhotoImage(resize_img)   #
img_lable= Label(root,image=img)     #labing the image

img_lable.pack(pady=(10,10))        #placing the image on gui


text_lable=Label(root,text="Flipkart",fg="white",bg="#0096DC")   #adding label and setting property
text_lable.pack(pady=(10,10))
text_lable.config(font=('verdana',24))  #used to design the text

email_label=Label(root, text="Enter Email" ,fg="white", bg="#0096DC")
email_label.pack(pady=(20,5))
email_label.config(font=("verdana",12))

email_input=Entry(width=40)
email_input.pack(ipady=4, pady=(1,7))


password_label=Label(root, text="Enter password" ,fg="white", bg="#0096DC")
password_label.pack(pady=(10,5))
password_label.config(font=("verdana",12))

password_input=Entry(width=40)
password_input.pack(ipady=4, pady=(1,7))

login_button=Button(root, text="Login", fg="black", bg="white",width=15,height=2,command=handle_login)
login_button.pack(pady=(18,5))
login_button.config(font=("verdana",13))

root.mainloop()  #this is used to hold the GUI screan
