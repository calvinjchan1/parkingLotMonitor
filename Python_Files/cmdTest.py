import subprocess
#Get raw data from alpr.exe
raw = subprocess.check_output(['C:/users/obion/desktop/srp/dependencies/openalpr_32/alpr.exe', 'C:/users/obion/desktop/srp/samples/test4.jpg', '-p', 'az'])


def getData(raw):
    #Change data into a string
    #print(raw)
    raw = raw.decode('utf-8')
    print(raw)
    #print(type(raw))

    data = []
    for index, item in enumerate(raw.split(' results\r\n')):
        if index != 0:
            #Process data into a list
            plateList = item.split("-")
            #print(plateList)
            plateList.pop(0)
            #print("------------------------------------------------------")
            for index, item in enumerate(plateList):
                strList = item.split("\t")
                #print(strList)
                item = ['', '', '']
                item[0] = strList[0].split(' ')[1]
                item[1] = float(strList[1].split(" confidence: ")[1])
                item[2] = float(strList[2].split(" pattern_match: ")[1].split("\r")[0])
                plateList[index] = item
            data.append(plateList)
            #print(plateList)
            #print('\n')
    #print(len(data))
    for i in data:
        print(i[0])
    return data
getData(raw)
