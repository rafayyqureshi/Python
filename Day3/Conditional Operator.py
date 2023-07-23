#Conditional Operator / if / else

print("Welcome to the rollercoaster!")
height = int(input("Please enter your height in cm: "))
bill = 0
if height >= 120:
    print("You can ride the rollercoaster.")
    age = int(input("Enter your age: "))
    if age < 12:
        bill = 5
        print("Please pay $5")
    elif age <18:
        bill = 7
        print("Please pay $7")
    else:
        bill = 12
        print("Please pay $12")


    photo = input("Do you want a photo taken? Y or N: ")
    if photo == "Y":
        bill += 3

        print(f"Your final bill is {bill}.")


else:
    print("Sorry, you need to grow taller before you can ride.")