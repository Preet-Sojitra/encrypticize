import streamlit as st
from playfair_cipher import encrypt
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
    options=["None", "Caesar Cipher"],
    placeholder="Select method",
)

if option == "Caesar Cipher":
    # st.write("You selected: ", option)

    st.write("<p style='font-size: 20px;'>Enter Key</p>", unsafe_allow_html=True)
    key = st.text_input(
        label="Enter key",
        key="key",
        placeholder="Enter key",
        label_visibility="collapsed",
    )
    # st.write("You entered: ", key)

    st.write(
        "<p style='font-size: 20px;'>Enter text to encrypt</p>", unsafe_allow_html=True
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
        table, encrypted_text = encrypt(key, plain_text)
        # pprint(table)
        # print(encrypted_text)

        st.markdown("# Output")

        col1, col2 = st.columns([2, 1])

        with col1:
            st.header("Encryption Table: ", anchor=False)
            table = pd.DataFrame(table, columns=(["col{}".format(i) for i in range(5)]))
            st.dataframe(table, hide_index=True, width=400)

        with col2:
            st.header("Encrypted text: ", anchor=False)
            st.subheader("_{}_".format(encrypted_text), anchor=False)
