import streamlit as st
from algorithms.caesar_cipher.encrypt import encrypt as caesar_encrypt
from algorithms.caesar_cipher.decrypt import decrypt as caesar_decrypt
from algorithms.brute_force.guess_password import guess_password
from algorithms.brute_force.key_guess import key_guess
from algorithms.playfair_cipher.encrypt import encrypt as playfair_encrypt
from algorithms.playfair_cipher.decrypt import decrypt as playfair_decrypt
from pprint import pprint
import pandas as pd

st.markdown(
    """
            <style>
                label-size{
                    font-size: 20px;
                }
            </style>
            """,
    unsafe_allow_html=True,
)

st.title("Encryption Methods")

st.write(
    "<p style='font-size: 20px;'>Select encryption method</p>", unsafe_allow_html=True
)

option = st.selectbox(
    label="Select encryption method",
    label_visibility="collapsed",
    options=["None", "Caesar Cipher", "Brute Force", "Playfair Cipher"],
    placeholder="Select method",
)

radio = None

if option != "None":
    st.write(
        "<p style='font-size: 20px;'> What you want to do?</p>", unsafe_allow_html=True
    )

    if option == "Brute Force":
        radio = st.radio(
            label="Guess Password",
            options=["Guess Password", "Guess Key"],
            label_visibility="collapsed",
            horizontal=True,
        )

    else:
        radio = st.radio(
            label="Encrypt or Decrypt",
            options=["Encrypt", "Decrypt"],
            label_visibility="collapsed",
            horizontal=True,
        )

# FOR: Caesar Cipher
if option == "Caesar Cipher":
    # st.write("You selected: ", option)

    st.write("<p style='font-size: 20px;'>Enter Key</p>", unsafe_allow_html=True)
    key = st.text_input(
        label="Enter key",
        key="key",
        placeholder="Enter key (integer)",
        label_visibility="collapsed",
    )
    # st.write("You entered: ", key)

    if radio == "Encrypt":
        st.write(
            "<p style='font-size: 20px;'>Enter text to encrypt</p>",
            unsafe_allow_html=True,
        )
        col1, col2 = st.columns([7, 1])

        with col1:
            plain_text = st.text_input(
                label="Enter text to encrypt",
                label_visibility="collapsed",
                key="text_input",
                placeholder="Enter text",
            )
            # st.write("You entered: ", plain_text)

        with col2:
            button = st.button(label="Encrypt")

        if button:
            if key == "" or plain_text == "":
                st.error("Key or text cannot be empty")
                st.stop()

            encrypted_text = caesar_encrypt(int(key), plain_text)
            # print(encrypted_text)

            st.markdown("# Output")

            st.header("Encrypted text: ", anchor=False)
            st.code(encrypted_text, language="plaintext")

    elif radio == "Decrypt":
        st.write(
            "<p style='font-size: 20px;'>Enter text to decrypt</p>",
            unsafe_allow_html=True,
        )
        col1, col2 = st.columns([7, 1])

        with col1:
            cipher_text = st.text_input(
                label="Enter text to decrypt",
                label_visibility="collapsed",
                key="text_input",
                placeholder="Enter cipher text",
            )
            # st.write("You entered: ", plain_text)

        with col2:
            button = st.button(label="Decrypt")

        if button:
            decrypted_text = caesar_decrypt(int(key), cipher_text)
            # pprint(table)
            # print(encrypted_text)

            st.markdown("# Output")

            st.header("Decrypted text: ", anchor=False)
            st.subheader("_{}_".format(decrypted_text), anchor=False)


