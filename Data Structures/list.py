# List 1 Write a program to create a list of 5 integers and display the list items. Access individual elements through index. 


arr=list(map(int,input().split()))
print(arr)
for i in range(len(arr)):
    print(f'Element at index {i} is {arr[i]}')

print()
print()

# List 2 M Write a program to append a new item to the end of the list. 
new=int(input("Enter element to add to the list: "))
arr.append(new)
print(f"Element {new} is added to the list")
print(arr)

print()
print()

# List 3 M Write a program to reverse the order of the items in the list. 
reverse_arr=arr.reverse()
print(arr)

print()
print()

# List 4 M Write a program to print the number of occurrences of a specified element in a list. 
arr=[1,2,3,4,1,5,1,2,3]
el=int(input("Enter Element:"))
count=0
for i in arr:
    if i==el:
        count+=1
print(count)
print()
print()

# List 5 M Write a program to append the items of list1 to list2 in the front.
# method1
list1=[1,2,3,4,5]
list2=[6,7,8,9,10]
list1.extend(list2)
print(list1)
#method2
list1=[1,2,3,4,5]
list2=[6,7,8,9,10]
list2=list1+list2
print(list2)
print()
print()

# List 6 M Write a program to insert a new item before the second element in an existing list.
list6=[1,3,4,5,6,7]
el=int(input("enter element:"))
pos=int(input(f"enter position (0-{len(list6)-1}):"))
list6.insert(pos,el)
print(list6)
print()
print()

# List 7 M Write a program to remove the item from a specified index in a list.
list7=[1,3,4,5,6,7] 
idx=int(input("enter index:"))
list7.pop(idx)
print(list7)
print()
print()

# List 8 M Write a program to remove the first occurrence of a specified element from a list.
list6=[1,1,2,3,3,4,5,6,7]
el=int(input("enter element:"))
for i in range(len(list6)):
    if list6[i]==el:
        list6.pop(i)
        break
print(list6)

print()
print()
