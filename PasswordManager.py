from cryptography.fernet import Fernet
import hashlib
import os
import ast
import MFASender
from HTTP_Post.SwiftSequencing import SwiftSequencer

class PasswordManager:
    sw = None

    def __init__(self):
        self.password_manager = [] # List of credentials
        self.key = None # Key of current object
        self.fernet = None # Creating object of a symmetric key encryption library
        self.account_tracker_username = "" # Tracking the username of the current account
        self.valid_creds = False # Variable for when logging in
        self.account_email = "" # Variable for MFA email
        self.MFA_code = 0


    def create_key(self):
        self.key = Fernet.generate_key() # Creating a symmetric encryption key
        self.fernet = Fernet(self.key) # Pairing the key with the Fernet encryption Library
        self.sw = SwiftSequencer(self.key.decode())
    # End of create key method

    
    def load_key(self, hashed_username): # Username param to find the account
        key_file = "key.txt" # File to store the accounts for the manager
        if os.path.exists(key_file): # If statement to check the file exists
            with open(key_file, "r") as file: # Opening the file in read
                lines = file.readlines() # Getting the text document as lines of text
                if len(lines) >= 5: # Ensuring their are 5 lines meaning there has been an account made
                    for line_num in range(len(lines)): # For Loop with iterable of the line number
                        if line_num % 5 == 0: # Activating when the For Loop gets to Line 5, break line
                            if lines[line_num-4].strip() == hashed_username: # Getting the hashed username and checking it with the param username
                                self.key = lines[line_num-2].strip().encode() # Get the key for the account username
                                self.sw = SwiftSequencer(self.key.decode())
                                decrypted_key = self.sw.decrypt_key()
                                self.fernet = Fernet(decrypted_key) # Creating the account Fernet object
                                break
        else:
            #print("File not found to load key")
            pass # Pass because the print is commented out
    # End of loading key method
        
    def save_key(self, hashed_username, creating = False, keep_signed_in = False):
        # Below is encrypting your current password manager list of lists
        for sublist in self.password_manager: # Get all the groups of creds in password list
            for index, value in enumerate(sublist): # Keep track of each index and its value in the sublist
                encrypted_value = self.encrypt_data(str(value)) # Encrypting all the values at the current index
                self.password_manager[self.password_manager.index(sublist)][index] = encrypted_value # Adding the encrypted cred list to the password manager
        # End of sublist and index,value For Loops
        # Done this way to eliminate having 2 nested For Loops, and allowing for the list to be added as a whole list at once
        # Checking if the account is actually made using param variable
        account_exists = self.find_account(hashed_username)

        if account_exists and not creating: # Creating is false when not under create_account so it becomes true in order to replace accounts needing updates
            left_start = 0
            right_end = 0
            with open("key.txt", "r") as file: # Open jey file as read only
                lines = file.readlines()
                for line_num, line in enumerate(lines): # Better version of load key nested For Loops, I LEARNED!
                    if line.strip() == hashed_username: # Checking for the hashed username
                        left_start = line_num - 1 # Set the left replace variable
                        right_end = line_num + 4 # Set the right replace variable
                        #print(f'left {left_start}')
                        #print(f'right {right_end}')
                        break
                # End of find replacement text For Loop
            
            # Create variable to store replacement text and use replacement variables for correct location
            encrypted_key = self.sw.key_to_edit # When loaded the encrypted key is still inside class variable
            new_content = f"Account:\n{hashed_username}\n{self.password_manager}\n{encrypted_key}\n--------------------------------------------\n" 
            new_lines = lines[:left_start] + [new_content] + lines[right_end:] 

            with open("key.txt", "w") as file:
                file.writelines(new_lines) # Write to the file
        elif account_exists and creating: # This is for creating an account to see if it exists
            print("Account already exists")
            pass
            
        else:
            key_file = "key.txt" # Create the key file
            with open(key_file, "a") as file: # Open file and append first submission            
                self.sw = SwiftSequencer(self.key.decode())
                encrypted_key = self.sw.encrypt_key()
                file.write(f"Account:\n{hashed_username}\n{self.password_manager}\n{encrypted_key}\n--------------------------------------------\n")

        if keep_signed_in:
            self.password_manager = self.find_password_list(self.account_tracker_username)
    # End of save key function  



    def encrypt_data(self, data):
        return self.fernet.encrypt(data.encode())
    # End of encrypt data method

    def decrypt_data(self, encrypted_data):
        return self.fernet.decrypt(encrypted_data).decode()
    # End of decrypt data method



    def find_account(self, hashed_username):
        key_file = "key.txt"
        if os.path.exists(key_file):
            with open(key_file, "r") as file:
                lines = file.readlines()
                if len(lines) >= 5:
                    for line_num in range(len(lines)):
                        if line_num % 5 == 0:
                            if lines[line_num-4].strip() == hashed_username: # Checking if the username matches for every username line
                                return True
        return False
    # End of find account method

    def create_account(self, main_username, main_password, main_email):
        #main_username = str(input('Enter your username: '))
        #main_password = str(input('Enter your password: ')) 
        #main_email = str(input('Enter your 2FA email: '))   
        hashed_main_username = hashlib.sha256(main_username.encode()).hexdigest() # Encrypting username using Sha256
        hashed_main_password = hashlib.sha256(main_password.encode()).hexdigest() # Encrypting password using Sha256
        if not self.find_account(hashed_main_username):
            self.password_manager += [['Main', hashed_main_username, hashed_main_password]] # The first list in each password manager account is the main login
            #print('Account created successfully.')

            self.create_key() # Creating account key

            self.password_manager += [['2FA', main_email, '']] # The second list in each password manager account is the 2FA email
            self.save_key(hashed_main_username, creating = True) # Save the key and account creds list
            return True
        else:
            return False
    # End of account creation method


    def login(self, main_username_guess, main_password_guess):
        # main_username_guess = str(input("Enter your username: "))
        # main_password_guess = str(input("Enter your password: "))
        hashed_main_username_guess = hashlib.sha256(main_username_guess.encode()).hexdigest()
        hashed_main_password_guess = hashlib.sha256(main_password_guess.encode()).hexdigest()

        account_found = self.find_account(hashed_main_username_guess) # Check for account

        if account_found:
            self.load_key(hashed_main_username_guess) # Load the account key

            self.password_manager = self.find_password_list(hashed_main_username_guess) # Getting the list associating with the account

            self.valid_creds = self._check_for_creds('Main', hashed_main_username_guess, hashed_main_password_guess) # Validating the username AGAIN, but also validating password
            
            if self.valid_creds: # Only run 2FA if account is right
                self.account_email = self.password_manager[1][1] # Getting the 2FA email
                self.MFA_code = int(MFASender.email_alert(self.account_email)) # Getting the int email one time code
                #MFA_code_guess = int(str(input('Enter your email verification code: ')))
                #if MFA_code == MFA_code_guess:
                    #print('Verification code match')
                    #return True
                return True

            return False
        else:
            #print("Account not found")
            self.valid_creds = False # Account wasn't found
            self.password_manager = [] # Empty account list of lists
            return False
    # End of LogIn method

    def check_MFA(self, MFA_code_guess):
        #MFA_code_guess = int(str(input('Enter your email verification code: ')))
        if self.MFA_code == MFA_code_guess:
            #print('Verification code match')
            return True
        return False
    # End of MFA checker method


    def add_new_creds(self, new_website, new_username, new_password):
        #print(f"Are the creds valid? {self.valid_creds}")
        if self.valid_creds:
            #new_website = str(input("Enter the website: "))
            #new_username = str(input(f'Enter your username for {new_website}: '))
            #new_password = str(input(f"Enter your password for {new_website}: "))
            self.password_manager += [[new_website, new_username, new_password]]
            self.save_key(self.account_tracker_username, False, True)  # Save to txt file immediately
        else:
            #print("Invalid credentials, cannot add new entry")
            pass
    # End of adding creds method



    def find_password_list(self, hashed_username):
        key_file = "key.txt"
        encrypted_list = []
        if os.path.exists(key_file):
            with open(key_file, "r") as file:
                lines = file.readlines()
                if len(lines) >= 5:
                    for line_num in range(len(lines)):
                        if line_num % 5 == 0:
                            if lines[line_num-4].strip() == hashed_username:
                                encrypted_list = lines[line_num-3].strip() # Getting the list of encrypted values for the account
                                encrypted_list_of_lists = ast.literal_eval(encrypted_list) # Convert a string representation of list into actual list, better type cast
                                # Decrypt each value in the nested lists
                                for i in range(len(encrypted_list_of_lists)):
                                    for j in range(len(encrypted_list_of_lists[i])):
                                        if isinstance(encrypted_list_of_lists[i][j], bytes): # Checks if the value in the list is in byte format to decrypt
                                            decrypted_value = self.decrypt_data(encrypted_list_of_lists[i][j]) # Decrypt the value
                                            #print(f'Index is {i}, {j} and it is now: {decrypted_value}')  # Debug print
                                            encrypted_list_of_lists[i][j] = decrypted_value # Set the value of the original to decrypted value
                                return encrypted_list_of_lists # Return decrypted list
        return None
    # End of find the password list method

    def _check_for_creds(self, website, username, password):
        for sublist in self.password_manager:
            if sublist[0].lower() == website.lower():
                if username == sublist[1] and password == sublist[2]: # Check if hashed username and password match
                    #print("Login Credentials Match")
                    self.account_tracker_username = username # Set the account username
                    return True
                else:
                    #print("Invalid Login Credentials")
                    return False  
        #print('Invalid website')
        return False
    # End of checking for LogIn credentials match



    def save_new_info(self):
        self.save_key(self.account_tracker_username, True)
    # Method for GUI integration use



    def edit_website_creds(self, website, new_username, new_password):
        if website.lower() != "main" and website.lower() != "2fa":
            if self.valid_creds :
                for i in range(len(self.password_manager)):
                    if self.password_manager[i][0].lower() == website.lower():
                        self.password_manager[i][1] = new_username
                        self.password_manager[i][2] = new_password
                        self.save_key(self.account_tracker_username, False, True)  # Save to txt file immediately
                        break
                    else:
                        #print(f'\nThere is no account credentials for: {website}')
                        pass
        else:
            pass
    # End of specific method display

    def delete_website_creds(self, website):
        if website.lower() != "main" and website.lower() != "2fa":
            if self.valid_creds :
                for i in range(len(self.password_manager)):
                    if self.password_manager[i][0].lower() == website.lower():
                        self.password_manager.pop(i)
                        self.save_key(self.account_tracker_username, False, True)  # Save to txt file immediately
                        break
                    else:
                        #print(f'\nThere is no account credentials for: {website}')
                        pass
        else: 
            pass
    # End of specific method display

    def display_all(self):
        if self.valid_creds :
            #for sublist in self.password_manager:
                #print(f"\nWebsite creds: {sublist[0]}, Username: {sublist[1]}, Password: {sublist[2]}")
            return self.password_manager
    # End of display all creds function

# End of class

if __name__ == "__main__":
    var = int(input("Please input 1 for create account or 2 for login: "))
    var2 = "False"
    pm = PasswordManager()

    if var == 1:
        pm.create_account()
        var2 = pm.login()
    elif var == 2:
        var2 = pm.login()
        
    if var2:
        pm.add_new_creds()