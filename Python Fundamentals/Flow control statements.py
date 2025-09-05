# Q1. Write a program to check if a given number is Positive, Negative or Zero.

num=int(input("Enter A Number: "))
if num ==0:
    print("Zero")
elif num>0:
    print("Positive")
elif num<0:
    print("Negative")

# Q2. Write a program to check if a given number is odd or even.
num=int(input("Enter A Number: "))
if num %2==0:
    print("Even Number")
else:
    print("Odd Number")

# Q3. # Given two non-negative values, print true if they have the same last digit, such as with 27 and 57
num1=int(input("Enter First Number: "))
num2=int(input("Enter Second Number: "))

if num1%10==num2%10:
    print("True")
else:
    print("False")

#  Q4. Write a program to print numbers from 1 to 10 in a single row with one tab space.
for i in range(1,11):
    print(i,end="   ")   

# Q5. Write a program to print even numbers between 23 and 57. Each number should be printed in a seperate row.
for i in range(23,57):
    if i%2==0:
        print(i)

# Q6. Write a program to check if a given number is prime or not.
num=int(input("Enter A Number: "))
check=1
for i in range(2,num//2+1):
    if num% i == 0:
        check=0
if check:
    print(f"{num} is Not Prime Number")
else:
    print(f"{num} isPrime Number")

# Q7. Write a program to print prime numbers between 10 and 99.
for num in range(10,99):
    check=1
    for i in range(2,num//2+1):
        if num% i == 0:
            check=0
            break
    if check:
        print(num, end=" ")
        
# Q8. Write a program to print the sum of all the digits of a given number.
num=int(input("Enter A Number: "))
sum=0
while num>9:
    last=num%10
    sum+=last
    num=num//10
sum+=num
print(sum)


# Q9. Write a program to reverse a given number and print.
num=int(input("Enter A Number: "))
reverse=0
while num>0:
    last=num%10
    reverse=reverse*10+last
    num=num//10
print(reverse)

# Q10. Write a program to find if the given number is palindrom or not.

# method 1 using reverse of anumber
num=int(input("Enter A Number: "))
org=num
reverse=0
while num>0:
    last=num%10
    reverse=reverse*10+last
    num=num//10
num=org
if num==reverse:
    print("Palindrome")
else:
    print("Not a Palindrome")
    print(reverse)

# Method-2 Using string and 2 pointers:

num=int(input("Enter A Number: "))
num_str=str(num)
check=1
start=0
end=len(num_str)-1
while start<=end:
    if num_str[start]!=num_str[end]:
        check=0
    start+=1
    end-=1
if check:
    print("Palindrome")
else:
    print("Not a Palindrome")