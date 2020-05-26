import pyautogui, time
time.sleep(5)
#MS paint auto draw 
#need paint to be in the coordinate in below code , x=967 y=153
pyautogui.moveTo(967,153,duration=2)
pyautogui.click()    # click to put drawing program in focus
distance = 840
ms = 0.05
while distance > 0:
    #to drag mouse - use dragTo() and dragRel() method
    pyautogui.dragRel(distance, 0, duration=ms)   # move right
    distance = distance - 5
    pyautogui.dragRel(0, distance, duration=ms)   # move down
    pyautogui.dragRel(-distance, 0, duration=ms)  # move left
    distance = distance - 5
    pyautogui.dragRel(0, -distance, duration=ms)  # move up
