import json

with open('../secrets/test.json') as f:
    data = json.load(f)

def getParent(plate):
    '''
    Tries to match the license plate to a list of known license plates
    Returns the parent maching the license plate, false if the parent
    wasn't found
    '''
    try:
        return data[plate]
    except KeyError:
        return False

def getParentList():
    '''
    Returns a list of all parents (no license plates)
    '''
    parentList = set()
    for plate in data:
        parentList.add(str(data[plate]))
    return parentList

