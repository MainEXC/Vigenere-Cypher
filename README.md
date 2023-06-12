## Vigenere-Cypher

This repository contains Python code for implementing the Vigenere Cipher, a polyalphabetic substitution cipher that encrypts alphabetic text using a series of interwoven Caesar ciphers. The code can be used to encrypt and decrypt messages using a given key.

## Files

This repository includes the following files:

- `vigenere.py`: Python script for encrypting and decrypting messages using the Vigenere Cipher.
- `README.md`: A brief introduction to the Vigenere Cipher and instructions for using the `vigenere.py` script.
- `LICENSE`: MIT License for the code.

## Usage

The `vigenere.py` script takes a message and a key as input and returns the encrypted or decrypted message. The script uses the ASCII values of the characters to perform the encryption and decryption.

To encrypt a message using the Vigenere Cipher, run the following command in the terminal:

```
python vigenere.py -e "message" "key"
```

To decrypt a message using the Vigenere Cipher, run the following command in the terminal:

```
python vigenere.py -d "encrypted message" "key"
```

Replace `"message"` with the message you want to encrypt, `"key"` with the key you want to use for encryption, and `"encrypted message"` with the message you want to decrypt.

## License

This repository is licensed under the MIT License. You are free to use and modify the code as you like. See the `LICENSE` file for more information.

## Acknowledgments

This repository is intended for anyone who wants to learn about the Vigenere Cipher and how to implement it using Python. If you find any bugs or have suggestions for improvement, feel free to open an issue or submit a pull request.
