# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line👇
weight = float(weight)
height = float(height)
calc = weight / (height ** 2)
bmi = round(calc)
print(bmi)