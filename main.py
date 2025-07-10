import tkinter as tk
from tkinter import ttk
from PasswordManager import PasswordManager
from PasswordGenerator import PasswordGenerator


#----------------------------------------------------------------------------------------------------------------------#


pm = None
current_window = None
entry_username = None
entry_password = None
entry_MFA = None
entry_gmail = None


#----------------------------------------------------------------------------------------------------------------------#


def open_login_screen(incorrect = False, account_exists = False, empty_string = False, insecure_password = False):
    global pm
    pm = PasswordManager()

    # Create the main window
    global current_window
    current_window = tk.Tk()
    current_window.title("Password Manager")

    # Set the initial size of the window
    current_window.geometry("400x200+750+400")  

    # Username label and textbox
    global entry_username
    label_username = tk.Label(current_window, text="Username:")
    label_username.pack()
    entry_username = tk.Entry(current_window)
    entry_username.pack()

    # Password label and textbox
    global entry_password
    label_password = tk.Label(current_window, text="Password:")
    label_password.pack()
    entry_password = tk.Entry(current_window, show="*")
    entry_password.pack()

    # LogIn button
    LogIn_button = tk.Button(current_window, text="LogIn", command=login_function)
    LogIn_button.pack()

    # Create Account button
    create_account_button = tk.Button(current_window, text="Create Account", command=create_account_function)
    create_account_button.pack()

    if incorrect:
        label_username = tk.Label(current_window, text="Previous login failed, try again!")
        label_username.pack()

    if account_exists:
        label_username = tk.Label(current_window, text="Username is taken, please try again!")
        label_username.pack()

    if empty_string:
        label_username = tk.Label(current_window, text="Please enter all fields and try again!")
        label_username.pack()

    if insecure_password:
        label_username = tk.Label(current_window, text="Please use a secure password and try again!")
        label_username.pack()

    # Run the main loop
    current_window.mainloop()


#----------------------------------------------------------------------------------------------------------------------#


def create_account_function():
    global current_window, entry_username, entry_password
    new_username = entry_username.get()
    new_password = entry_password.get()
    if len(new_password) < 8:
        current_window.destroy()
        open_login_screen(False, False, False, True)
    elif new_username != None and new_password != None and new_username != "" and new_password != "":
        open_gmail_window(new_username, new_password)
    else:
        current_window.destroy()
        open_login_screen(False, False, True)

def open_gmail_window(username, password):
    global current_window
    current_window.destroy()

    current_window = tk.Tk()
    current_window.title("Password Manager")
    current_window.geometry("400x200+750+400")

    label_gmail = tk.Label(current_window, text="Enter your gmail for 2FA:")
    label_gmail.pack()

    global entry_gmail
    entry_gmail = tk.Entry(current_window, width=50)
    entry_gmail.pack()

    enter_gmail_button = tk.Button(current_window, text="Confirm", command=lambda: gmail_function(username, password))
    enter_gmail_button.pack()

def gmail_function(username, password):
    global current_window, entry_gmail
    new_gmail = entry_gmail.get()
    account_made = pm.create_account(username, password, new_gmail)
    if account_made:
        current_window.destroy()
        open_login_screen()
    else:
        current_window.destroy()
        open_login_screen(False, True)


#----------------------------------------------------------------------------------------------------------------------#


def login_function():
    global current_window, entry_username, entry_password
    username_guess = entry_username.get()
    password_guess = entry_password.get()
    
    correct_creds = pm.login(username_guess, password_guess)
    
    if correct_creds:
        open_MFA_window()
    else: 
        current_window.destroy()
        open_login_screen(True)

def open_MFA_window():
    global current_window
    current_window.destroy()

    current_window = tk.Tk()
    current_window.title("Password Manager")
    current_window.geometry("400x200+750+400")

    label_MFA = tk.Label(current_window, text="Enter MFA Code:")
    label_MFA.pack()

    global entry_MFA
    entry_MFA = tk.Entry(current_window)
    entry_MFA.pack()

    enter_MFA_button = tk.Button(current_window, text="Verify", command=MFA_button)
    enter_MFA_button.pack()

def MFA_button():
    global current_window, entry_MFA
    try:
        MFA_guess = int(entry_MFA.get())
    except:
        current_window.destroy()
        open_login_screen(True)
    
    MFA_correct = pm.check_MFA(MFA_guess)
    if MFA_correct:
        open_password_manager()
    else:
        current_window.destroy()
        open_login_screen(True)


