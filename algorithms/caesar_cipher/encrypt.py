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


def encrypt(key: int, plain_text: str) -> str:
    encrypted_string = ""

    for i in plain_text:
        if i in alphabets:
            encrypted_string += alphabets[(alphabets.index(i) + key) % 26]
        else:
            encrypted_string += i

    return encrypted_string
