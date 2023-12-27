import random
#from ecommerce.utils import find_max
from bingo.utils import abstact_number, get_bingo_number, create_bingo_card, get_number_from_package, check_user_card_update


def new_card():

  numbers = []
  for i in range(15):
    num = random.randint(1, 90)
    if num not in numbers:
      numbers.append(num)
    else:
      num = random.randint(1, 90)
      numbers.append(num)

  numbers.sort()
  return numbers


print("----------------------------Game Guide----------------------------")
print("1. You will be given a bingo card with 15 numbers.")
print("2. You will get a card ,If you want you can get more than 1 card ")
print("3.Computer will choice a card")
print("4.Computer will shuffle the numbers than it will get a number")
print("5.You are going to check if the numer is exists on your card")
print("-------------------------------------------------------------------")
print("Enter Your name : ")
name = input()
accept = "n"

account_card = []

while accept == "n":
  numbers = new_card()
  account_card.append(numbers)
  print(create_bingo_card(numbers, True))


  print(
    "Do You accept your Cards or want to change ? (Accept => y , Change => n)")
  accept = input()
  accept.lower()
  if accept == "n":
    print("You did not start Game")
  else:
    print(f"Congartulations {name} !!! You have choosen your card")


  



#print(f"Your cards : {account_card}")
account_computer = new_card()
print("-------------------------------------------------------------------")
print("Start Game  Yes=>y No=>n ")
answear = input()
while answear == "y":
  if answear.lower() == "y":
    choice_number = get_number_from_package()
    abstact_number(choice_number)
    print(
        "........................................................................"
    )
    print(f"A number has been choosen from the package : {choice_number}")
    print(
        "........................................................................"
    )
    print()

    print(
        f"---------------------Your Updated Card {name}  -------------------------------"
    )
    print()
    print(check_user_card_update(choice_number, True))
    print()
    print()

    print()
    print()
    computer_number = new_card()

    print(
        "---------------------Computer Updated Card -------------------------------"
    )
    print()
    create_bingo_card(computer_number, False)
    print()
    print(check_user_card_update(choice_number, False))
    print()
    print()
    print()
    print("Do you want to continue ? Yes=>y No=>n")
    answear = input()

#print(f"{create_bingo_card(numbers)}")
