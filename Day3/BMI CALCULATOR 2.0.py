# BMI CALCULATOR 2.0
weight = input("Please enter weight: ")
height = input("Please enter height: ")
bmi = round(int(weight) / float(height) ** 2)
if bmi <= 18.5:
    print(f"Your BMI id {bmi}. You are under weight.")
elif bmi <= 25 :
    print(f"Your BMI id {bmi}. You have a normal weight.")
elif bmi <= 30:
    print(f"Your BMI id {bmi}. You are over weight.") 
elif bmi <= 35:
    print(f"Your BMI id {bmi}. You are over obese.") 
else:
    print("You are above 35. You are clinically abese.")