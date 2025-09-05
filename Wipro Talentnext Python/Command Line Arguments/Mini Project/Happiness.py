# Throughcommand line arguments three strings separated by space aregiven to you. Eachstring is a series of numbersseparated by hyphen(-). You like all the numbers in string 1 and dislike all the numbers in string 2.Third string contains thenumbers given to you. Your initial happiness is 0.
#  When you encounter anumberwhich is present in string 1, add 1 to yourhappiness, if it is present in string 2, add -1 to your happiness.Otherwise, your happiness does not change. Output your final happiness at the end.

from sys import argv
s1=argv[1]
s2=argv[2]
s3=argv[3]

l1=s1.split('-')
l2=s2.split('-')
l3=s3.split('-')

happy=0
for i in range(len(l3)):
    if l3[i] in l1:
        happy+=1
        
    elif l3[i] in l2:
        happy=happy-1
    
print(happy)