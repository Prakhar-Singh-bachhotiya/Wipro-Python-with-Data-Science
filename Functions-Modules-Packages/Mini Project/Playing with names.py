# Create a Python module with the following functions:
# Function Name                
# ispalindrome(name)-
#  Given the user name as input, this function should tell us whether the name is a palindrome or not.
# count_the_vowels(name)-
# Given the user name as input, this function should tell us howmany vowels are present in it.
# frequency_of_letters(name)-
# Given the user name as input, this function should tell us how many times each letter appears in the name.
def ispalindrome(name):
    rev=name[-1::-1]
    if name==rev:

        print('Palindrome')
    else:
        print('Not a Palindrome')

def count_the_vowels(name :str):
    vowels='aeiou'
    count=0
    name=name.lower()
    for i in name:
        if i in vowels:
            count+=1
        
    print(count)

def frequency_of_letters(name: str):
    freq={}
    for i in name:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    print(freq)

name= 'bob'
frequency_of_letters(name)
count_the_vowels(name)
ispalindrome(name)