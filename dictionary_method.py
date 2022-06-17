car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change
print(car)

x = car.values()
print(x)

print("this is item",car.items())   # item return the pair in tuple

car.update({"color":"red"})   # add/ update data in dic
print(car)

car["price"]=450000     # add one more to dict
print(car)

car.pop("model")     # remove req. from dict
print(car)

car.popitem()
print("this is popitem",car)   # reemove last element from dict

del car["brand"]      # this removes req key:value pair from dict
print( "this is delet", car)

for x, y in car.items():
  print(x, y)

mydict = dict(car)
print("this is copy of car",mydict)

# car.clear()
# print("this is empty dict", car)

x = car.get("year")

print("this is get",x)

x = car.keys()

print("this is key ",x)

z=car.values()
print("this is value ",z)

x = ('key1', 'key2', 'key3')
y = 0

thisdict = dict.fromkeys(x, y)

print(thisdict)

# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
#
# car.update({"color":"red"})
#
# print(car)
#
# car.popitem()
#
# print(car)