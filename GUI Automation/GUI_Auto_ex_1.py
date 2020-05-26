import pyautogui

#get screen size - return tuple of int value (width and height)
#can be assign individually to variable like below code
width,height = pyautogui.size() 

#to get mouse position - return coordinate x,y in tuple
x,y = pyautogui.position()

#move mouse cursor 
#without duration specifies - the mouse move instantaneously
pyautogui.moveTo(100,100) 

#move mouse cursor 
#duration specifies - the mouse move linearly 
pyautogui.moveTo(400,100,duration=1.5) 

#move mouse relative to the current position
pyautogui.moveRel(400,800,duration=2.0)

#mouse click action 
pyautogui.click()

#mouse click action with x,y coordinate 
pyautogui.click(1100,231)