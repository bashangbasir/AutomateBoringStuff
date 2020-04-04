import os 

# getsize() method and listdir() - listdir() is not in path module

cwd = os.getcwd()
print(cwd)

os.chdir(r"F:\AutomateBoringStuff\Files IO\files")

cwd = os.getcwd()
print(cwd)

print("folder {} size is : {}".format(cwd,os.path.getsize(os.path.join(cwd,"2.jpg"))))

print("List of file :",os.listdir(cwd)) # return list of file in the path

# Example of the filesize

total_size = 0

for file in os.listdir(cwd):
    if not os.path.isfile(os.path.join(cwd,file)):
        continue
    total_size = total_size + os.path.getsize(os.path.join(cwd,file))
print("Total size file in [{}] : {}bytes".format(cwd,total_size))

# makedirs() method
if not os.path.exists(os.path.join(cwd,"example")):
    print("Create folder!")
    os.makedirs(os.path.join(cwd,"example"))
else:
    print("Folder already exist")
    

