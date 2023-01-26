# name=input('Enter your name:\n')
# print('Good Afternoon,', name)


letter='''Dear, <|name|>
Greetings from Microsoft
Iam happy to let you know about your selection,
you are a selected!
Have a great day!

Thanks and regards,
Microsoft
date: <|date|>'''

name=input('Enter your name:\n')
date=input('Enter Date:\n')
letter=letter.replace('<|name|>', name)
letter=letter.replace('<|date|>', date)
print(letter)
