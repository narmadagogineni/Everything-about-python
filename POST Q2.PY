# #CHECK IF THIS POST IS TALKING ABOUT NARMADA

# post = ['narmada', 'Narmada', 'NARMADA', 'NaRmAdA']
# name = input('Enter the word\n')

# if name in post:
#     print('Yes, This post is taling about Narmada')
# else:    
#     print('No, This post is not taling about Narmada')

post = 'NarmaDa is walking in the park'
case_insensitive = post.casefold()

if 'narmada' in case_insensitive:
    print('yes, this post is talking about narmada')
else:
    print('no, this post is not talking about narmada')    