magic_word = "please"

while True:
    word = input("Say the magic word: ")

    if word == "":
        print("You didn't say anything!")
        continue

    if word == "quit":
        print("Game ended.")
        break

    if word == magic_word:
        print("Gate opened!")
        break
    else:
        print("Wrong!")
