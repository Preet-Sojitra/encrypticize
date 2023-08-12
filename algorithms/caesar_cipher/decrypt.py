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


def decrypt(key: int, cypher_text: str) -> str:
    decrypted_string = ""

    for i in cypher_text:
        if i in alphabets:
            decrypted_string += alphabets[(alphabets.index(i) - key) % 26]
        else:
            decrypted_string += i

    return decrypted_string
