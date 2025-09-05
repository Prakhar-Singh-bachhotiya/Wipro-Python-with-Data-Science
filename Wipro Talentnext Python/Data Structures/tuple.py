# Write a program to print the 4th element from first and 4th element from last in a tuple. Tuple	
t1=(1,2,3,4,5,6,7,8,9,10)
print(t1[3])

print(t1[len(t1)-4])
print()
print()
# 2	M Write a program to check whether an element exists in a tuple or not.
t1=(1,2,3,4,5,6,7,8,9,10)
el=int(input("Enter Element:"))
if el in t1:
    print(True)
else:
    print(False)

print()
print()
# 3	M Write a program to convert a list into a tuple.
l1=[1,2,3,4,5,6,7,8,8]
t2=tuple(l1)
print(t2)
print()
# 4	M Write a program to find the index of an item in a tuple.
t1=(1,2,3,4,5,6,7,8,9,1,4,0)
el=int(input("Enter Element:"))
for i in range(len(t1)):
    if t1[i]==el:
        print(i)
        
print()
print()
# 5	M Write a program to replace last value of tuples in a list to 100. 
# Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)] 
# Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]
t1=[(10, 20, 40), (40, 50, 60), (70, 80, 90)]
t2=[]
for i in t1:
    l1=list(i)
    l1[-1]=100
    t2.append(tuple(l1))

print(t2)
print()