#----------------------------------------------------------------------------------------------------------------------#


def open_password_manager():
    global current_window, pm
    current_window.destroy()

    current_window = tk.Tk()
    current_window.title("Password Manager")
    current_window.geometry("700x400+550+300")

    label = tk.Label(current_window, text="Welcome to the Password Manager Account screen!")
    label.pack()

    tree = ttk.Treeview(current_window, columns=("Application", "Username", "Password"), show="headings")
    tree.heading("Application", text="Application")
    tree.heading("Username", text="Username")
    tree.heading("Password", text="Password")
    tree.pack()

    account_creds_list = pm.display_all()
    for row in account_creds_list:
        tree.insert("", "end", values=row)

    add_creds_button = tk.Button(current_window, text="Add Entry", command=add_creds_function)
    add_creds_button.pack()

    edit_creds_button = tk.Button(current_window, text="Edit Entry", command=edit_creds_function)
    edit_creds_button.pack()

    delete_creds_button = tk.Button(current_window, text="Delete Entry", command=delete_creds_function)
    delete_creds_button.pack()

    logout_button = tk.Button(current_window, text="LogOut", command=logout_function)
    logout_button.pack()


#----------------------------------------------------------------------------------------------------------------------#


def add_creds_function():
    temp_window = tk.Tk()
    temp_window.title("Password Manager")

    # Set the initial size of the window
    temp_window.geometry("400x200+750+400")  

    label_application = tk.Label(temp_window, text="Application:")
    label_application.pack()
    entry_application = tk.Entry(temp_window)
    entry_application.pack()

    label_username = tk.Label(temp_window, text="Username:")
    label_username.pack()
    entry_username = tk.Entry(temp_window)
    entry_username.pack()

    label_password = tk.Label(temp_window, text="Password:")
    label_password.pack()
    entry_password = tk.Entry(temp_window)
    entry_password.pack()

    # LogIn button
    submit_button = tk.Button(temp_window, text="Add", command=lambda: add_creds_call(entry_application.get(), entry_username.get(), entry_password.get(), temp_window))
    submit_button.pack()

def add_creds_call(app, username, password, temp_window):
    global current_window, pm
    pm.add_new_creds(app, username, password)
    temp_window.destroy()
    open_password_manager()


#----------------------------------------------------------------------------------------------------------------------#


def edit_creds_function():
    temp_window = tk.Tk()
    temp_window.title("Password Manager")

    # Set the initial size of the window
    temp_window.geometry("400x200+750+400")  

    label_application = tk.Label(temp_window, text="Application:")
    label_application.pack()
    entry_application = tk.Entry(temp_window)
    entry_application.pack()

    label_username = tk.Label(temp_window, text="New Username:")
    label_username.pack()
    entry_username = tk.Entry(temp_window)
    entry_username.pack()

    label_password = tk.Label(temp_window, text="New Password:")
    label_password.pack()
    entry_password = tk.Entry(temp_window)
    entry_password.pack()

    # LogIn button
    submit_button = tk.Button(temp_window, text="Change", command=lambda: edit_creds_call(entry_application.get(), entry_username.get(), entry_password.get(), temp_window))
    submit_button.pack()

def edit_creds_call(app, username, password, temp_window):
    global current_window, pm
    pm.edit_website_creds(app, username, password)
    temp_window.destroy()
    open_password_manager()


#----------------------------------------------------------------------------------------------------------------------#


def delete_creds_function():
    temp_window = tk.Tk()
    temp_window.title("Password Manager")

    # Set the initial size of the window
    temp_window.geometry("400x200+750+400")  

    label_application = tk.Label(temp_window, text="Application:")
    label_application.pack()
    entry_application = tk.Entry(temp_window)
    entry_application.pack()

    # LogIn button
    submit_button = tk.Button(temp_window, text="Change", command=lambda: delete_creds_call(entry_application.get(), temp_window))
    submit_button.pack()

def delete_creds_call(app, temp_window):
    global current_window, pm
    pm.delete_website_creds(app)
    temp_window.destroy()
    open_password_manager()


#----------------------------------------------------------------------------------------------------------------------#


def logout_function():
    global current_window
    current_window.destroy()
    open_login_screen()


#----------------------------------------------------------------------------------------------------------------------#


open_login_screen()
