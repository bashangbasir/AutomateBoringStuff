
# as previously , we know how to handle exception provided by python when some anomalies within in. 
# here , we will learn to raise our own exception with custom message. 
# 

def box_print(symbol, width, height) :
    
    if len(symbol) != 1:
        raise Exception("'Symbol' parameter need to be string of length 1 only")
    if (width<2) or (height<2):
        raise Exception("Width and Height parameter need to be more than 2")

    print(symbol * width)
    for i in range(height-2): # minus 2 since the upper and lower height is deducted
        print(symbol + (' '*(width-2)) + symbol)
    print(symbol * width)

#first case (pass case - no raise issue)
box_print("*", 3, 3)

#2nd case (raise issue implement)
try:
    box_print("**", 3, 3) #symbol with length of 2 is passed
except Exception as e:
    print(e)

#3rd case (raise issue implement)
try:
    box_print("*", 1, 1) #symbol with length of 2 is passed
except Exception as e:
    print(e)