#  Write a program to count the number of upper and lower case letters in a String.
s1='ABCdefGHIjkl'
lower=upper=0
for i in s1:
    if i.isupper():
        upper+=1
    elif i.islower():
        lower+=1
print(f"The count of uppercase is {upper} and the count of Lowercase is {lower}")	
print()	
print()	
#  Write a program that will check whether a given String is Palindrome or not.
s2='abcdedcbaf'
check=True
left=0
right=len(s2)-1
while(left<=right ):
    if s2[right]!=s2[left]:
        check=False
        break
    right-=1
    left+=1
print(check)


print()
print()
print()
#  Given a string, return a new string made of n copies of the first 2 chars of the original string where n is the length of the string. The string length will be >=2. 
# If input is "Wipro" then output should be "WiWiWiWiWi".
s3=input("enter a string:")
s4=s3[0:2]
s4=s4*len(s3)
print(s4)

print()
print()
print()
#  Given a string, if the first or last character is 'x', return the string without those 'x' character, else return the string unchanged. If the input is "xHix", then output is "Hi".
s3=input("enter a string:")
if s3[0]!=s3[len(s3)-1]!='x':
    print('unchanged')
else:
    print(s3[1:len(s3)-1])
print()
print()
print()
#  Given a string and an integer n, return a string made of n repetitions of the last n characters of the string. You may assume that n is between 0 and the length of the string inclusive. For example if the inputs are “Wipro” and 3, then the output should be “propropro”.
s3=input("enter a string:")
n=int(input(f"Enter a number (0-{len(s3)-1}):"))
rep=s3[-n:]
rep=rep*n
print(rep)