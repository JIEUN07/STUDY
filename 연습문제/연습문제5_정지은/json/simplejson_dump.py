import json
data = {"name": "jane", "age": 17}
with open ('friends.json','w') as f:
    json.dump(data, f)
