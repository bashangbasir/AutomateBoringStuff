# send2trash module - module that delete file/dir to the OS trashbin
# this module can help user from delete the file permenantly.
# Since os module and shutil module the the file permenantly from the harddrive.

import send2trash

# delete any file/dir to recycle bin 

path = "any path to delete"
send2trash.send2trash(path)