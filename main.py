ON = True
MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-', " ": "/", "": " "}


def convertor(string):  # Converts given string to morse code or morse code to string
    translated_word = ""
    if string[0].isalnum():  # Checks whether the input is morse code or not
        for letter in string.upper():
            morse_code = MORSE_CODE_DICT[letter]
            translated_word += f"{morse_code} "
        return translated_word
    else:
        for letter in string.split():
            for key, value in MORSE_CODE_DICT.items():
                if letter == value:
                    translated_word += key
        return translated_word.title()


while ON:
    word = input("Enter the text to be converted: ")  # word input

    for i in word.upper():
        if i not in MORSE_CODE_DICT:  # checks if word contains symbols like % and *
            print("Do not enter invalid symbols!")
            break
        else:
            print(f"The Translated Text is: {convertor(word)}")
            break

    keep_going = (input("Do u want to run the program again? Y/N: ")).lower()

    if keep_going == "n":
        ON = False
