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
