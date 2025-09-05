import re

# 1. Check if a string has only octal digits
strings = ['789', '123', '004']
for s in strings:
    if re.fullmatch(r'[0-7]+', s):
        print(f"{s} is octal")
    else:
        print(f"{s} is not octal")
print()
print()

# 2. Extract user id, domain name and suffix from email addresses
emails = """zuck@facebook.com
sunder33@google.com
jeff42@amazon.com"""
for email in emails.splitlines():
    match = re.match(r'([\w\d]+)@([\w\d]+)\.(\w+)', email)
    if match:
        print(f"User: {match.group(1)}, Domain: {match.group(2)}, Suffix: {match.group(3)}")
print()
print()

# 3. Split the irregular sentence into proper words
sentence = "A, very   very; irregular_sentence"
words = re.split(r'[;,\s_]+', sentence)
print(' '.join(words))
print()
print()

# 4. Clean up the tweet
tweet = '''Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats'''
cleaned = re.sub(r'(RT|cc:)|@\w+|http\S+|#\w+|[^\w\s]', '', tweet)
print(' '.join(cleaned.split()))
print()
print()

# 5. Extract all text portions between HTML tags
import requests
r = requests.get("https://raw.githubusercontent.com/selva86/datasets/master/sample.html")
html = r.text
results = re.findall(r'>([^<>]+)<', html)
cleaned_results = [text.strip() for text in results if text.strip()]
print(cleaned_results)
print()
print()

# 6. Identify words that begin and end with the same character
words = ['civic', 'trust', 'widows', 'maximum', 'museums', 'aa', 'as']
for word in words:
    if re.match(r'^(.).*\1$', word):
        print(word)
# filepath: c:\Users\lenovo\Desktop\STUDY\wipro python training\Regular