# Automate Cellulaire et Chiffrement

Ce projet utilise un automate cellulaire (Règle 30) pour générer des clés de chiffrement et effectuer un chiffrement/déchiffrement simple par XOR sur des messages entiers.

## Contenu du Projet(XOR)

- **init_automate(size)** : Initialise l'automate cellulaire avec une cellule centrale définie à 1.
- **rule30(state)** : Applique la Règle 30 pour générer l'état suivant de l'automate cellulaire.
- **generate_key(message)** : Génère une clé basée sur l'évolution de l'automate cellulaire pour un message donné.
- **int_to_bin(nombre)** : Convertit un nombre entier en une liste de bits.
- **bin_to_int(binaire)** : Convertit une liste de bits en un nombre entier.
- **encrypt(message, key)** : Chiffre un message en utilisant une clé par XOR.
- **decrypt(ciphertext, key)** : Déchiffre un message chiffré en utilisant une clé par XOR.
- 
# Automate Cellulaire pour Génération de Clés RSA

Ce projet utilise un automate cellulaire (Règle 30) pour générer des clés RSA et chiffrer/déchiffrer des messages.

## Description

L'algorithme exploite un automate cellulaire pour produire des bits pseudo-aléatoires, utilisés ensuite pour générer des nombres premiers nécessaires à la création des clés RSA.

