import smtplib
from email.mime.text import MIMEText
from key import key
def send_email(sender_email, sender_password, recipient_email, subject, body):
  """Sends an email using Gmail's SMTP server.

  Args:
    sender_email: Your Gmail address.
    sender_password: Your Gmail password (or App Password for enhanced security).
    recipient_email: The email address of the recipient.
    subject: The subject of the email.
    body: The text content of the email.

  Raises:
    smtplib.SMTPException: If an error occurs during the email sending process.
  """
  try:
    # Create an SMTP session
    server = smtplib.SMTP('smtp.gmail.com', 587) 
    server.starttls()  # Enable TLS for secure connection
    server.login(sender_email, sender_password)

    # Create the email message
    msg = MIMEText(body)
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    # Send the email
    server.sendmail(sender_email, recipient_email, msg.as_string())
    print("Email sent successfully!")

  except smtplib.SMTPException as e:
    print(f"Error sending email: {e}")

  finally:
    server.quit()

