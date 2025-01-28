import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email credentials
from_addr = 'bokdesaurabh802@gmail.com'
to_addr = 'bokadesaurabh88@gmail.com'  # Corrected typo
password = "xktd gjfz rjaz upfu"  # Consider using an app password if 2FA is enabled

# Create the email message
msg = MIMEMultipart()
msg['From'] = from_addr
msg['To'] = to_addr
msg['Subject'] = 'Just to Check'

body = 'Hello World'
msg.attach(MIMEText(body, 'plain'))

try:
    # Connect to the Gmail SMTP server
    mail = smtplib.SMTP('smtp.gmail.com', 587)
    mail.ehlo()  # Identify ourselves to the SMTP server
    mail.starttls()  # Start TLS encryption
    mail.login(from_addr, password)  # Log in with your email and password

    # Send the email
    text = msg.as_string()
    mail.sendmail(from_addr, to_addr, text)
    print("Email sent successfully!")

except smtplib.SMTPAuthenticationError:
    print("Failed to login: Check your email and password.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    mail.quit()  # Ensure the connection is closed
