from pynput.keyboard import Controller, Key
import time
import sys
keyboard = Controller()

def copyFunc():
    keyboard.press(Key.ctrl)
    keyboard.press('c')
    keyboard.release('c')
    keyboard.release(Key.ctrl)
    time.sleep(responseTime)

def pasteFunc():
    keyboard.press(Key.ctrl)
    keyboard.press('v')
    keyboard.release('v')
    keyboard.release(Key.ctrl)
    time.sleep(responseTime)

def tabForwardFunc():
    keyboard.press(Key.ctrl)
    keyboard.press(Key.tab)
    keyboard.release(Key.ctrl)
    keyboard.release(Key.tab)
    time.sleep(responseTime)

def tabBackwardFunc():
    keyboard.press(Key.ctrl)
    keyboard.press(Key.shift)
    keyboard.press(Key.tab)
    keyboard.release(Key.ctrl)  
    keyboard.release(Key.shift)
    keyboard.release(Key.tab)
    time.sleep(responseTime)

def tabFunc():
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    time.sleep(0.075)

def shiftTabFunc():
    keyboard.press(Key.shift)
    keyboard.press(Key.tab)
    keyboard.release(Key.shift)
    keyboard.release(Key.tab)
    time.sleep(0.075)

def downFunc():
    keyboard.press(Key.down)
    keyboard.release(Key.down)
    time.sleep(responseTime)

def upFunc():
    keyboard.press(Key.up)
    keyboard.release(Key.up)
    time.sleep(responseTime)

def rightFunc():
    keyboard.press(Key.right)
    keyboard.release(Key.right)
    time.sleep(responseTime)

def leftFunc():
    keyboard.press(Key.left)
    keyboard.release(Key.left)
    time.sleep(responseTime)

def ctrlLeftFunc():
    keyboard.press(Key.ctrl)
    keyboard.press(Key.left)
    keyboard.release(Key.left)
    keyboard.release(Key.ctrl)
    time.sleep(responseTime)

def enterFunc():
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(responseTime)

def spaceFunc():
    keyboard.press(Key.space)
    keyboard.release(Key.space)
    time.sleep(responseTime)

def altTabFunc():
    keyboard.press(Key.alt)
    keyboard.press(Key.tab)
    keyboard.release(Key.alt)
    keyboard.release(Key.tab)
    time.sleep(responseTime)

def deleteFunc():
    keyboard.press(Key.delete)
    keyboard.release(Key.delete)
    time.sleep(responseTime)

def selectAllFunc():
    keyboard.press(Key.ctrl)
    keyboard.press('A')
    keyboard.release('A')
    keyboard.release(Key.ctrl)
    time.sleep(responseTime)

def setAnswer(n,resetPosition=True):
    for i in range(0,2):
        #3 times ----- Tab 22 times
        tabFunc()       
    spaceFunc()
    for i in range(0,n):
        tabFunc()
    spaceFunc()
    for i in range(0,6-n):
        tabFunc()
    enterFunc()
    if resetPosition==True:
        for i in range(0,15):
            tabFunc()

async def asyncInputFunc(message):
    return int(input(message))

#START
inputList = []
n = 0
responseTime = 0.1   

while True:
    val = int(input("Enter Number, Enter -1 to start"))
    if val==-1:
        x=len(inputList)
        break 
    inputList.append(val)
# x=int(input("Number of questions"))
# for j in range(0,x):
#     inputList.append(int(input("Enter Number")))

# for j in range(0,x):
#     print(inputList.pop(0))

print(inputList)
# sys.exit(0)

time.sleep(5)
while x>0:
    copyFunc()
    tabForwardFunc()
    pasteFunc()
    tabFunc()
    tabFunc()
    tabFunc()
    
    #Clearing Options
    for i in range(0,4):
        deleteFunc()
        tabFunc()
        tabFunc()
        tabFunc()
    for i in range(0,12):
        shiftTabFunc()

    for i in range(0,4):
        tabBackwardFunc()
        rightFunc()
        copyFunc()
        tabForwardFunc()
        pasteFunc()
        #if i!=1:
        tabFunc()
        tabFunc()
        tabFunc()


    # tabBackwardFunc()
    # rightFunc()
    # rightFunc()
    # copyFunc()
    # tabForwardFunc()
    # altTabFunc()
    # time.sleep(5)
    # pasteFunc()
    # enterFunc()
    # altTabFunc()
    
    prev = n
    n=inputList.pop(0)

    if n<5 and n>0:
        setAnswer(n)
    
    for i in range(0,3):
        #3 times ----- Tab 22 times
        tabFunc()  

    enterFunc()
    time.sleep(1.25)
    deleteFunc()

    #REMOVE PREVIOUS ANSWER
    if n<5 and n>0:
        for i in range(0,15):
            tabFunc()
        setAnswer(n,False)
        time.sleep(responseTime)

    tabBackwardFunc()
    downFunc()
    ctrlLeftFunc()
    rightFunc()     
    x-=1