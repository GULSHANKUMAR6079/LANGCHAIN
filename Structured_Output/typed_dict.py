from typing import TypedDict
class Person(TypedDict):
    name:str
    age:int
new_person:Person={"name":"Gulshan kumar","age":"Twenty One"}
print(new_person)