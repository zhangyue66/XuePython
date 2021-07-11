import time
import os


print("You can press any key to exit!")
counter = True
content = " Seattle Like Yue Zhang"

#print(len(content))

#print(content[1])

length = len(content)

try:
    while counter:
        #os.system('cls')
        for number in range(0,length):
            time.sleep(0.2)
            print(content[number],end = '')

    #if os.system("pause"):
        #counter = False
except KeyboardInterrupt:
    pass