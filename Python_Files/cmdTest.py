import subprocess
#Get raw data from alpr.exe
#raw = subprocess.check_output(['C:/users/obion/desktop/srp/dependencies/openalpr_32/alpr.exe', 'C:/users/obion/desktop/srp/samples/test4.jpg', '-p', 'az'])


def getData(raw):
    '''
    Returns an array of license plates detected by openALPR, each containing an array of openALPR's guesses, each of which is an array of 3 elements:
    ALL[Plate0[Guess0[str plateNumber, float Confidence, float pattern_match], Guess1], Plate1[Guess0['AFBSD', 90.534, 0]]]
    '''
    #Change data into a string from bytes
    #print(raw)
    raw = raw.decode('utf-8')
    print(raw)
    #print(type(raw))

    #Turn string into array
    data = []
    #Each Plate
    for index, item in enumerate(raw.split(' results\r\n')):
        if index != 0:
            #Break up the plate into guesses by "-" symbol
            plateList = item.split("-")
            plateList.pop(0)
            #print("------------------------------------------------------")
            plate = []
            #Each Guess
            for index, item in enumerate(plateList):
                #Turn each guess into a list containing the plate number, confidence, and pattern_match, in that order
                strList = item.split("\t")
                item = ['', '', '']
                item[0] = strList[0].split(' ')[1]
                item[1] = float(strList[1].split(" confidence: ")[1])
                item[2] = float(strList[2].split(" pattern_match: ")[1].split("\r")[0])
                #print(item)
                plate.append(item)
            #print(plate)
            data.append(plate)
    #print(data)
    return data
def scanPlate(path):
    '''
    Returns license plate scans from given path
    '''
    raw = subprocess.check_output(['../dependencies/openalpr_32/alpr.exe', path, '-p', 'az'])
    return getData(raw)

#print(scanPlate("C:/users/obion/desktop/srp/samples/test4.jpg"))
