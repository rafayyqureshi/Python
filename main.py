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

# BMI CALCULATOR
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

percentage = 100
print("Welcome to the tip calculator.")
bill = input("What is your total bill? $")
tip = input("What percentage tip would you like to give 10, 12 or 15?")
split = input("How many people to split the bill? ")

tip_cal = float(bill) / int(percentage) * int (tip)
split_cal = float(tip_cal) / int(split)
bill_cal = float(bill) / int(split)
total_bill = float(bill_cal) + float(split_cal)
final_amount = "{:.2f}".format(total_bill, 2) # round(totall_bill,2)

print(f"Each person should pay ${final_amount}")

