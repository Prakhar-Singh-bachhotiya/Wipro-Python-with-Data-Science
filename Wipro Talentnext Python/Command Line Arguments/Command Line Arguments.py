# # Write a program to accept two numbers as command line arguments and display their sum.
from sys import argv
num1=int(argv[1])
nums2=int(argv[2])
print(num1+nums2)	
print()	
print()	
# #  Write a program to accept a welcome message through command line arguments and display the file name along with the welcome message.
wel=argv[1]
file=argv[0]
print(f"{wel}----{file}")
print()
print()
#  Write a program to accept 10 numbers through command line arguments and calculate the sum of prime numbers among them.
from sys import argv
def isprime(n:int):
   
    if n<=1:
        return False
    elif n==2:
        return True
    elif n%2==0:
        return False
    else:
        for i in range(3,int(n**.5)+1,2):
            if n%i==0:
                return False
    return True
nums=[int(argv[i]) for i in range(1,len(argv))]
total=0
for i in range(len(nums)):
    if isprime(nums[i]):
        total+=nums[i]
print(total)