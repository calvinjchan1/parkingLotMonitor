import json

with open('../secrets/test.json') as f:
    data = json.load(f)

print(data)
