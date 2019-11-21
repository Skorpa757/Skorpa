from random import randrange
Counter = 0
Answer = (randrange(10))
while True:

    Guess = int(input("What is your guess? "))
    Counter += 1
    print(f"Your guess is {Guess}")
    if Answer < Guess:
        print("Its a bit lower mate")
    if Answer > Guess:
        print("Its a bit higher mate")
    if Answer == Guess:
        print(f"Yes! Correct mate! It took you {Counter} times!")
        break
#Made by Teije // Skorpa 757 (Github) with love <3

