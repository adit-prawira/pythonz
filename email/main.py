import smtplib
from config import my_email, my_password, target_email

emailProvider = {
    "gmail":"smtp.gmail.com",
    "hotmail": "smtp.live.com",
    "yahoo":"smtp.mail.yahoo.com"
}

connection = smtplib.SMTP(emailProvider["gmail"])

# secure email connection
connection.starttls()

# login
connection.login(user = my_email, password = my_password )

connection.sendmail(
    from_addr=my_email, 
    to_addrs=target_email, 
    msg = "Subject:Hi\n\nHey"
)

connection.close()