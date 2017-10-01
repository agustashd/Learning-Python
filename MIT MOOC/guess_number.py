print("Please think of a number between 0 and 100!")
low, high = 0, 100
guess = int((low + high) / 2)
while True:
    print("Is your secret number",guess ,"?")
    print("Enter 'h' to indicate the guess is too high. Enter 'l'", end="")
    y = input("to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if y == "h":
        high = guess
    elif y == "l":
        low = guess
    elif y == "c":
        break
    else:
        print("Sorry, I did not understand your input.")
    guess = int((low + high) / 2)

print("Game over. Your secret number was:", guess)