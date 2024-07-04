# Fonction pour initialiser l'automate cellulaire au milieu par '1'
def init_automate(size):
    automate = [0] * size
    if size > 0:
        automate[size // 2] = 1
    return automate

# Règle 30
def rule30(state):
    new_state = []
    for i in range(len(state)):
        left = state[i-1] if i-1 >= 0 else state[-1]
        center = state[i]
        right = state[i+1] if i+1 < len(state) else state[0]
        new_state.append(left ^ (center | right))
    return new_state

# Fonction pour générer la clé
def generate_key(message):
    message_bin = int_to_bin(message)
    size = len(message_bin)
    state = init_automate(size)
    # Évolution de l'automate cellulaire
    for _ in range(size):
        state = rule30(state)
    return state

# Fonction de transfert entier --> binaire
def int_to_bin(nombre):
    return [int(bit) for bit in bin(nombre)[2:]]

# Fonction de transfert binaire --> entier
def bin_to_int(binaire):
    return int(''.join(str(bit) for bit in binaire), 2)

# Fonction de chiffrement XOR
def encrypt(message, key):
    msg_to_bin = int_to_bin(message)
    if len(msg_to_bin) != len(key):
        raise ValueError("La taille de la clé doit être égale à la taille du message")
    return [a ^ b for a, b in zip(msg_to_bin, key)]

# Fonction de déchiffrement XOR
def decrypt(ciphertext, key):
    if len(ciphertext) != len(key):
        raise ValueError("La taille de la clé doit être égale à la taille du chiffrement")
    return bin_to_int([a ^ b for a, b in zip(ciphertext, key)])

# Chiffrement et déchiffrement d'un nombre
message =1999999999999999999999999
key = generate_key(message)
print("Clé privée:", ''.join(map(str, key)))
print("Message original:", message)

ciphertext = encrypt(message, key)
print("Message chiffré:",''.join(map(str, ciphertext)))

decrypted_message = decrypt(ciphertext, key)
print("Message déchiffré:", decrypted_message)
