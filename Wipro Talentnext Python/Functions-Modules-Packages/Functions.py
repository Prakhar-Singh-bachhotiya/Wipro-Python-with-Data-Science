# 1. Write a function to return the sum of all numbers in a list.
def sum_list(numbers):

    return sum(numbers)

# 2. Write a function to return the reverse of a string.
def reverse_string(s):

    return s[::-1]

# 3. Write a function to calculate and return the factorial of a number (a non-negative integer).
def factorial(n):

    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# 4. Write a function that accepts a string and prints the number of upper case letters and lower case letters in it.
def count_case(s):

    upper = sum(1 for c in s if c.isupper())
    lower = sum(1 for c in s if c.islower())
    print(f"Upper case letters: {upper}")
    print(f"Lower case letters: {lower}")

# 5. Write a function to print the even numbers from a given list. List is passed to the function as an argument.
def even_numbers(numbers:list):

    return [num for num in numbers if num % 2 == 0]

# 6. Write a function that takes a number as a parameter and checks whether the number is prime or not.
def is_prime(n):

    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True