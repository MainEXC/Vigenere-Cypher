def encrypt(plaintext, key):
    ciphertext = ""
    j = 0
    for i in range(len(plaintext)):
        char = plaintext[i]
        if char.isalpha():
            if char.isupper():
                ciphertext += chr((ord(char) + ord(key[j % len(key)].upper()) - 2 * 65) % 26 + 65)
            else:
                ciphertext += chr((ord(char) + ord(key[j % len(key)].lower()) - 2 * 97) % 26 + 97)
            j += 1
        else:
            ciphertext += char
    return ciphertext
