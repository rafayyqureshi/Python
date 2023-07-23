# # BMI CALCULATOR
weight = input("Please enter weight: ")
height = input("Please enter height: ")
bmi = int(weight) / float(height) ** 2
int_bmi = int(bmi)
print(int_bmi)