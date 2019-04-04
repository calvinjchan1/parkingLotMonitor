import sys, time
import webcam, cmdTest, firebase

oldTime = time.time()
refreshCounter = 0
REFESH_TIME = 60 #Time between refreshes in seconds
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

def handleTime():
    global oldTime
    '''
    Returns delta time since last called
    '''
    dt = time.time()-oldTime
    oldTime = time.time()
    return dt

def handleRefresh():
    '''
    Handles refreshing data from server, call once per loop
    or don't - I don't care
    '''
    refreshCounter += handleTime()
    if(refreshCounter/1000>REFRESH_TIME):
        firebase.refreshPlateDict()
        refreshCounter = refreshCounter%(REFRESH_TIME*1000)
    

def main():
    while True:
        #Get data
        data, timeTaken = webcam.takePicture(85)
        print("NEW PLATE ------- " + str(timeTaken))
        plates = cmdTest.toList(data)
        #print(plates)
        for plate in plates:
            print(plate)
            if firebase.setLot(plate, mode): print("MATCH!")
        
main()
                
        
        
