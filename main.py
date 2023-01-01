import json

dic = '{"name": "Precious", "age": "16", "school": "ABC"}'

Person = json.loads(dic)
print("My name is", Person["name"])
print("I am", Person["age"], "years old")
print("The abbreviation of my school is", Person["school"])

List = '["apple", "mango", "grape", "pineapple"]'

lis = json.loads(List)
print("My favourite fruit is", lis[3])