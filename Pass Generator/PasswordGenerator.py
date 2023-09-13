from tkinter import *
import string
import random


def generator():
    smallChar = string.ascii_lowercase
    capitalChar = string.ascii_uppercase
    number_s= string.digits
    specialCharacter = string.punctuation

    all_char = smallChar+capitalChar+number_s+specialCharacter
    passwordLength= int(password_length_input.get())   

    password = random.sample(all_char, passwordLength)


    generated_pass.delete(0,"end")
    generated_pass.insert(0,password)


def clear():
    password_length_input.delete(0,"end")
    generated_pass.delete(0,"end")
    user_name_input.delete(0,"end")


main=Tk()
main.geometry("450x350")
main.title("Password Generator")

passlebel= Label(main, text="Password Generator",font=("times new roman", 18, "bold"))
passlebel.pack()

user_name = Label(main, text = "Enter Username:", font=("times new roman", 14))
user_name.place(x = 30, y = 60) 
   
length = Label(main, text = "Enter Password Length:", font=("times new roman", 14))
length.place(x = 30,y = 100) 

password = Label(main, text = "Generated Password:", font=("times new roman", 14,))
password.place(x = 30,y = 140) 

user_name_input = Entry(main, width = 30)
user_name_input.place(x = 220,y = 60) 
   
password_length_input = Entry(main, width = 30)
password_length_input.place(x = 220, y = 100)

generated_pass = Entry(main, width = 30, fg="red")
generated_pass.place(x = 220, y = 140)
   
generate_btn = Button(main, text = "Generate password", font=("times new roman", 14),pady=10, command=generator)
generate_btn.pack(anchor= CENTER)
generate_btn.place(x=125,y=200)

generate_btn = Button(main, text = "Reset", font=("times new roman", 14), command=clear)
generate_btn.pack(anchor= CENTER)
generate_btn.place(x=180,y=270)

main.mainloop()