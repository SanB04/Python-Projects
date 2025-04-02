import art
import random

print(art.logo)
print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100.")
rand_num=random.randint(1,101)
difficulty=input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

# print(rand_num)
attempts=0

if difficulty=='easy':
    attempts=10
elif difficulty=='hard':
    attempts=5
else:
    print("Invalid")

while attempts!=0:
    print(f"You have {attempts} remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if rand_num == guess:
        print(f"You got it! The answer was {rand_num}")
        break
    else:
        attempts -= 1
        if rand_num > guess:
            print("Too low..")
        elif rand_num < guess:
            print("Too high..")