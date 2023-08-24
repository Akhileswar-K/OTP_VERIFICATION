import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def generate_otp():
    return random.randint(100000, 999999)

def send_email(sender_email, app_password, receiver_email, subject, message):
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject
    msg.attach(MIMEText(message, "plain"))

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        try:
            server.login(sender_email, app_password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
            print("OTP sent successfully!")
        except smtplib.SMTPAuthenticationError:
            print("SMTP authentication failed.")

def verify_otp():
    sender_email = "akkykuppachi31@gmail.com"
    app_password = "gjouvxhuidgyvuwl"

    email = input("Enter your email: ")
    receiver_email = email
    subject = "Your OTP"

    otp = generate_otp()
    message = f"Your OTP is: {otp}"

    send_email(sender_email, app_password, receiver_email, subject, message)

    user_otp = input("Enter the OTP you received: ")
    if user_otp == str(otp):
        print("OTP verification successful!")
    else:
        print("OTP verification failed!")

verify_otp()
