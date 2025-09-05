txt=input('Enter a word')
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

