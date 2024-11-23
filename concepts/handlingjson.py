#!/usr/bin/python3
import json

data = {
    "person1": {
        'name': 'John',
        'age': 20,
        'gender': 'male',
    },
    "person2": {
        'name': 'Jane',
        'age': 20,
        'gender': 'female',
    },
}
# Json serialization
with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)

json_data = json.dumps(data)
print(json_data)

# Json deserialization
with open('data.json', 'r') as file:
    loaded_data = json.load(file)

# my_data = json.loads(loaded_data)
print(loaded_data)
