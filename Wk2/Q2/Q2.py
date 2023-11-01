#Q2
#input
#run 5 times
#e : end
#evenLen : Upper
#elseLen: Lower

round_count = 0
while (round_count <5):
    word_input = input('Enter a word (or e to exit): ')
    if (len(word_input) %2 == 0):
        print('The UPPERCASE of {0} is {1}'.format(word_input, word_input.upper()))
        round_count = round_count + 1
    elif (word_input == 'e'):
        print('Loop is terminated.')
        break
    else:
        print('The lowercase of {0} is {1}'.format(word_input, word_input.lower()))
        round_count = round_count + 1
