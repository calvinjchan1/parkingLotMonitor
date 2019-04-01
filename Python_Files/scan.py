import sys
import webcam, cmdTest, listReader, firebase

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

def main():
    while True:
        #Get data
        data, timeTaken = webcam.takePicture(85)
        print("NEW PLATE ------- " + str(timeTaken))
        plates = cmdTest.toList(data)
        #print(plates)
        for plate in plates:
            #Make sure parent exists
            print(plate)
            parent = listReader.getParent(plate)
            if(parent != False):
                print("Match!")
                #Entrace
                if(mode):
                    firebase.setParent(parent, True)
                #Exit
                else:
                    firebase.setParent(parent, False)
main()
                
        
        
