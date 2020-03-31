from tkinter import *

class User():
    name = ""
    lastName = ""
    users = ""
    password = ""

def Window():
    main_Window = Tk()
    main_Window.title("Login")
    main_Window.option_add("*font","Helvetica 20")
    Label(main_Window,text = "Login",font = ("Helvetica",35),anchor = CENTER).grid(row = 0,column = 1)
    Label(main_Window,text = "Username").grid(row = 1,column = 0)
    username = Entry(main_Window)
    username.grid(row = 1,column = 1)

    Label(main_Window,text="Password").grid(row = 2,column = 0)
    password = Entry(main_Window)
    password.grid(row = 2,column = 1)

    login = Button(main_Window,text = "Login",bd=5)
    login.grid(row = 3, column = 0)

    forgot_password = Button(main_Window,text = "Forgot Password",bd=5)
    forgot_password.grid(row = 3,column = 1)
    main_Window.mainloop()

def Register(User):



def Window_choice():
    window_choice = Tk()
    window_choice.option_add("*font","consolas 30")
    window_choice.title("Project Login")
    Label(window_choice,text = "Welcome to Project Login").grid()

    choice_login = Button(window_choice,text = "Login",bd = 5,width=8,command=Window)
    choice_login.grid()


    choice_regis = Button(window_choice,text = "Register",bd = 5,width=8)
    choice_regis.grid()
    window_choice.mainloop()







Window_choice()
Window()