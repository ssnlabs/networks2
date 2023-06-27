import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, sender_password, recipient_email, subject, message):
    # SMTP server configuration
    smtp_server = "smtp.gmail.com"
    smtp_port = 587  # Use the appropriate port for your SMTP server

    # Create a MIME multipart message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    # Add the message body
    msg.attach(MIMEText(message, 'plain'))

    try:
        # Connect to the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)

        # Send the email
        server.sendmail(sender_email, recipient_email, msg.as_string())

        # Disconnect from the server
        server.quit()

        print('Email sent successfully!')
    except smtplib.SMTPException as e:
        print('Error sending email:', str(e))

# Example usage
sender_email = 'arunvijaynov10@gmail.com'
sender_password = 'arun@8018'
recipient_email = 'arunvijaynov10@gmail.com'
subject = 'successful implementation of SMTP protocol'
message = 'SMTP protocol was successfully implemented Harsh and Jai'

send_email(sender_email, sender_password, recipient_email, subject, message)