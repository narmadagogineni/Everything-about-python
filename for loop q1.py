num = int(input("enter the num"))

for i in range(11):
    #print(str(num) + ' X ' + str(i) + ' = ' + str(num*i))

    # using f string
    print(f'{num} X {i} = {num*i}')