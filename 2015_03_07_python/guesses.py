from random import randint

# Generates a number from 1 through 10 inclusive
random_number = randint(1, 10)

guesses_left = 3
# Start your game!
while guesses_left >  0:
    num = randint(1, 6)
    guess = int(raw_input("Your guess:"))
    if guess == num:
        print "You win!"
        break
    guesses_left -= 1
else:
    print "Sorry, you lose!"