if option == "Brute Force":
    if radio == "Guess Password":
        st.write(
            "<p style='font-size: 20px;'>Enter Password</p>", unsafe_allow_html=True
        )

        col1, col2 = st.columns([4, 1])

        with col1:
            password = st.text_input(
                label="Enter password",
                key="key",
                placeholder="Enter password (only 3 characters )",
                label_visibility="collapsed",
            )

        with col2:
            button = st.button(label="Guess Password")

        if button:
            if password == "":
                st.error("Password cannot be empty")
                st.stop()

            all_combinations, correct_password, time_taken = guess_password(password)

            st.markdown("# Output")

            st.write(
                "<p style='font-size: 18px;'>All possible combinations : {}</p>".format(
                    len(all_combinations)
                ),
                unsafe_allow_html=True,
            )
            st.write(
                "<p style='font-size: 18px;'>Time taken : {} seconds</p>".format(
                    round(time_taken, 4)
                ),
                unsafe_allow_html=True,
            )
            st.write(
                "<p style='font-size: 18px;'>Correct password : {}</p>".format(
                    correct_password
                ),
                unsafe_allow_html=True,
            )

    elif radio == "Guess Key":
        st.write(
            "<p style='font-size: 20px;'>Enter Cipher Text</p>", unsafe_allow_html=True
        )

        col1, col2 = st.columns([4, 1])

        with col1:
            cipher_text = st.text_input(
                label="Cipher Text",
                key="key",
                placeholder="Cipher Text",
                label_visibility="collapsed",
            )

        with col2:
            button = st.button(label="Guess Key")

        if button:
            if cipher_text == "":
                st.error("Cipher Text cannot be empty")
                st.stop()

            all_combinations, time_taken = key_guess(cipher_text)

            st.markdown("# Output")

            st.write(
                "<p style='font-size: 18px;'>Time taken : {} seconds</p>".format(
                    round(time_taken, 4)
                ),
                unsafe_allow_html=True,
            )
            st.write(
                "<p style='font-size: 18px;'>All possible combinations :</p>",
                unsafe_allow_html=True,
            )
            st.write(
                "<p style='font-size: 18px;'>{}</p>".format(all_combinations),
                unsafe_allow_html=True,
            )

# FOR: Playfair Cipher
if option == "Playfair Cipher":
    # st.write("You selected: ", option)

    st.write("<p style='font-size: 20px;'>Enter Key</p>", unsafe_allow_html=True)
    key = st.text_input(
        label="Enter key",
        key="key",
        placeholder="Enter key",
        label_visibility="collapsed",
    )
    # st.write("You entered: ", key)

    if radio == "Encrypt":
        st.write(
            "<p style='font-size: 20px;'>Enter text to encrypt</p>",
            unsafe_allow_html=True,
        )
        col1, col2 = st.columns([7, 1])

        with col1:
            plain_text = st.text_input(
                label="Enter text to encrypt",
                label_visibility="collapsed",
                key="text_input",
                placeholder="Enter text",
            )
            # st.write("You entered: ", plain_text)

        with col2:
            button = st.button(label="Encrypt")

        if button:
            if key == "" or plain_text == "":
                st.error("Key or text cannot be empty")
                st.stop()

            table, encrypted_text = playfair_encrypt(key, plain_text)
            # pprint(table)
            # print(encrypted_text)

            st.markdown("# Output")

            col1, col2 = st.columns([1.8, 1.2])

            with col1:
                st.header("Key Square Table: ", anchor=False)
                table = pd.DataFrame(
                    table, columns=(["col{}".format(i) for i in range(5)])
                )
                st.dataframe(table, hide_index=True, width=400)

            with col2:
                st.header("Encrypted text: ", anchor=False)

                # st.subheader("_{}_".format(encrypted_text), anchor=False)
                st.code(encrypted_text, language="plaintext")

    elif radio == "Decrypt":
        st.write(
            "<p style='font-size: 20px;'>Enter text to decrypt</p>",
            unsafe_allow_html=True,
        )
        col1, col2 = st.columns([7, 1])

        with col1:
            cipher_text = st.text_input(
                label="Enter text to decrypt",
                label_visibility="collapsed",
                key="text_input",
                placeholder="Enter cipher text",
            )
            # st.write("You entered: ", plain_text)

        with col2:
            button = st.button(label="Decrypt")

        if button:
            table, decrypted_text = playfair_decrypt(key, cipher_text)
            # pprint(table)
            # print(encrypted_text)

            st.markdown("# Output")

            col1, col2 = st.columns([1.8, 1.2])

            with col1:
                st.header("Key Square Table: ", anchor=False)
                table = pd.DataFrame(
                    table, columns=(["col{}".format(i) for i in range(5)])
                )
                st.dataframe(table, hide_index=True, width=400)

            with col2:
                st.header("Decrypted text: ", anchor=False)
                st.subheader("_{}_".format(decrypted_text), anchor=False)
