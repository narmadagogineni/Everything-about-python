from collections import Counter

a = [2,2,2,2,5,6,7,8,8,9,4,4,6,7,9,9,9,9]
count = Counter(a)
print(count)
print(list(count.elements()))
print(count.most_common())

#to substract
sub = {9: 2, 5 : 1}
print(count.subtract(sub))
print(count.most_common())
