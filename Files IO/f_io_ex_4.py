# file can be plaintext or binary file
# plaintext - contain plain text file (.txt)
# binary - example of binary file --> pdf,exe . Need certain module/software to open this.

f = open(r"F:\AutomateBoringStuff\Files IO\files\test1.txt")
content = f.read() #only can read once, to read again we need to close file and open again followed by reading it
print("Using read() method: ",content)
f.close() #always close file after read/write operation

# readlines() method - return line as string in list 

f = open(r"F:\AutomateBoringStuff\Files IO\files\test1.txt")
content = f.readlines() #return line as string in list 
print("Using readlines() method: ",content)
f.close()

# open file as write - "w" parameter (will write the file like file is blank)

f = open(r"F:\AutomateBoringStuff\Files IO\files\test2.txt","w") # as you can see we provide parameter as "w". Mean write mode
f.write("Hi there! Write something in file.") # will return how many char was write. but can ignore this info
f.close()

# Append data to file - "a" parameter 

f = open(r"F:\AutomateBoringStuff\Files IO\files\test2.txt","a")
f.write("\nAppend something to this file !")
f.close()
