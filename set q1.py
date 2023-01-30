myDict = {
    'Pankha' : 'Fan',
    'kursi' : 'Chair',
    'Paani' : 'Water',
    'aata' : 'Flour'
}

print('Options are ', myDict.keys())
a = input('Enter the hindi word you want to search\n')
print('The meaning od entered wors is :', myDict[a])
print('The meaning od entered wors is :', myDict.get(a))
