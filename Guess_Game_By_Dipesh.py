from random import randint

print('''
************************************************
* Guess the number correctly within 1 to 100   *
* Three Difficulty levels with valid range     *
* Easy    : 1 - 20                             *
* Medium  : 1 - 50                             *
* Hard    : 1 - 100                            *
*                                              *
* Rules:                                       *
* 1. You will get three chances only to guess. *
* 2. Number should be within the valid range.  *
* 3. Minus(-) values are not allowed           *
*                                              *
****************Lets, Begin !!!*****************
''')

difficulty = input("Choose Difficulty Level : ")
attempts = 3
if difficulty == 'Easy':
  number = randint(1,20)
elif difficulty == 'Medium':
  number = randint(1,50)
elif difficulty == 'Hard':
  number = randint(1,100)
else:
  print("Choose Proper Difficulty Level : ")

while attempts > 0:
  user_number = int(input("Guess the number: "))
  if user_number == number:
    print("\nCongratulations ! You have guessed the number correctly.")
    break
  elif user_number < 0:
    print("Number is out of valid range.")
    attempts = attempts - 1
    print("-------------------------")
    print(f"{attempts} attemps left")
    print("-------------------------")  
  elif difficulty == 'Easy' and user_number > 20:
    print("Number is out of valid range.")
    attempts = attempts - 1
    print("-------------------------")
    print(f"{attempts} attemps left")
    print("-------------------------")
  elif difficulty == 'Medium' and user_number > 50:
    print("Number is out of valid range.")
    attempts = attempts - 1
    print("-------------------------")
    print(f"{attempts} attemps left")
    print("-------------------------")
  elif difficulty == 'Hard' and user_number > 100:
    print("Number is out of valid range.")
    attempts = attempts - 1
    print("-------------------------")
    print(f"{attempts} attemps left")
    print("-------------------------")
  elif user_number != number and attempts > 0:
    if user_number > number and user_number - number < 30:
      print("You are close. Put a lower number.")
    elif number > user_number and number - user_number < 30:
      print("You are close. Put a higher number")
    attempts = attempts - 1
    print("-------------------------")
    print(f"{attempts} attemps left")
    print("-------------------------")
if attempts == 0:    
  print("\nSorry! You couldn't guess the number")
  print(f"Correct number was '{number}'")