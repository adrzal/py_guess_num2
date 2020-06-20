import random

number = random.randint(1, 20)
print("Hello what's your name?")
name = input()
print(f"Well {name}, I am thinking fo a number between 1 and 20")

for guess_taken in range(1, 7):
    #print(number)
    guess = int(input())

    if(guess < number):
        print("number is bigger")
    elif(guess > number):
        print("number is smaller")
    else:
        break

if(guess == number):
    print(f"Good job {name}, you guess my number in {guess_taken} attempts")
else:
    print(f"sorry my number was: {number}")
