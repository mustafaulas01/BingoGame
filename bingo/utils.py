import random

user_card_rows = []
computer_card_rows = []


bingo_numbers = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21,
    22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
    41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59,
    60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78,
    79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90
]


def abstact_number(number):
  bingo_numbers.remove(number)


def get_number_from_package():
  if len(bingo_numbers) > 0:
    return random.choice(bingo_numbers)
  else:
    print("There is no any number in package")
    return -1


def check_user_card_update(number, user):
  global userwin_count
  global computerwin_count
  
  if user:
    for item in user_card_rows:
      if number in item:
        item[item.index(number)] = "✅"
        
        print("Well done the number is exist on your card")
  else:
    for item in computer_card_rows:
      if number in item:
        item[item.index(number)] = "✅"

        print("the number is exist on computer card")


  
  
  if user:
    card = f"""------------------------------------------------------------------ 
    | {user_card_rows[0]}                                                       

    | {user_card_rows[1]}                                                        

    | {user_card_rows[2]}                                                            
    ------------------------------------------------------------"""
  else:
    card = f"""------------------------------------------------------------------ 
    | {computer_card_rows[0]}                                                       

    | {computer_card_rows[1]}                                                        

    | {computer_card_rows[2]}                                                            
    ------------------------------------------------------------"""

  return card
    



def emptylist_create():
  numbers = []
  for j in range(4):
    index = random.randint(0, 8)
    if index not in numbers:
      numbers.append(index)
    else:
      index = random.randint(0, 8)
    if index not in numbers:
      numbers.append(index)
    else:
      index = random.randint(0, 8)

  numbers.sort()
  return numbers


def clean_list(list):
  for item in list:
    if item == -1:
      list.remove(item)
  return list


def get_bingo_number():
  random.shuffle(bingo_numbers)
  return random.choice(bingo_numbers)


def create_bingo_card(numbers, user):
  numbers.sort()

  first = numbers[0:5]
  second = numbers[5:-5]
  third = numbers[-5:]

  first_row = arrange_numbers(first)
  second_row = arrange_numbers(second)
  third_row = arrange_numbers(third)

  if user:
    user_card_rows.append(clean_list(first_row))
    user_card_rows.append(clean_list(second_row))
    user_card_rows.append(clean_list(third_row))
  else:
    computer_card_rows.append(first_row)
    computer_card_rows.append(second_row)
    computer_card_rows.append(third_row)

  #print(f"First Row : {first_row}")
  #print(f"Second Row : {second_row}")
  #print(f"Third Row : {third_row}")

  card = f"""------------------------------------------------------------------ 
          | {first_row}                                                       
                                                                              
          | {second_row}                                                        
                                                                              
          | {third_row}                                                            
          ------------------------------------------------------------"""

  return card


def arrange_numbers(numbers):
  counter = 5

  first_row = [-1, -1, -1, -1, -1, -1, -1, -1, -1]
  for i in range(9):
    if counter > 0:
      if first_row[i] == -1:
        first_row[i] = numbers[i]
        counter = counter - 1

  #random.shuffle(first_row)
  newlist = []
  emptyIndexList = emptylist_create()

  for m in range(9):
    if m in emptyIndexList:
      newlist.insert(m, "⚫")
    else:
      newlist.insert(m, -1)

  counterforemptyIndex = 0
  for numb in newlist:
    if numb != "⚫":
      newlist[counterforemptyIndex] = first_row[0]
      first_row.pop(0)
    else:
      newlist[counterforemptyIndex] = "⚫"

    counterforemptyIndex = counterforemptyIndex + 1
  first_row = []
  emptyIndexList = []
  counterforemptyIndex = 0
  return newlist
