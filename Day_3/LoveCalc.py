# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
concat = (name1 + name2).lower()
T = concat.count('t')
R = concat.count('r')
U = concat.count('u')
E = concat.count('e')
A = T + R + U + E
L = concat.count('l')
O = concat.count('o')
V = concat.count('v')
E = concat.count('e')
B = L + O + V + E
#print(f"T occurs {T} times")
#print(f"R occurs {R} times")
#print(f"U occurs {U} times")
#print(f"E occurs {E} times")
#print(f"Total = {A}")
#print(f"L occurs {L} times")
#print(f"O occurs {O} times")
#print(f"V occurs {V} times")
#print(f"E occurs {E} times")
#print(f"Total = {B}")
LS = f"{A}{B}"
#print(f"Love Score = {LS}")
check = int(LS)
if check < 0 or check > 90:
    print(f"Your score is {LS}, you go together like coke and mentos.")
elif check >= 40 and check <= 50:
    print(f"Your score is {LS},  you are alright together.")
else:
    print(f"Your score is {LS}")