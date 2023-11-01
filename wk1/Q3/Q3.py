#Q4
number_input = input('Enter an integer: ')
number_integer = int(number_input)
number_range = number_integer + 1
for i in range(1, number_range):

    if (i == number_integer):
        trailing = '.'
    elif (i % 4 == 0):
        trailing = ";"
    else:
        trailing = ","

    print(3 * i, end="")
    print(trailing, end="")
