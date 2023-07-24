import random

namestr = input("Give me everybody name, seperted by comma. ")
name = namestr.split(",")
# num_item = len(name)
# random_choice = random.randint(0, num_item)
person_who_will_pay = random.choice(name)
print(person_who_will_pay + " is going to buy a meal today.")

