#L Calculator

print("Welcome to L calculator!")

name1 = input("Please enter first name: ")
name2 = input("Please enter second name: ")

name1 = name1.lower()
name2 = name2.lower()

# Name 1 count 

T = name1.count("t")
R = name1.count("r")
U = name1.count("u")
E = name1.count("e")
L = name1.count("l")
O = name1.count("o")
V = name1.count("v")
E = name1.count("e")

# Name 2 count

t = name2.count("t")
r = name2.count("r")
u = name2.count("u")
e = name2.count("e")
l = name2.count("l")
o = name2.count("o")
v = name2.count("v")
e = name2.count("e")

tt = int(T) + int(R) + int(U) + int(E) + int(t) + int(r) + int(u) + int(e)
ll = int(L) + int(L) + int(O) + int(V) + int(l) + int(o) + int(v) + int(e)

t1 =  tt
l1 = ll

z1 = str(t1) + str(l1)
y1 = int(z1)
int(y1)

# print(z1)

if y1 <= 10 or y1 >= 90 :
    print(f"Your score is {y1}. you go togather like coke and mentos.")
if y1 >= 40 and y1 <= 50 :
    print(f"Your score is {y1}. you are alright togather.")
else:
    print(f"Your score is {y1}.")

