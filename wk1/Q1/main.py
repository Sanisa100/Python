#Q1
name = input("Enter your first name: ")
surname = input("Enter your last name: ")
date = input("Enter your dob (DD-MM-YYYY): ")
format = input("Choose a format:  (Abb) Abbreviated  (Norm) Normal: ")

print('{:<15}  {:<15}  {:<15}'.format("First Name","Last Name", "Date of Birth"))

#cal date
date_s = date.split("-")
day = date_s[0]
month = date_s[1]
year = date_s[2]
month_dict = {"1":"Jan","2":"Feb","3":"Mar","4":"Apr","5":"May","6":"Jun","7":"Jul","8":"Aug","9":"Sep","10":"Oct","11":"Nov","12":"Dec"}

if(format == "Abb"):
    print('{:<15}  {:<15}  {:<15}'.format(name,surname, day+"/"+month_dict[month]+"/"+year))
elif(format == "Norm"):
    print('{:^15}  {:^15}  {:^15}'.format(name,surname, date))
else:
    print('{:^15}  {:^15}  {:<15}'.format(name,surname, year+"-"+month+"-"+day)) 
