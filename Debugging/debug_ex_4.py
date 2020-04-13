import logging
# to disable the log module entirely
#code:
#logging.disable(logging.CRITICAL)

# log level {debug,info,warning,error,critical}
# disable can be done according to level
# ex : logging.disable(logging.CRITICAL) - will disable Critical,error,warning,info,debug
#      logging.disable(logging.WARNING) - will disable Warning,info and debug

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# to write the log in the log file 
# this will create a txt file with the log inside, the file will be locate in the cwd.
#code:
#logging.basicConfig(filename="logging.txt",level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


def factorial(n):
    total = 1
    
    for i in range(1,n+1): # error here , which i start at 0. Causing the total become 0. to fix, we need to range start with 1.
        total = total * i
        logging.debug("i is %s, total is %s " % (i,total))
    
    logging.debug("Return value is %s" % (total))
    return total

print(factorial(4))

logging.debug("end of program !")

