## End-to-End Encryption using Python

# -----------------------------      ------------------------------------------------
# To implement end-to-end encryption using Python, I’ll first define two Python functions to determine
# if the length of a message is odd or even:
def is_even(number):
    return number % 2 == 0

def get_even_letters(message):
    even_letters = []
    for counter in range(0, len(message)):
        if is_even(counter):
            even_letters.append(message[counter])
    return even_letters

def get_odd_letters(message):
    odd_letters = []
    for counter in range(0, len(message)):
        if not is_even(counter):
            odd_letters.append(message[counter])
    return odd_letters

# Now I will define a Python function to swap the letters of the message between them, here
# if the length of the letters in the message will be odd then we will add an extra letter to the message as “x”:
def swap_letters(message):
    letter_list = []
    if not is_even(len(message)):
        message = message + 'x'
    even_letters = get_even_letters(message)
    odd_letters = get_odd_letters(message)
    for counter in range(0, int(len(message)/2)):
        letter_list.append(odd_letters[counter])
        letter_list.append(even_letters[counter])
    new_message = ''.join(letter_list)
    return new_message

# Now let’s test this end-to-end encryption system by creating an
# end-to-end application using the streamlit library:
import streamlit as st
st.title("End-to-End Encryption")
user = st.text_input("Enter a Message")
st.write(swap_letters(user))

# As we are using the streamlit library here, so to run your code use the command streamlit run filename.py