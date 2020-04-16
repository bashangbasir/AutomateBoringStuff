#! python3

import webbrowser, sys
import pyperclip

sys.argv #read command line 

if len(sys.argv) > 1:
    address = " ".join(sys.argv[1:])

else:
    address = pyperclip.paste()

#https://www.google.com.my/maps/place/Bachok,+Kelantan
webbrowser.open("https://www.google.com.my/maps/place/"+address)

