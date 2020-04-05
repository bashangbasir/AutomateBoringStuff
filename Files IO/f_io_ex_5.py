import os
import shelve # use to make binary file

os.chdir(r"F:\AutomateBoringStuff\Files IO\files")
cwd = os.getcwd()
print(cwd)

shelf_file = shelve.open("mydata")
shelf_file["data"] = ["Bassam",26,"Test Engineer","Penang"]
shelf_file.close()

# view the data create
shelf_file = shelve.open("mydata")
print(shelf_file["data"])
shelf_file.close()

# when view the actual file in txt editor, there will be some weird char, since the file is in binary 
# shelve module handle the reading of the data in binary file

# keys() and values() method in shelve module 

# keys example
shelf_file = shelve.open("mydata")
keys = shelf_file.keys() # will return keysview object
print("keys return : ",keys, " \ntype:",type(keys))
# can change to list if you want more readable result 
print("keys in list format : ",list(keys))
shelf_file.close()

#values example
shelf_file = shelve.open("mydata")
values = shelf_file.values() # will return keysview object
print("values return: ",values, " \ntype:",type(values))
# can change to list if you want more readable result 
print("values in list format : ",list(values))
shelf_file.close()
