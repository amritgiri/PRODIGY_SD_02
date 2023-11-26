import random
import math
# taking input
lowerBound = int(input("Enter the lower bound: "))
upperBound = int(input("Enter the upper bound: "))

# generating random number
GuessResultCheck = random.randint(lowerBound, upperBound)

print("\n\t you have only ", round(math.log(upperBound - lowerBound +1, 2)), " chances to guess the integer\n")

print(GuessResultCheck)

count = 0

while (count) < math.log(upperBound-lowerBound+1,2):
    count +=1

    guess = int(input("Guess a number: "))

    if GuessResultCheck == guess:
        print("CONGRATULATION you did it in ", count, " try")
        break
    elif GuessResultCheck > guess:
        print("You guessed too small !\n")
    elif GuessResultCheck < guess:
        print("You guessed to large !\n")



if (count) >= (math.log(upperBound - lowerBound + 1, 2)):
    print("\nThe number is ", GuessResultCheck)
    print("\n BETTER LUCK NEXT TIME.....")
