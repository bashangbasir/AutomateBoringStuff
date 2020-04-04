import os 

# dirname() method - retrieve the directory part of the path (folder part)

dirname = os.path.dirname("F:\\AutomateBoringStuff\\Files IO\\files\\2.jpg")
print("Dir name:",dirname)

# basename() method - retrieve the last slash in path 

basename = os.path.basename("F:\\AutomateBoringStuff\\Files IO\\files\\2.jpg")
print("Base name : ",basename)

#exists() method - check file exist or not (return bool)

print("Is 2.jpg exist: ",os.path.exists("F:\\AutomateBoringStuff\\Files IO\\files\\2.jpg"))

print("Is 3.jpg exist: ",os.path.exists("F:\\AutomateBoringStuff\\Files IO\\files\\3.jpg"))

# isfile() and isdir() method 

print("Is this a file: ",os.path.isfile("F:\\AutomateBoringStuff\\Files IO\\files\\2.jpg"))
print("Is this a file: ",os.path.isfile("F:\\AutomateBoringStuff\\Files IO\\files"))

print("Is this a directory: ",os.path.isdir("F:\\AutomateBoringStuff\\Files IO\\files"))
print("Is this a directory: ",os.path.isdir("F:\\AutomateBoringStuff\\Files IO\\files\\2.jpg"))

