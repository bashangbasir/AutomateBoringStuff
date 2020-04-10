# walking the directory tree 

import os
import shutil 

os.chdir(r"F:\AutomateBoringStuff\Files IO\files")

root_path = os.getcwd()
python_folder = os.path.join(root_path,"py")

for folder_name, sub_folders, filenames in os.walk(root_path):
    print("====================================================")
    print("Folder name is : ",folder_name) # the folder name 
    print("Subfolders are : ",sub_folders) # subfolder under the folder name - in list
    print("Filenames are : ",filenames)    # file under the folder name - in list 

    for sub_folder in sub_folders:
        #do something 
        if "fish" == sub_folder:
            #delete folder with the name fish
            try:
                os.rmdir(sub_folder)
            except:
                print("Error !")

    for filename in filenames:
        # do something
        if filename.endswith(".py"):
            try:
                shutil.move(os.path.join(folder_name,filename),python_folder)
            except:
                print("Error !")



    