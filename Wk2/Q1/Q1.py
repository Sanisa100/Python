#Q1
# input5
# ask more if in case
# well done
# sum of attempts
sum_attempt = 0

while True:
    letter_input = input('Please enter a five-letter word: ')

    if (len(letter_input) == 5) and (sum_attempt == 0):
        sum_attempt = sum_attempt + 1
        print('Well done! You have entered a five-letter word after {0} attempt!'.format(sum_attempt))
        break

    elif (len(letter_input) < 5):
        print('Not a five-letter word. Please enter again.')
        sum_attempt = sum_attempt+ 1
    else:
        sum_attempt = sum_attempt+ 1
        print('Well done! You have entered a five-letter word after {0} attempts!'.format(sum_attempt))
        break
