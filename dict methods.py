mydict = {
    1 : 'Books', 
    'Narmada': 'Programmer',
    'nesteddict' : {'Apple' : 'juice' } ,
    'day':'night'
}

                #dict overrides previous values

print(mydict.keys())
print(type(mydict.keys()))
print(mydict.values())
print(mydict.items())

updatedict = {
    'good' : 'friend',
    'Narmada': 'Coder'
}

mydict.update(updatedict)
print(mydict)

print(mydict.get('Narmada'))           
print(mydict['Narmada'])

#difference btwn .get and []syntax
print(mydict.get('Narmada2'))      #returns none
print(mydict['Narmada2'])      #throws error if item doesnt exist