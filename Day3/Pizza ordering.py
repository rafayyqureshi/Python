# Pizza ordering

print("Welcome to python Pizza!")

size = input("What size of pizza do you want? S , M , L : ")
add_papperoni = input("Do you want to add Papperoni? Y or N : ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

if size == "S" and add_papperoni != "Y" and extra_cheese != "Y":
    print("Your final bill is $15.")

elif size == "S" and add_papperoni == "Y" and extra_cheese != "Y":
    print("Your final bill is $17 of Small pizza with papperoni")

elif size == "S" and add_papperoni == "Y" and extra_cheese == "Y":
    print("Your final bill is $17 of Small pizza with papperoni and extra cheese.")

if size == "M" and add_papperoni != "Y" and extra_cheese != "Y":
    print("Your final bill is $20.")

elif size == "M" and add_papperoni == "Y" and extra_cheese != "Y":
    print("Your final bill is $23 of Medium pizza with papperoni")

elif size == "M" and add_papperoni == "Y" and extra_cheese == "Y":
    print("Your final bill is $23 of Medium pizza with papperoni and extra cheese.")

if size == "L" and add_papperoni != "Y" and extra_cheese != "Y":
    print("Your final bill is $25.")

elif size == "L" and add_papperoni == "Y" and extra_cheese != "Y":
    print("Your final bill is $28 of Large pizza with papperoni")

elif size == "L" and add_papperoni == "Y" and extra_cheese == "Y":
    print("Your final bill is $28 of Large pizza with papperoni and extra cheese.")