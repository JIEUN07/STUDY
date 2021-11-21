import json

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def toJson(self):
        '''
        Serialize the object custom object
        '''
        return json.dumps(self, default=lambda o: o.__dict__,
            sort_keys=True, indent=4)
p1 = Person("Lucy", 23)
p2 = Person("Thomas", 29)

people = []
people.append(json.loads(p1.toJson()))
people.append(json.loads(p2.toJson()))

json_data = json.dumps(people)

print(repr(json_data))

# '[{"age": 23, "name": "Lucy"}, {"age": 29, "name": "Thomas"}]'
