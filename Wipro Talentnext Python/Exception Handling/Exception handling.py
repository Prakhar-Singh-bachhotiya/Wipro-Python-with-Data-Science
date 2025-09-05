#  Write a program to accept two numbers from the user and perform division. If any exception occurs, print an error message or else print the result.
try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = num1 / num2
    print("Result:", result)
except Exception as e:
    print("Error:", e)

#  Write a program to accept a number from the user and check whether it’s prime or not. If user enters anything other than number, handle the exception and print an error message.
try:
    n = int(input("Enter a number to check if it's prime: "))
    if n < 2:
        print("Not a prime number")
    else:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                print("Not a prime number")
                break
        else:
            print("Prime number")
except Exception as e:
    print("Error:", e)


#  Write a program to accept the file name to be opened from the user, if file exist print the contents of the file in title case or else handle the exception and print an error message.

try:
    filename = input("Enter the file name to open: ")
    with open(filename, "r") as f:
        contents = f.read()
        print(contents.title())
except Exception as e:
    print("Error:", e)
# #  Declare a list with 10 integers and ask the user to enter an index. Check whether the number in that index is positive or negative number. If any invalid index is entered, handle the exception and print an error message.
try:
    nums = [12, -7, 5, -3, 9, 0, -2, 8, 4, -6]
    index = int(input("Enter an index (0-9): "))
    value = nums[index]
    if value > 0:
        print("Positive number")
    elif value < 0:
        print("Negative number")
    else:
        print("Zero")
except IndexError:
    print("Error: Invalid index entered.")
except Exception as e:
    print("Error:", e)