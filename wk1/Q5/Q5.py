#Q5
integer_starting = input('Enter the starting integer: ')
starting = int(integer_starting)
integer_ending = input('Enter the ending integer: ')
ending = int(integer_ending)
for i in range(starting, ending+1):
    if (starting<=ending) and (i == starting):
        print('{0:<10}{1:<10}{2:>10}'.format('Num', 'Double', 'Triple'))
        for i in range(starting, ending + 1):
            if (starting<=ending):
                print('{0:<10}{1:<10}{2:>10}'.format(i, i*2, i*3))
if (starting>ending):
    print('Your starting integer is larger than ending integer.')
