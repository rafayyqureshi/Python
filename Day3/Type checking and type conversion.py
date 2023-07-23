# Type checking and type conversion

num_char = len(input("What is your name? "))
new_num_char = str(num_char)
print("Your name have "+new_num_char+" characters.")

# Types

a = 13
print(type(a))

a = float(123)
print(type(a))

print(70 + float("100.5"))
print(str(123)+str(321))