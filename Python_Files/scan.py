import sys
import webcam

#Get what mode we are running the program in
#a True mode is entrance, false is exit
mode = input("Do you want to run in \"Entrance\" or \"Exit\" mode?\n")
mode = mode.upper()
if mode == "ENTRANCE":
    mode = True
elif mode == "EXIT":
    mode = False
else:
    print("Invalid mode, aborting.")
    sys.exit()
