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


def guess_password(password: str) -> tuple:
    all_combinations = []
    correct_password = ""

    time_start = time()

    for i in range(len(alphabets)):
        guessed_password = alphabets[i]

        for j in range(len(alphabets)):
            guessed_password = alphabets[i] + alphabets[j]

            for k in range(len(alphabets)):
                guessed_password = alphabets[i] + alphabets[j] + alphabets[k]
                # All combinations of passwords
                # print(guessed_password, end=" ")
                all_combinations.append(guessed_password)

                if guessed_password == password:
                    correct_password = guessed_password
                    # print("Correct password is: ", correct_password)

    time_end = time()

    return all_combinations, correct_password, time_end - time_start
