# concepts about file
# 1) filename - ex: ex1."file extension"
# 2) file path - ex: C:\Users\"username"\Desktop\example
#   - file extension represent the file format of the file. it comes after the "dot".

# path example.
path = "F:\\AutomateBoringStuff\\Files IO"

#using raw string format
path_rawformat = r"F:\AutomateBoringStuff\Files IO"

print("path :",path)
print("path :",path_rawformat)

# in the example above the path using backslash which is for windows.
# However for Mac and linux the path use slash.
# to make the script that can be used with diff OS,
# python have OS module to overcome this limitation.

import os

path = os.path.join("folder1","folder2","folder3","file.png")
print(path)

#if this above code is run in other os(Mac or Linux), the result will be fowardslash as the separator.
#you can check the separator for the os by using os.sep

print(os.sep) # result will be "\" for windows and "/" for mac or linux

# from os module, we can get the current working directory by using os.getcwd() method

current_working_path = os.getcwd()
print(current_working_path)

# to change the working directory, can use os.chdir() method

os.chdir(r'F:\AutomateBoringStuff')
print(os.getcwd())

# path can be classified into two : absolute and relative path
# absolute path - give the complete location of the program/path
# relative path - give location relative to the current working directory

os.chdir("F:\\AutomateBoringStuff\\Files IO\\files")
abs_path = os.path.abspath("1.jpg") #return the absolute path
print("Absolute path: ",abs_path)

print("Is [ {} ] Absolute path : {}".format(abs_path,os.path.isabs(abs_path))) #return bool. True is path is absolute

os.chdir("F:\\AutomateBoringStuff")
rel_path = os.path.relpath("F:\\AutomateBoringStuff\\Files IO\\files\\2.jpg","F:\\AutomateBoringStuff")
print("Relative path: ",rel_path)
