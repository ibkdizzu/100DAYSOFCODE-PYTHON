#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print('Welcone to the tip calculator')
bill = float(input('what was the total bill? $'))
pacint = int(input('What percentage tip will you like to give? 10,12 or 15? '))
count = int(input('How many people to split the bill? '))

convers = bill + (bill*(pacint / 100))
toeach = round(convers/count,2)
final_amount = "{:.2f}".format(toeach)
print(f'Each person to pay: ${final_amount}')
