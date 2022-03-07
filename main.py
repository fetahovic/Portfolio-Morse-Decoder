# Dictionary containing the morse code for all the letters and numbers created
symbols = {"A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.", "H": "....", "I": "..",
           "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.",
           "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--", "Z": "--..",
           "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....", "7": "--...",
           "8": "---..", "9": "----.", "0": "-----"}


# The function that it needs to decode
def get_key(symbol):
    for key, value in symbols.items():
        if symbol == value:
            return key
        elif symbol == "/":
            return " "


# The starting inputs are provided and while loop created
decoding = True

while decoding:
    direction = input("Would you like to 'Encode' or 'Decode'?").title()
    sentence = input("What would you like to translate?").upper()

    message = ""

    # Deciding on the direction and translating the message

    if direction == "Encode":
        for letter in sentence:
            if letter in symbols:
                message += f"{symbols[letter]} "
            elif letter == " ":
                message += "/ "
            else:
                print("Your input is invalid!")

    elif direction == "Decode":
        letter_list = sentence.split(" ")
        for letter in letter_list[:-1]:
            message += get_key(letter)

    print(message)
    restart = input("Would you like to decipher something else? Y or N").title()
    if restart == "N":
        decoding = False
