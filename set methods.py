b = {1, 8}
b.add(4)           #indexing doesnt work
b.add(7)
print(b)

#b.add([4,7,8])  #error u cnt add list or dict in set, bcz they both are mutable
b.add((4,7,8))  # tuple works bcz its unmutable
print(b)

print(len(b))

b.remove(4)
print(b)

b.pop()           #removes random elemnt
print(b)

b.clear    #empties the set

b.union

b.intersection