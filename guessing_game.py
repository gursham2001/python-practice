# allows users to enter inputs until they guess the mystery word,
# we only give three guesses

# we need to create a variable to store the secret word
secret_word = 'jassi'
# we need to create a variable to store the answers of the user
guess = ''
# we want to limit guesses so we need three variables a guess counter (how many times user has guessed), a guess limit and a boolean of out_of_guesses
guess_count = 0
guess_limit = 3
# we set this to false as when it turns to true lives have been exceeded
out_of_guesses = False

# we create a while loop checking if guesses = secret word and if we are not out of guesses as this will mean the loop continues if the user has not guessed correctly and lives have not been exceeded
while guess != secret_word and not(out_of_guesses):
    # we now need an if statement to see if guess count is bigger than the limit
    if guess_count < guess_limit:
        # we then want to prompt user to input guess and increment a guess onto guess count each loop
        guess = input("enter a guess: ")
        guess_count += 1
    # we now ser our guess to true as an else so game stops
    else:
        out_of_guesses = True

# now there is two scenarios we need to send messages back to the user on being out_of guesses and the other being you win

if out_of_guesses:
    print("out of guesses Unlucky")
else:
    print("You guessed correct!")
