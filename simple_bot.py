import pyautogui
from time import sleep
from random import randint

x = 50   #how many messages or comments you want to send

def name():
    """generates random names"""

    nameList = ["Baby Duck", "Fart Rocket", "Honey", "Snuggle Bunny", "Wifey", "Sweetie"]   #list of names (change according to your requirement)
    rand_name = nameList[randint(0, len(nameList) - 1)]      #traverse names randomly for n, from 0 to (n-1)

    return rand_name    #return the random name it just generated
 

def phrase():
    """generate random phrases"""

    phraseList = ["I love you ", "You are my ", "My precious little "]
    rand_phrase = phraseList[randint(0, len(phraseList) - 1)]

    return rand_phrase


while True:      #forever loop
    sleep(30)
    pyautogui.typewrite(f"{phrase()} {name()}", interval=0.25)  #type message
    #sleep(.600)
    sleep(60)                           #A bit delay of 60
    pyautogui.typewrite("enter")        #New line, here 'Enter' to send text
    sleep(10)                           #delay of 2 seconds

    x = x - 1         #decrement x value by 1

    if x == 0:       
        break         #get out of the loop and finish
