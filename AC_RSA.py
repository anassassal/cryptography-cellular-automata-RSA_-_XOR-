import random
from sympy import nextprime
from Crypto.Util.number import inverse

# Fonction pour initialiser l'automate cellulaire avec une source d'entropie
def init_automate(size):
    return [random.randint(0, 1) for _ in range(size)]

# Règle 30 pour l'évolution de l'automate cellulaire
def rule30(state):
    new_state = []
    for i in range(len(state)):
        left = state[i-1] if i-1 >= 0 else state[-1]
        center = state[i]
        right = state[i+1] if i+1 < len(state) else state[0]
        new_state.append(left ^ (center | right))
    return new_state

# Fonction pour extraire des bits à partir de l'état final de l'automate cellulaire
def extract_bits(state, num_bits):
    bits = []
    for cell in state:
        bits.append(cell)
        if len(bits) >= num_bits:
            break
    return bits

# Générer un nombre pseudo-aléatoire à partir des bits extraits
def bits_to_int(bits):
    return int(''.join(map(str, bits)), 2)

# Fonction pour générer des clés RSA
def generate_rsa_keys(bits_length):
    # Initialisation de l'automate cellulaire
    #size = bits_length//2
    size = bits_length 
    state = init_automate(size)

    # Évolution de l'automate cellulaire
    for _ in range(size):
        state = rule30(state)

    # Extraction de bits et génération de nombres premiers
    p_bits = extract_bits(state, int(bits_length*0.8))
    q_bits = extract_bits(state, int(bits_length * 0.7))
    p = nextprime(bits_to_int(p_bits))
    q = nextprime(bits_to_int(q_bits))

    # Calcul des paramètres RSA
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 65537  # Valeur couramment utilisée pour e
    d = inverse(e, phi)
    

    return (n, e), (n, d)
# function de transfere entier -->binaire
def int_to_bin(nombre):
    return bin(nombre)[2:]

# function de transfere binaire -->entier
def bin_to_int(binaire):
    return int(binaire, 2) 

# Fonction de chiffrement RSA
def encrypt(message, public_key):
    n, e = public_key
    ciphertext = pow(message, e, n)
    return int_to_bin(ciphertext) 

# Fonction de déchiffrement RSA
def decrypt(ciphertext, private_key):
    n, d = private_key
    plaintext = pow(bin_to_int(ciphertext), d, n)
    return plaintext

# Exemple d'utilisation
bits_length = 100
public_key, private_key = generate_rsa_keys(bits_length)
print("Clé publique:", public_key)
print("Clé privée:", private_key)

# Chiffrement et déchiffrement d'un nombre
message = 1991
print("Message original:", message)

ciphertext = encrypt(message, public_key)
print("Message chiffré:", ciphertext)

decrypted_message = decrypt(ciphertext, private_key)
print("Message déchiffré:", decrypted_message)
