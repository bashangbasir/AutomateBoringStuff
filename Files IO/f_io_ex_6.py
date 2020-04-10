# copy/move files in can be done by using shutil module (read as shell utilities module) 

import shutil

#copy single file 
shutil.copy(r"./Files IO/files/test1.txt",r"./Files IO/files/example")

#copy entire folder/directory
shutil.copytree(r"./Files IO/files/",r"./Files IO/files_backup")

#move file to other destination.
shutil.move(r"./Files IO/files/test2.txt",r"./Files IO/files/example")

# to rename file , we use move() method but change name for the destination
shutil.move(r"./Files IO/files/example/test2.txt",r"./Files IO/files/example/test3.txt")