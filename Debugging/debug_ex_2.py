# traceback module to keep the log in log file .
# we can use traceback.format_exc() method to print the traceback error

import time
import traceback


try:
    raise Exception("This is error message")
except:
    log_file = open("log.txt","a")
    log_file.write("{} : {}".format(time.ctime(),traceback.format_exc()))
    log_file.close()
    print("Error is recorded in log.txt")
