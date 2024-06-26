from art import *
import time


def converter():

    morse_alphabet = [  # letters
        ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.",
        "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--..",
        # numbers
        "-----", ".----", "..---", "...--", "....-", ".....", "-....", "--...", "---..", "----.",
        # characters
        ".-.-.-", "--..--", "---...", "..--..", ".----.", "-....-", "-..-.", "-.--.", "-.--.-", "......."
    ]

    en = [  # letters
        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
        "w", "x", "y", "z",
        # numbers
        "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
        # characters
        ".", ",", ":", "?", "'", "-", "/", "(", ")", " "
    ]

    tprint("MORSE CONVERTER")
    time.sleep(2)

    print("Welcome to my Text to Morse Converter! Hope this help :)")
    time.sleep(1)

    string = input("\nJust tell me what your secret and I won't tell a soul 😉 : ")

    morse_code = ""

    for letter in string.lower():
        index = en.index(letter)

        morse_code += morse_alphabet[index] + " "

    print(morse_code)


converter()
