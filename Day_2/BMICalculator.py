# π¨ Don't change the code below π
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# π¨ Don't change the code above π

#Write your code below this lineπ
weight = float(weight)
height = float(height)
calc = weight / (height ** 2)
bmi = round(calc)
print(bmi)