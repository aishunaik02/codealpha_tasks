import random

words = ["python", "computer", "program", "coding", "college"]

word = random.choice(words)
guessed_letters = []
wrong_guesses = 0
max_wrong = 6

print("Welcome to Hangman!")

while wrong_guesses < max_wrong:
    display = ""

    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)
    print("Wrong guesses:", wrong_guesses, "/", max_wrong)

    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct!")
    else:
        wrong_guesses += 1
        print("Wrong guess!")

    if all(letter in guessed_letters for letter in word):
        print("\n🎉 You won! The word was:", word)
        break
else:
    print("\nGame over! The word was:", word)
