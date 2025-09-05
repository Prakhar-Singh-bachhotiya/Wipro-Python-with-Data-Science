# Write a LC program to create an output dictionary which contains only the odd numbers that are present in the input list = [1,2,3,4,5,6,7] as keys and their cubes as values
l1=[1,2,3,4,5,6,7]
l2={i:i*i*i for i in l1 if i%2!=0}
print(l2)

#  Make a dictionary of the 26 english alphabets mapping each with the corresponding integer

alpha={i:ord(i)-ord('a')+1 for i in 'abcdefghiklmnopqrstuvwxyz'}
print(alpha)