text = input('Enter the text\n')

if('make a lot of money' in text):
    spam = True
elif('buy this now' in text):
    spam= True
elif('subscribe this' in text):
    spam = True 
elif('click this' in text):
    spam = True
else:
    spam = False

if (spam):
    print('this is spam')
else:
    print('this is not spam')                     