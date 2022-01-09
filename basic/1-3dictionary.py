#dictionary
Person = {
  "name" : "ilgon",
  "age" : 26,
  "hobby" : ["music","game"],
  "korean" : True
}

print(Person)
Person["Cool"]=True
print(Person)
Person["age"]+=23
print(Person)
Person["hobby"].append("아아아")
print(Person)