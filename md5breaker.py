import hashlib
import argparse

# Creating the argument parser
parser = argparse.ArgumentParser(description="Crack an MD5 hash using a provided wordlist.")
parser.add_argument('-w', '--wordlist', type=str, required=True, help="Path to the wordlist file")
parser.add_argument('-u', '--hash', type=str, required=True, help="The MD5 hash to be cracked")

# Parse the arguments provided by the user
args = parser.parse_args()

# Variables from the arguments
wordlist = args.wordlist
str2hash = args.hash

# Trying to open the wordlist file and compare the hashes
try:
    with open(wordlist, 'r') as file:
        for cell in file:
            cell = cell.strip()
            result2 = hashlib.md5(cell.encode())
            if result2.hexdigest() == str2hash:
                print('\n[*] HASH BROKEN: ' + f'{cell}' + '\n')
                break
            else:
                print(result2.hexdigest() + " ===== " + cell)
except FileNotFoundError:
    print(f"Error: The file {wordlist} was not found.")
