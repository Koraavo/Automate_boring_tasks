#! python3 # she bang
import re
import pyperclip
# pyperclip allows you to copy data and use that data
# without having to create a new file of the pasted data

# create a regex for phone numbers
phoneregex = re.compile(r'''
# 415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext.12345, x12345
(
(\d{3}[.-])?\d{3}[.-]\d{4}
((ext(\.?) | x)?
\d*?)?
)
''', re.VERBOSE)

# create a regex for emails
# some_something@something.com
emailregex = re.compile(r'''
[a-zA-Z0-9_.+]+ # name part
@               #@symbol
[a-zA-Z0-9_.+]+ # domain name part

''', re.VERBOSE)
# get text off the clipboard
text=pyperclip.paste()
# extract email addresses and phone numbers from this text
extractedphone = phoneregex.findall(text)
extractedmail = emailregex.findall(text)

phonenumbers= []
for i in extractedphone:
    phonenumbers.append(i[0])

for i in range(len(phonenumbers)):
    result = phonenumbers[i] + "|" + extractedmail[i]
    print(result)
# pyperclip.copy(result)