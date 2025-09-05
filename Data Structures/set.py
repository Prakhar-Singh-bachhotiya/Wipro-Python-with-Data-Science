#  Write a program to remove a given item from the set.
s1={1,2,3,4,5}
s1.remove(1)
print(s1)
print()

#  Write a program to create an intersection of sets.
s1={1,2,3,4,5}
s2=[3,4,5,6,7]
s3=s1.intersection(s2)
print(s3)
print()
#  Write a program to create an union of sets.
s1={1,2,3,4,5}
s2=[3,4,5,6,7]
s3=s1.union(s2)
print(s3)
print()
print()
#  Write a program to find the maximum and minimum value in a set.
maximum=max(s3)
minimum=min(s3)
print(maximum)
print(minimum)