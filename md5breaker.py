import hashlib
import argparse

# Criando o parser de argumentos
parser = argparse.ArgumentParser(description="Quebra um hash MD5 usando uma wordlist fornecida.")
parser.add_argument('-w', '--wordlist', type=str, required=True, help="Caminho para o arquivo de wordlist")
parser.add_argument('-u', '--hash', type=str, required=True, help="O hash MD5 a ser quebrado")

# Parse os argumentos fornecidos pelo usuário
args = parser.parse_args()

# Variáveis a partir dos argumentos
wordlist = args.wordlist
str2hash = args.hash

# Tentando abrir o arquivo wordlist e comparar os hashes
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
