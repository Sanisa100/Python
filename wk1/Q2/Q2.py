#Q2
#input
fruit1 = input("Which kind of apples would you like: Royal Gala/Jonagold: ")
if(fruit1 == "Royal Gala" or fruit1 == "Jonagold"):
    fruit1_w = input("How many kilograms of apples would you like: ")
    fruit1_w = float(fruit1_w)
fruit2 = input("Which kind of oranges would you like: Valencia/Maltese: ")
if(fruit2 == "Valencia" or fruit2 == "Maltese"):
    fruit2_w = input("How many kilograms of oranges would you like: ")
    fruit2_w = float(fruit2_w)
fruit_dict ={"Royal Gala":4.99,"Jonagold":5.99,"Valencia":2.99,"Maltese": 3.99}

#print
print('{:>15}{:>15}{:>15}{:>15}'.format("Item","Weight", "Unit Price","Price"))

fruit1_price =0.00
if(fruit1 == "Royal Gala"):
    fruit1_price = float("{:.2f}".format(fruit_dict[fruit1]* float(fruit1_w)))
    print('{:>15}{:>15}{:>15}{:>15}'.format(fruit1,fruit1_w, str(fruit_dict[fruit1]),str(fruit1_price)))
elif(fruit1 == "Jonagold"):
    fruit1_price = float("{:.2f}".format(fruit_dict[fruit1]* float(fruit1_w)))
    print('{:>15}{:>15.1f}{:>15}{:>15}'.format(fruit1,fruit1_w, str(fruit_dict[fruit1]),str(fruit1_price)))
else:
    print('{:>15}{:>15}{:>15}{:>15}'.format("-","0", "0","0.00"))

fruit2_price =0.00
if(fruit2 == "Valencia" or fruit2 == "Maltese"):
    fruit2_price = float("{:.2f}".format(fruit_dict[fruit2]* float(fruit2_w)))
    print('{:>15}{:>15}{:>15}{:>15}'.format(fruit2,fruit2_w, str(fruit_dict[fruit2]),str(fruit2_price)))
else:
    print('{:>15}{:>15}{:>15}{:>15}'.format("-","0", "0","0.00"))
Total_price = float('{:.2f}'.format(fruit1_price+fruit2_price))
print('{:>15}{:>15}{:>15}{:>15.2f}'.format("Total","", "",Total_price))
