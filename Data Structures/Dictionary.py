# 1 M Write a program to add a key and value to a dictionary. Sample Dictionary : {0: 10, 1: 20} Expected Result : {0: 10, 1: 20, 2: 30}
dict1= {0: 10, 1: 20}
key=int(input("Enter Key:"))
Value=int(input("Enter Value:"))
dict1[key]=Value
print(dict1)
print()
print()
# Dictionary 2 M Write a program to concatenate the following dictionaries to create a new one. Sample Dictionary : dic1={1:10, 2:20} dic2={3:30, 4:40} dic3={5:50,6:60} Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60} 
dic1={1:10, 2:20} 
dic2={3:30, 4:40}
dic3={5:50,6:60}
dict4=dict()
dict4.update(dic1)
dict4.update(dic2)
dict4.update(dic3)


print(dict4)
print()
print()
# Dictionary 3 M Write a program to check if a given key already exists in a dictionary.
key=int(input("Enter Key:")) 
if key in dict4.keys():
    print(True)
else:
    print(False)
    

print()
print()
# Dictionary 4 M Write a program to iterate over a dictionary using for loop and print the keys alone, values alone and both keys and values.
for key,value in dict4.items():
    print(f'key ->{key}')
    print(f'value ->{value}')
    print(f'{key} ->{value}')
    print()

print()
print()
# Dictionary 5 M Write a program to prepare a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of the keys.
dict5={i:i**2 for i in range(1,16) }
print(dict5)
print()
print()
# Dictionary 6 M Write a program to sum all the values in a dictionary, considering the values will be of int type.
dict5={i:i**2 for i in range(1,16) }
total=0
for i in dict5.values():
    total+=i

print(total)
print()