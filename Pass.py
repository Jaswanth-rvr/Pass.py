from tkinter import *
import string
import random

def generate_password():
    password = ''
    lowercase_letters = list(string.ascii_lowercase)
    uppercase_letters = list(string.ascii_uppercase)
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    characters = lowercase_letters + uppercase_letters + digits
    
    length = int(length_entry.get())
    for _ in range(length):
        password += str(random.choice(characters))
    
    generated_entry.delete(0, END)
    generated_entry.insert(0, password)

def reset_fields():
    username_entry.delete(0, END)
    length_entry.delete(0, END)
    generated_entry.delete(0, END)
    message_label.config(text="", bg="#0af0de")
    password_label.config(text="", bg="#0af0de")

def display_message():
    message = username_entry.get() + " ! Please Remember Your Password: "
    message_label.config(text=message,
                         font=("Courier", 20, "bold"),
                         fg="blue",
                         bg="#0af0de")
    password_label.config(text=generated_entry.get(),
                          font=("Courier", 20, "bold"),
                          bg="#0af0de")

window = Tk()
window.geometry("1000x700")
window.config(bg="#0af0de")
window.title("PASSWORD GENERATOR")

title_label = Label(window,
                    text="Password Generator",
                    font=("Courier", 40, "bold"),
                    fg="black",
                    bg="#0af0de")
title_label.place(x=300, y=20)

username_label = Label(window,
                       text="Enter username: ",
                       font=("Courier", 20, "bold"),
                       fg="red",
                       bg="#0af0de")
username_label.place(x=200, y=150)

username_entry = Entry(window,
                       font=("Courier", 20),
                       fg="black",
                       bg="white")
username_entry.place(x=600, y=150)

length_label = Label(window,
                     text="Enter password length: ",
                     font=("Courier", 20, "bold"),
                     fg="red",
                     bg="#0af0de")
length_label.place(x=200, y=250)

length_entry = Entry(window,
                     font=("Courier", 20),
                     fg="black",
                     bg="white")
length_entry.place(x=600, y=250)

generated_label = Label(window,
                        text="Generated Password: ",
                        font=("Courier", 20, "bold"),
                        fg="green",
                        bg="#0af0de")
generated_label.place(x=200, y=350)

generated_entry = Entry(window,
                        font=("Courier", 20, "bold"),
                        fg="black",
                        bg="lightyellow")
generated_entry.place(x=600, y=350)

generate_button = Button(window,
                         text="GENERATE PASSWORD",
                         font=("Impact", 20),
                         bg="blue",
                         fg="white",
                         bd=2,
                         command=generate_password)
generate_button.place(x=630, y=450)

accept_button = Button(window,
                       text="ACCEPT",
                       font=("Impact", 17),
                       bg="yellow",
                       fg="black",
                       bd=4,
                       command=display_message)
accept_button.place(x=700, y=550)

reset_button = Button(window,
                      text="RESET",
                      font=("Impact", 17),
                      bg="yellow",
                      fg="black",
                      bd=4,
                      command=reset_fields)
reset_button.place(x=830, y=550)

message_label = Label(window, bg="#0af0de")
message_label.place(x=200, y=650)

password_label = Label(window, bg="#0af0de")
password_label.place(x=900, y=650)

window.mainloop()
