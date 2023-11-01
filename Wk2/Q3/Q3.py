#Q3
def operate_2_numbers(number1, number2, operator):
    if(operator == '+'):
        result = number1 + number2
    elif(operator == '-'):
        result = number1 - number2
    elif(operator == 'x'):
        result = number1 * number2
    else:
        result = number1 // number2
    return result
result = operate_2_numbers(2,5,"+")
print(result)
