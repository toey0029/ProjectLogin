from tkinter import *

def Window_choice():
    window_choice = Tk()
    window_choice.option_add("*font","consolas 30")
    window_choice.title("Project Login")
    Label(window_choice,text = "Welcome to Project Login").grid()
    choice_login = Button(window_choice,text = "Login",bd = 5,width=8).grid()
    choice_login.bind("<Button-1>",)
    choice_regis = Button(window_choice,text = "Register",bd = 5,width=8,command=choice_login).grid()
    window_choice.mainloop()

def Window():
    main_Window = Tk()
    main_Window.title("Login")
    #main_Window.geometry("350x300")
    main_Window.option_add("*font","Helvetica 20")
    Label(main_Window,text = "Login",font = ("Helvetica",35),anchor = CENTER).grid(row = 0,column = 1)
    Label(main_Window,text = "Username").grid(row = 1,column = 0)
    username = Entry(main_Window).grid(row = 1,column = 1)
    Label(main_Window,text="Password").grid(row = 2,column = 0)
    password = Entry(main_Window).grid(row = 2,column = 1)
    #register = Button(main_Window, text="Register").grid(row=3, column = 0)
    login = Button(main_Window,text = "Login",bd=5).grid(row = 3, column = 0)
    forgot_password = Button(main_Window,text = "Forgot Password",bd=5).grid(row = 3,column = 1)
    main_Window.mainloop()


class User():
    name = ""
    lastName = ""
    users = ""
    password = ""


Window_choice()
#Window()