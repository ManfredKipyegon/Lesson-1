#Dictionaries are used to store data in pair form. Dictionaries use curly braces
#data types like integers, floasts, strings, booleans 
cars = {
    "model": "Ford",    #commas are important in moving to the next item
    "year" : 1964

}
cars.update ({"year" : 1920})

print(cars.get("model"))
for x in cars :
    print(cars[x])