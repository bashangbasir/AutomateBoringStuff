# in this excercise, we learn about delete files
# two ways to delete file 
# 1. use os.unlink() method

import os 
import shutil

cwd = os.getcwd()
path_file = os.path.join(cwd,"Files IO\\files_backup\\1.jpg")
path_dir = os.path.join(cwd,"Files IO\\files_backup\\example")

#delete a file
os.unlink(path_file)

#delete a dir 
#need dir to be empty
os.rmdir(path_dir)

# second way - use shutil module 
# delete an entire dir tree (no need to be empty dir as os.rmdir() method)
# need to be care since it will delete as we run this code  
shutil.rmtree(r"path_to_delete")
