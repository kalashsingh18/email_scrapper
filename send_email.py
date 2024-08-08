import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email configuration
def send(email,team_name):  
  smtp_server = "smtpout.secureserver.net"
  smtp_port = 465  # Use 587 if you're using TLS
  email_address = "info@indoricoders.com"
  email_password = "IndoriCoders@12"
  
# Create the email content
  msg = MIMEMultipart()
  msg['From'] = email_address
  msg['To'] = email
  msg['Subject'] = "Registration Email From INDORICODERS "

# Create the body of the message (a plain-text and an HTML version)

  html = ""
  with open("index.html", 'r') as html_file:
    html = html_file.read()
    html = html.replace("{team_name}", team_name)


# Attach parts into message container.
  
  msg.attach(MIMEText(html, 'html'))
  mail_not_sent=[]
# Connect to the server and send the email
  try:
    server = smtplib.SMTP_SSL(smtp_server, smtp_port)
    server.login(email_address, email_password)
    server.sendmail(email_address, email, msg.as_string())
    print(email,"sent_email sucessfully")
    server.quit()
   
  except Exception as e:
    print(email)
    return True

    # send("info@indoricoders.com","the email is not sent")


