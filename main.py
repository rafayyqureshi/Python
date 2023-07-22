                                        # DAY1

# Python print code
# print("Hello World: ")

# Python Variable

# name = input("What is Your Name: ")
# length = len(name)
# print(length)

# Switch Values

# a = input("a= ")
# b = input("b= ")

# c = a
# a = b
# b = c

# print("a= ", a)
# print("b= ", b)

# Band Name Generator

# name = input("What is your name? \n")

# city = input("what is your city name? \n ")

# print("Your band name could be " + name + " " + city)


                                            # DAY2

# Data TYPES

# STRINGS

# print("Hello"[0])

# Float

# 12.3343

# Boolean 
# True 
# False      Capital T and F

# Type checking and type conversion

# num_char = len(input("What is your name? "))
# new_num_char = str(num_char)
# print("Your name have "+new_num_char+" characters.")

# Types

# a = 13
# print(type(a))

# a = float(123)
# print(type(a))

# print(70 + float("100.5"))
# print(str(123)+str(321))

# # Add two digit number

# two_digit_number = input("Enter two digit number: ")
# one = two_digit_number[0]
# two = two_digit_number[1]
# print(int(one) + int(two))

# Matgimatical Operations in Python

# print(3-2)
# print(4+1)
# print(4/2)[]
# print(2**3)

# PEMDAS
# ()
# **
# *
# /
# +
# -
# print(3*3+3/3-7)
# print("3.0")

# # BMI CALCULATOR
# weight = input("Please enter weight: ")
# height = input("Please enter height: ")
# bmi = int(weight) / float(height) ** 2
# int_bmi = int(bmi)
# print(int_bmi)

#Number Manipulation and F String in PYTHON

# print(8/3)  # 2.66666666666665
# print(int(8/3)) # 2
# print(round(8/3)) # 2.6 = 3
# print(8//3) # 2

# score = 0
# score += 1 #  -= , /=  , *= 
# print(score)

# # f string

# # score = 10
# # height = 1.8
# # winning = True

# # print(f"your score in {score}, your height is {height} and your winning is {winning}")

# Life in Weeks

# max_age = 90
# age = input("Please enter your age: ")
# days = int(max_age) - int(age)
# d= days * 365
# weeks = int(max_age) - int(age)
# w = weeks * 52
# months = int(max_age) - int(age)
# m = months * 12

# print(f"You have {d} days, {w} weeks and {m} months.")

# Tip Calculator

# percentage = 100
# print("Welcome to the tip calculator.")
# bill = input("What is your total bill? $")
# tip = input("What percentage tip would you like to give 10, 12 or 15?")
# split = input("How many people to split the bill? ")

# tip_cal = float(bill) / int(percentage) * int (tip)
# split_cal = float(tip_cal) / int(split)
# bill_cal = float(bill) / int(split)
# total_bill = float(bill_cal) + float(split_cal)
# final_amount = "{:.2f}".format(total_bill, 2) # round(totall_bill,2)
# print(f"Each person should pay ${final_amount}") 

                                            # Day3

#Conditional Operator / if / else

# print("Welcome to the rollercoaster!")
# height = int(input("Please enter your height in cm: "))
# bill = 0
# if height >= 120:
#     print("You can ride the rollercoaster.")
#     age = int(input("Enter your age: "))
#     if age < 12:
#         bill = 5
#         print("Please pay $5")
#     elif age <18:
#         bill = 7
#         print("Please pay $7")
#     else:
#         bill = 12
#         print("Please pay $12")


#     photo = input("Do you want a photo taken? Y or N: ")
#     if photo == "Y":
#         bill += 3

#         print(f"Your final bill is {bill}.")


# else:
#     print("Sorry, you need to grow taller before you can ride.")
    
#Modulo

# num = input("Enter any number: ")
# modulo = int(num) % 2
# if modulo == 0:
#     print("Nmber is even")
# else:
#     print("Number is odd")


# BMI CALCULATOR 2.0
# weight = input("Please enter weight: ")
# height = input("Please enter height: ")
# bmi = round(int(weight) / float(height) ** 2)
# if bmi <= 18.5:
#     print(f"Your BMI id {bmi}. You are under weight.")
# elif bmi <= 25 :
#     print(f"Your BMI id {bmi}. You have a normal weight.")
# elif bmi <= 30:
#     print(f"Your BMI id {bmi}. You are over weight.") 
# elif bmi <= 35:
#     print(f"Your BMI id {bmi}. You are over obese.") 
# else:
#     print("You are above 35. You are clinically abese.")


# # Leap Year
# year = int(input("Enter Year: "))
# if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
#     print("It's a leap year.")
# else:
#     print("Not a leap year.")

# Pizza ordering

# print("Welcome to python Pizza!")

# size = input("What size of pizza do you want? S , M , L : ")
# add_papperoni = input("Do you want to add Papperoni? Y or N : ")
# extra_cheese = input("Do you want extra cheese? Y or N: ")

# if size == "S" and add_papperoni != "Y" and extra_cheese != "Y":
#     print("Your final bill is $15.")

# elif size == "S" and add_papperoni == "Y" and extra_cheese != "Y":
#     print("Your final bill is $17 of Small pizza with papperoni")

# elif size == "S" and add_papperoni == "Y" and extra_cheese == "Y":
#     print("Your final bill is $17 of Small pizza with papperoni and extra cheese.")

# if size == "M" and add_papperoni != "Y" and extra_cheese != "Y":
#     print("Your final bill is $20.")

# elif size == "M" and add_papperoni == "Y" and extra_cheese != "Y":
#     print("Your final bill is $23 of Medium pizza with papperoni")

# elif size == "M" and add_papperoni == "Y" and extra_cheese == "Y":
#     print("Your final bill is $23 of Medium pizza with papperoni and extra cheese.")

# if size == "L" and add_papperoni != "Y" and extra_cheese != "Y":
#     print("Your final bill is $25.")

# elif size == "L" and add_papperoni == "Y" and extra_cheese != "Y":
#     print("Your final bill is $28 of Large pizza with papperoni")

# elif size == "L" and add_papperoni == "Y" and extra_cheese == "Y":
#     print("Your final bill is $28 of Large pizza with papperoni and extra cheese.")

#L Calculator

# print("Welcome to L calculator!")

# name1 = input("Please enter first name: ")
# name2 = input("Please enter second name: ")

# name1 = name1.lower()
# name2 = name2.lower()

# # Name 1 count 

# T = name1.count("t")
# R = name1.count("r")
# U = name1.count("u")
# E = name1.count("e")
# L = name1.count("l")
# O = name1.count("o")
# V = name1.count("v")
# E = name1.count("e")

# Name 2 count

# t = name2.count("t")
# r = name2.count("r")
# u = name2.count("u")
# e = name2.count("e")
# l = name2.count("l")
# o = name2.count("o")
# v = name2.count("v")
# e = name2.count("e")

# tt = int(T) + int(R) + int(U) + int(E) + int(t) + int(r) + int(u) + int(e)
# ll = int(L) + int(L) + int(O) + int(V) + int(l) + int(o) + int(v) + int(e)

# t1 =  tt
# l1 = ll

# z1 = str(t1) + str(l1)
# y1 = int(z1)
# int(y1)

# # print(z1)

# if y1 <= 10 or y1 >= 90 :
#     print(f"Your score is {y1}. you go togather like coke and mentos.")
# if y1 >= 40 and y1 <= 50 :
#     print(f"Your score is {y1}. you are alright togather.")
# else:
#     print(f"Your score is {y1}.")

