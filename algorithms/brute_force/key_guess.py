from time import time

alphabets = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]


def key_guess(cypher_text: str) -> tuple:
    decrypted_strings = []

    time_start = time()

    for key in range(26):
        decrypted_string = ""
        for letter in cypher_text:
            if letter in alphabets:
                index = alphabets.index(letter)
                decrypted_string += alphabets[(index - key) % 26]
            else:
                decrypted_string += letter

        decrypted_strings.append(decrypted_string)

    time_end = time()

    return decrypted_strings, time_end - time_start


all_strings, time_taken = key_guess("thiy")
print(all_strings)
