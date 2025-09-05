#  Write a program to read the entire content from a txt file and display it to the user.
with open('IO Operations/mini project/sample.txt', 'r') as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]
    print(lines)
print()
print()
print()
#  Write a program to read first n lines from a txt file. Get n as user input.
n=int(input('Enter number of lines : '))
lines=[]
with open('IO Operations/mini project/sample.txt', 'r') as file:
    for i in range(n):
        line=file.readline()
        lines.append(line)
lines=[line.strip() for line in lines]
print(lines)	
print()	
print()	
#  Write a program to accept input from user and append it to a txt file.

txt=input("Enter Text:")
with open('IO Operations/mini project/sample.txt', 'a+') as file:
    file.write(txt)
    file.seek(0)  # Move pointer to the beginning
    lines = file.readlines()
    lines = [line.strip() for line in lines]

print(lines)
print()
print()
#  Write a program to read contents from a txt file line by line and store each line into a list.
with open('IO Operations/mini project/sample.txt', 'r') as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]

print(lines)
print()
print()
#  Write a program to find the longest word from the txt file contents, assuming that the file will have only one longest word in it.
max_word = ''
max_len = 0
with open('IO Operations/mini project/sample.txt', 'r') as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]
    for line in lines:
        for word in line.split():
            if len(word) > max_len:
                max_word = word
                max_len = len(word)

if max_word:
    print(max_word)
else:
    print("No words found in the file.")
print()
print()
# #  Write a program to count the frequency of a user entered word in a txt file.

txt=input('Enter a word:')
file=open('IO Operations/mini project/sample.txt', 'r')
lines=file.readlines()
count=0
lines=[line.strip() for line in lines]
for line in lines:
    for word in line.split():
        if word==txt:
            count+=1
print(count)
file.close()

