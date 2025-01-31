# tkinter : toolkit interface

import tkinter as tk
from DBMYSQL.insert_data import insert_user_data, check_user_exists

# Create a window
screen = tk.Tk()

# set height and width of the screen
screen.geometry('400x400')

# set title of the screen
screen.title("Instagram")

# set logo here
logo_path = 'images/logo.ico'
screen.iconbitmap(logo_path)

# create a label

label_legend = tk.Label(screen, text="Welcome to Instagram", )
label_legend.pack(side='top')

# set lable font size 35px
label_legend.config(font=('Arial', 18))

# set margin and padding 10px
label_legend.config(padx=10, pady=10)


# on click login btn open new window
def open_login_window():
    login_screen = tk.Toplevel()
    login_screen.geometry('400x400')
    login_screen.iconbitmap(logo_path)
    login_screen.title("Login | Instagram")
    label_login = tk.Label(login_screen, text="Login Window")
    label_login.pack(side='top')
    label_login.config(font=('Arial', 18))

    # set login form
    label_email = tk.Label(login_screen, text="Email:")
    label_email.pack()
    entry_email = tk.Entry(login_screen)
    entry_email.pack()

    label_password = tk.Label(login_screen, text="Password:")
    label_password.pack()
    entry_password = tk.Entry(login_screen, show='*')
    entry_password.pack()

    def get_login_form_data():
        email = entry_email.get()
        password = entry_password.get()
        print(check_user_exists(email, password))
        if check_user_exists(email, password):
            lg_msg = tk.Label(
                login_screen,
                text="Login Successful!",
                font=('Arial', 18),
                fg='green',
                width=20,
                height=5,
            )
            lg_msg.pack()
        else:
            lg_msg = tk.Label(
                login_screen,
                text="Login Failed!",
                font=('Arial', 18),
                fg='red',
                width=20,
                height=5,
            )
            lg_msg.pack()

    # submit btn
    submit_btn = tk.Button(login_screen, text='Submit', command=lambda: get_login_form_data())
    submit_btn.pack()
    submit_btn.config(font=('Arial', 18), bg='lightgrey', fg='black')
 
    

# on click sign up btn open new window
def open_signup_window():
    signup_screen = tk.Toplevel()
    signup_screen.geometry('400x400')
    signup_screen.iconbitmap(logo_path)
    signup_screen.title("Sign Up | Instagram")
    label_signup = tk.Label(signup_screen, text="Sign Up Window")
    label_signup.pack(side='top')
    label_signup.config(font=('Arial', 18))

    # set registration form
    label_email = tk.Label(signup_screen, text="Email:")
    label_email.pack()
    entry_email = tk.Entry(signup_screen)
    entry_email.pack()

    label_password = tk.Label(signup_screen, text="Password:")
    label_password.pack()
    entry_password = tk.Entry(signup_screen, show='*')
    entry_password.pack()

    label_confirm_password = tk.Label(signup_screen, text="Confirm password:")
    label_confirm_password.pack()
    entry_confirm_password = tk.Entry(signup_screen, show='*')
    entry_confirm_password.pack()



    def get_signup_form_data():
        email = entry_email.get()
        password = entry_password.get()
        confirm_password = entry_confirm_password.get()
        if password == confirm_password:
            reg_msg = tk.Label(
                signup_screen,
                text="Registration Successful!",
                fg="green",
                font=("Arial", 12)
            )
            reg_msg.pack(side='top')
            insert_user_data(email, password)
        else:
            reg_msg = tk.Label(
                signup_screen,
                text="Passwords do not match!",
                fg="red",
                font=("Arial", 12)
            )
            reg_msg.pack(side='top')


    # submit btn
    submit_btn = tk.Button(signup_screen, text='Submit', command=lambda: get_signup_form_data())
    submit_btn.pack()
    submit_btn.config(font=('Arial', 18), bg='lightgrey', fg='black')
   




login_btn = tk.Button(screen, text='Login', command=open_login_window)
login_btn.pack(side='top')
login_btn.config(font=('Arial', 18), bg='pink', fg='#d62976')

signup_btn = tk.Button(screen, text='Sign Up', command=open_signup_window)
signup_btn.pack(side='top')
signup_btn.config(font=('Arial', 18), bg='pink', fg='#d62976')

# set shadow in btn
login_btn.config(relief='groove', bd=5, activebackground='lightgrey')
signup_btn.config(relief='groove', bd=5, activebackground='lightgrey')




screen.mainloop()