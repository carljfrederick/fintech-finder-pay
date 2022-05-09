################################################################################
# Imports
from lib2to3.pgen2.pgen import generate_grammar
import streamlit as st
from dataclasses import dataclass
from typing import Any, List
from web3 import Web3
w3 = Web3(Web3.HTTPProvider('HTTP://127.0.0.1:7545'))
################################################################################


# Imports the functions generate_account, get_balance,and send_transaction from `crypto_wallet.py 

from crypto_wallet import generate_account
from crypto_wallet import get_balance
from crypto_wallet import send_transaction

################################################################################
# Fintech Finder Candidate Information

# Database of Fintech Finder candidates including their name, digital address, rating and hourly cost per Ether.
# A single Ether is currently valued at $1,500
candidate_database = {
    "Lane": ["Lane", "0xaC8eB8B2ed5C4a0fC41a84Ee4950F417f67029F0", "4.3", .20, "Images/lane.jpeg"],
    "Ash": ["Ash", "0x2422858F9C4480c2724A309D58Ffd7Ac8bF65396", "5.0", .33, "Images/ash.jpeg"],
    "Jo": ["Jo", "0x8fD00f170FDf3772C5ebdCD90bF257316c69BA45", "4.7", .19, "Images/jo.jpeg"],
    "Kendall": ["Kendall", "0x8fD00f170FDf3772C5ebdCD90bF257316c69BA45", "4.1", .16, "Images/kendall.jpeg"]
}

# A list of the FinTech Finder candidates first names
people = ["Lane", "Ash", "Jo", "Kendall"]


def get_people(w3):
    """Display the database of Fintech Finders candidate information."""
    db_list = list(candidate_database.values())

    for number in range(len(people)):
        st.image(db_list[number][4], width=200)
        st.write("Name: ", db_list[number][0])
        st.write("Ethereum Account Address: ", db_list[number][1])
        st.write("FinTech Finder Rating: ", db_list[number][2])
        st.write("Hourly Rate per Ether: ", db_list[number][3], "eth")
        st.text(" \n")

################################################################################
# Streamlit Code

# Streamlit application headings
st.markdown("# Fintech Finder!")
st.markdown("## Hire A Fintech Professional!")
st.text(" \n")

################################################################################
# Streamlit Sidebar Code - Start

st.sidebar.markdown("## Client Account Address and Ethernet Balance in Ether")

#  Calls the `generate_account` function and saves it as the variable `account`
account = generate_account()

##########################################

# Writes the client's Ethereum account address to the sidebar
st.sidebar.write(account.address)

# Calls `get_balance` function and passes it your account address
# Writes the returned ether balance to the sidebar
st.write(account.address)

##########################################

# Creates a select box to chose a FinTech Hire candidate
person = st.sidebar.selectbox('Select a Person', people)

# Creates a input field to record the number of hours the candidate worked
hours = st.sidebar.number_input("Number of Hours")

st.sidebar.markdown("## Candidate Name, Hourly Rate, and Ethereum Address")

# Identifies the FinTech Hire candidate
candidate = candidate_database[person][0]

# Writes the Fintech Finder candidate's name to the sidebar
st.sidebar.write(candidate)

# Identifies the FinTech Finder candidate's hourly rate
hourly_rate = candidate_database[person][3]

# Writes the FinTech Finder candidate's hourly rate to the sidebar
st.sidebar.write(hourly_rate)

# Identifies the FinTech Finder candidate's Ethereum Address
candidate_address = candidate_database[person][1]

# Writes the inTech Finder candidate's Ethereum Address to the sidebar
st.sidebar.write(candidate_address)

# Writes the Fintech Finder candidate's name to the sidebar

st.sidebar.markdown("## Total Wage in Ether")

################################################################################
# Step 2: Signs and Executes a Payment Transaction


# Calculates total `wage` for the candidate by multiplying the candidate’s hourly
# rate from the candidate database (`candidate_database[person][3]`) by the
# value of the `hours` variable
wage = candidate_database[person][3] * hours

# Writes the `wage` calculation to the Streamlit sidebar
st.sidebar.write(wage)


# * Saves the transaction hash that the `send_transaction` function returns as a
# variable named `transaction_hash` and displays on the application’s
# web interface.


if st.sidebar.button("Send Transaction"):

    # Calls the `send_transaction` function and pass it 3 parameters:
    # Your `account`, the `candidate_address`, and the `wage` as parameters
    # Saves the returned transaction hash as a variable named `transaction_hash`
    transaction_hash = send_transaction(w3, account, candidate_address, wage)

    # Markdown for the transaction hash
    st.sidebar.markdown("#### Validated Transaction Hash")

    # Writes the returned transaction hash to the screen
    st.sidebar.write(transaction_hash)

    # Celebrates your successful payment
    st.balloons()

# The function that starts the Streamlit application
# Writes FinTech Finder candidates to the Streamlit page
get_people(w3)

################################################################################
# Step 3: Inspect the Transaction

# Send a test transaction by using the application’s web interface, and then
# look up the resulting transaction hash in Ganache.

# Complete the following steps:

# 1. From your terminal, navigate to the project folder that contains
# your `.env` file and the `fintech_finder.py` and `crypto_wallet.py` files.
# Be sure to activate your Conda `dev` environment if it is not already active.

# 2. To launch the Streamlit application,
# type `streamlit run fintech_finder.py`.

# 3. On the resulting webpage, select a candidate that you would like to hire
# from the appropriate drop-down menu. Then, enter the number of hours that you
# would like to hire them for. (Remember, you do not have a lot of ether in
# your account, so you cannot hire them for long!)

# 4 Click the Send Transaction button to sign and send the transaction with
# your Ethereum account information. If the transaction is successfully
# communicated to Ganache, validated, and added to a block,
# a resulting transaction hash code will be written to the Streamlit
# application sidebar.

# 5. Navigate to the Ganache accounts tab and locate your account (index 0).

# 6. Navigate to the Ganache transactions tab and locate the transaction.
 
