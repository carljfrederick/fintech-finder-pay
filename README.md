# Fintech Finder Pay

Fintech Finder Pay is an application that customers can use to find fintech professionals from a list of candidates, hire the candidate, and pay them in the cryptocurrency (Ethereum) on the personal Ethereum blockchain Ganache. The application uses the Streamlit library to provide a web application that will provide the user interface to conduct search for the preferred fintech pro and calculate the total value of the Etheruem transaction. The transaction will be digitally signed and will pay the fintech pro for their work on the Ganache blockchain. 

---

## Technologies

Fintech Finder Pay leverages Python 3.7 with the following libraries:

Streamlit: Python library used to build web interfaces for Python applications.

Web3.py: Python library for connecting to and performing operations on Ethereum-based blockchains.

data class: Python data container that can be used to create data structure blocks that can store data records.

Ganache: A program that allows you to set up a local blockchain which you can use to test and develop smart contracts.

bip44: Python implementation for deriving hierarchical deterministic wallets from a seed phrase based on the BIP-44 standard. 

python-dotenv: reads key-value pairs from a .env file and can set them as environment variables.

OS: Interacting with the computer's operating system.

Requests: HTTP Python library used to access data via APIs.

typing: Defines a standard notation for Python function and variable type annotations

web3.gas_strategies.time_based: Define Web3’s behaviour for populating gas price.

---

## Installation Guide

In your dev virtual enivronment, run the following commands:

pip install streamlit

pip install web3==5.17

pip install bip44

pip install python-dotenv

pip install requests

The following libraries are included in python 3.7: data class, OS, and typing.

To install Ganache, follow the instruction on the Ganache home page (https://trufflesuite.com/ganache/) to download and install the tool on your local machine.

----

## Usage

To use the Fintech Finder Pay application, clone or download the repository to your local computer. Open your terminal of choice and navigate to the directory that contains the fintech_finder.py file.

You will run the Streamlit application from this terminal instance and run the following command:  streamlit run fintech_finder.py

---

## Contributors

Contributions by Carl Frederick.

---

## License

MIT.

## Ganache Account

<img width="1122" alt="Screen Shot 2022-05-08 at 9 04 25 PM" src="https://user-images.githubusercontent.com/95586624/167324361-8e3ab66b-20b9-4248-a341-c311727034f8.png">

---

## Ganache Transactions

<img width="1196" alt="Screen Shot 2022-05-08 at 9 05 23 PM" src="https://user-images.githubusercontent.com/95586624/167324389-7ba17605-940c-443f-b709-6143ec856297.png">
