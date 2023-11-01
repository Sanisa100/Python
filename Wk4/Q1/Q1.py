#Q1
#Welcome to the e-mail repository
#1: Look up an entry
#2: Add an entry
#3: Delete an entry
#4: Update an entry
#Q: Exit the program
#1          Please select the operation you want to perform (1/2/3/4/Q): 1
#Juliana Helan          Enter the name: Juliana Helan
#The e-mail for Juliana Helan is jhelan@gmail.com
#2          Please select the operation you want to perform (1/2/3/4/Q): 2
#Steaven Johanson       Enter the name: Steaven Johanson
#sjohanson@yahoo.com    Enter the e-mail: sjohanson@yahoo.com
#A new entry is made as Steaven Johanson:sjohanson@yahoo.com
#3          Please select the operation you want to perform (1/2/3/4/Q): 3
#Mitchel Michael        Enter the name: Mitchel Michael
#No record exists against Mitchel Michael
#3          Please select the operation you want to perform (1/2/3/4/Q): 3
#Steaven Johanson       Enter the name: Steaven Johanson
#The record for Steaven Johanson has been deleted
#4          Please select the operation you want to perform (1/2/3/4/Q): 4
#Juliana Helan          Enter the name: Juliana Helan
#jhelan@gmail.com       Enter the updated e-mail: jhelan@gmail.com
#The record for Juliana Helan has been updated
#s          Please select the operation you want to perform (1/2/3/4/Q): s
#Please enter the correct choice
#Q          Please select the operation you want to perform (1/2/3/4/Q): Q

email_repository={"Johan Smith": "jsmith@gmail.com", "Michael Clarke": "mclarke@hotmail.com", "Juliana Helan": "jhelan@gmail.com"}

print('Welcome to the e-mail repository')
print('1: Look up an entry')
print('2: Add an entry')
print('3: Delete an entry')
print('4: Update an entry')
print('Q: Exit the program')

while True:
    operation = input('Please select the operation you want to perform (1/2/3/4/Q): ')
    if operation == '1':
        name = input('Enter the name: ')
        keys = email_repository.keys()
        check = 1
        for i in keys:
            if name == i:
                print('The e-mail for '+ name + ' is ' + str(email_repository.get(name)))
                check = 0
                break
        if check:
            print('No record exists against ' + name)
    elif operation == '2':
        name = input('Enter the name: ')
        mail = input('Enter the e-mail: ')
        email_repository[name] = mail
        print('A new entry is made as ' + name + ':' + mail)
    elif operation == '3':
        name = input('Enter the name: ')
        keys = email_repository.keys()
        check = 1
        for i in keys:
            if name == i:
                del email_repository[name]
                print('The record for ' + name + ' has been deleted')
                check = 0
                break
        if check:
            print('No record exists against ' + name)
    elif operation == '4':
        name = input('Enter the name: ')
        mail = input('Enter the updated e-mail: ')
        keys = email_repository.keys()
        check = 1
        for i in keys:
            if name == i:
                email_repository[name] = mail
                print('The record for ' + name  + ' has been updated')
                check = 0
                break
        if check:
            print('No record exists against ' + name)
    elif operation == 'Q':
        break
    else:
        print('Please enter the correct choice')
a