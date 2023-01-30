mydict = {
    1 : 'Books', 
    'Narmada': 'Programmer',
    'nesteddict' : {'Apple' : 'juice' } 
}

print(mydict)
print(mydict['Narmada'])
print(mydict['nesteddict'])

print(mydict['nesteddict']['Apple'])

mydict['Narmada']=['Developer']
print(mydict['Narmada'])