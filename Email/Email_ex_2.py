import imapclient
import pyzmail

#documentation for imapclient : https://imapclient.readthedocs.org
#documentation for pyzmail : http://magiksys.net/pyzmail

#create imap object
connection = imapclient.IMAPClient("imap.gmail.com",ssl=True)

# login to imap service
connection.login("email_address","password")

#select folder of email you want to access
#can get list of folser by using 
list_folder = connection.list_folders()
#readonly = false, you can delete email
connection.select_folder("INBOX",readonly=True)

#search email - return UIDs in list 
#search keys - "ALL", "BEFORE date", "ON date", "SINCE date", "SUBJECT string", "BODY string", "TEXT string" and etc
#for this example, we use "SINCE date"
UIDs = connection.search(["SINCE 1-Jan-2020"])

#choose UID from list - this code take the latest email
UID = UIDs[-1]

#fetch raw email
raw_email = connection.fetch([UID],["BODY[]","FLAGS"])

messages = pyzmail.PyzMessage.factory(raw_email[UID][b'BODY[]'])

# get subject
subject = messages.get_subject()

# get from, to, bcc addresses - will retrun list
from_list = messages.get_addresses("from")
to_list = messages.get_addresses("to")
bcc_list = messages.get_addresses("bcc")

#check email is text or html 
messages.text_part
messages.html_part

messages.text_part.get_payload().decode("UTF-8")

connection.logout()