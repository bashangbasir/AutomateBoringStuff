import smtplib
#sending email  procedure 

#1. create connection to smtp
connection = smtplib.SMTP("smtp.gmail.com", 587)

#2. start connection - return tuple which first element is the connection status code. 250 is successfull
response_ehlo = connection.ehlo()
print(response_ehlo)

#3. start tls encryption
response_tls = connection.starttls()
print(response_tls)

#4. login to email 
connection.login("email_address","password")

#5. Send email
connection.sendmail("sender_email","receiver_email","Subject: Hello .... \n\n Dear Bassam,\nHello this is email from script\n\n -bassam script ")

#6. quit connection
connection.quit()


