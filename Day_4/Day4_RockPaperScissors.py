import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
#Write your code below this line 👇
images = [rock, paper, scissors]
guest_play = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n "))

if guest_play >= 3 or guest_play < 0 :
  print("Choice invalid, you lose")
else:
  print(images[guest_play])
  
  comp_play = random.randint(0,2)
  print('Computer chose: ')
  print(images[comp_play])
  
  
  
  if guest_play == comp_play: 
    print("It's a draw")
  elif guest_play == 0 and comp_play == 2:
    print("You win!")
  elif guest_play == 2 and comp_play == 0:
    print("You lose")
  elif guest_play < comp_play:
    print("You lose")
  elif guest_play > comp_play:
    print("You win")
  


  

