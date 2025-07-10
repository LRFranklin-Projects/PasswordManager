import smtplib # Secure mail transfer protocol library
from email.message import EmailMessage # Library to build an email message
import random

def get_code() -> str: # Return a string for MFA validation
    verification_code = str(random.randint(100000, 1000000))
    return verification_code

def email_alert(to_Email) -> str:
    # Get and set the code
    current_code = get_code()
    current_code = str(current_code)

    subject = 'Email Verification Code' # Subject of email
    body = 'Your 2FA verification code: ' + current_code # Body of email

    msg = EmailMessage() # Creating email message object
    msg.set_content(body) # Setting the content of the email message
    msg['subject'] = subject # Setting the subject of the email message
    msg['to'] = to_Email # Setting the receiver of the email message

    user = "python.tempcode.alert@gmail.com" # The gmail sending the email
    msg['from'] = user # Setting the gmail to send the email message
    password = "gbef slgk ycav smui" # Password created through: myaccount.google.com/apppasswords

    server = smtplib.SMTP("smtp.gmail.com", 587) # Create an SMTP server object for GMAIL and on port 587
    server.starttls() # Put the SMTP connection in TLS mode for secure communication
    server.login(user, password) # Login to the SMTP server using the provided user and password credentials
    server.send_message(msg) # Send an email message using the server and msg object

    server.quit() # Close the server object

    return current_code # Return the MFA code to be checked

if __name__ == '__main__':
    email_alert('python.tempcode.alert@gmail.com')