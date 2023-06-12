def vigenere(key, message):
    message = message.lower()
    message = message.replace(' ','')
    m = len(key)
    cipher_text = ''
    for i in range(len(message)):
        letter = message[i]
        k= key[i % m]
        cipher_text = cipher_text + chr ((ord(letter) - 97 + k ) % 26 + 97)
    return cipher_text
