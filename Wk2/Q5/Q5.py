#Q5
# def power_calculation(F, S = 'default')
# return (integer, str, str) -->> F^S, sign, parity)

def power_calculation(first_number, second_number= 2):
    power = (first_number)**(second_number)
    if (power > 0):
        sign = 'positive'
        if (power % 2 == 0):
            parity = 'even'
    elif (power == 0):
        sign = 'zero'
        parity = 'even'
    else:
        sign = 'negative'
        if (power % 2 != 0):
            parity = 'odd'
    return power, sign, parity

power, sign, parity = power_calculation(0,8)
print("{} is a {} {} number.".format(power, sign, parity))

