# Your friend has sent you a text file containing n lines. He sent a secret message with it, which tells you the place and time where you have to go and meet him.
# He challenges you to find it out without seeing the content of the file. 
# He has given hints to find it. Let’s surprise him by breaking the challenge with our python code.Hints to find the secret message: 
# 1.The number of lines in the file tells you the meeting time.Note:1<= number of lines <= 24If the number of lines isexceeding 12, you need to convert it to 12 hour format. For example, If the number of lines is15, then the meeting time is 3 PM. If the number of lines is10, then the meeting time is 10 AM.
# 2.The word appearing for the maximum number of times tells you the meeting place.Note:Meeting place will be a street name.For example,If the word Oxfordappears for the maximum number of times, then meeting place is Oxford Street.If the word Parkappears for the maximum number of times, then meeting place is Park Street

file=open("IO Operations\mini project\sample.txt",'r')
lines=file.readlines()
time=len(lines)
if time>12:
    time=str(time-12)+'PM'
else:
    time=str(time)+'AM'
freq={}
for i in lines:
    for word in i.split(" "):
        if word not in freq:
            freq[word]=1
        else:
            freq[word]+=1

count=[i for i in freq.values()]
st=max(count)
for key,value in freq.items():
    if value==st:
        street=key

print(f"time:{time}")
print(f"place:{street} street")