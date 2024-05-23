import random

def roll():
    minValue = 1
    maxValue = 6

    roll = random.randint(minValue, maxValue)

    return roll

print("Welcome to PIG!")

while True:
    players = input("Enter the number of players (2 to 4): ")

    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break

        else:
            print("Must be between 2 - 4, try again")

    else:
        print("Invalid input, try again")

maxScore = 50
playerScores = [0 for _ in range(players)] #list comprehension - creates the amount of elements in list

while max(playerScores) < maxScore:
    
    for playerIndex in range(players):

        print("\nIt is player ", playerIndex + 1 , "turn\n")
        currentScore = 0

        while True:
            shouldRoll = input("Would you like to roll (y or n)? ")
            if shouldRoll.lower() != "y":
                break

            value = roll()
            if value == 1:
                currentScore = 0
                print("You rolled a 1! Turn done!")
                break

            else:
                currentScore += value
                print("You rolled a ", value)

            print("Your score is: ", currentScore)
        
        playerScores[playerIndex] += currentScore
        print("Your total score is: ", playerScores[playerIndex])

maxScore = max(playerScores)
winnningIndex = playerScores.index(maxScore)
print("Player number ", winnningIndex + 1, "wins!\n")




