import smtplib

my_email = "johnedaise@yahoo.com"
password = "Jedwin19870805"

connection = smtplib.SMTP_SSL("smtp.mail.yahoo.com")
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs="jdaise@gmail.com",msg="Hello")
connection.close()
