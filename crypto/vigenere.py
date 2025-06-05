# crypto/vigenere.py
class VigenereCipher:
    def __init__(self, key):
        self.key = key

    def encrypt(self, text):
        key = (self.key * (len(text) // len(self.key) + 1))[:len(text)]
        encrypted = ''.join(chr((ord(t) + ord(k)) % 256) for t, k in zip(text, key))
        return encrypted

    def decrypt(self, text):
        key = (self.key * (len(text) // len(self.key) + 1))[:len(text)]
        decrypted = ''.join(chr((ord(t) - ord(k)) % 256) for t, k in zip(text, key))
        return decrypted

# Example usage of VigenereCipher
if __name__ == "__main__":
    key = "233307092"
    plaintext = "Halo, namaku ahmad, nama kamu siapa?"
    
    vigenere = VigenereCipher(key)
    ciphertext = vigenere.encrypt(plaintext)
    print(f"Ciphertext: {ciphertext}")

    decrypted_text = vigenere.decrypt(ciphertext)
    print(f"Decrypted Text: {decrypted_text}")