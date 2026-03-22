#lists, tuples, dictionaries, sets

#lists

fruits = ["Apple", "orange", "Banana", "Coconut"]
fruits.append("Mango")

print(fruits)
print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[3])
print(fruits[::-1]) #reverse the list
print(fruits[1:3]) #slicing the list

for x in fruits:
    print(x)


#print(dir(fruits))
#print(help(fruits))

print(len(fruits))