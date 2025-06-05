from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64
from hashlib import sha256

class AESCipher:
    def __init__(self, user_id: str):
        hashed = sha256(user_id.encode()).digest() 
        self.key = hashed[:16]
        self.iv = hashed[16:32]

    def encrypt(self, plaintext: str) -> str:
        plaintext = plaintext.encode()

        padded = pad(plaintext, AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        ciphertext = cipher.encrypt(padded)
        b64_ciphertext = base64.b64encode(ciphertext).decode()

        print("\n==== PROSES ENKRIPSI AES-128 ====")
        print("Key:", self.key)
        print("IV:", self.iv)
        print("Plaintext (Hex):", padded)
        print("Ciphertext (Hex):", ciphertext.hex())
        print("Ciphertext (Base64):", b64_ciphertext)

        return b64_ciphertext

    def decrypt(self, ciphertext: str) -> str:
        ciphertext_byte = base64.b64decode(ciphertext)

        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        decrypted = cipher.decrypt(ciphertext_byte)

        try:
            plaintext = unpad(decrypted, AES.block_size)
            print("\n==== PROSES DEKRIPSI AES-128 ====")
            print("Key:", self.key)
            print("IV:", self.iv)
            print("Ciphertext:", ciphertext_byte)
            print("Ciphertext (byte):", ciphertext_byte)
            print("Decrypted Plaintext (Hex):", plaintext)
            print(f"Decrypted Plaintext: {plaintext.decode()}")
            return plaintext.decode()
        except ValueError:
            print("Error: Padding is incorrect. Data mungkin rusak atau kunci salah.")
            return b''

# Contoh penggunaan
if __name__ == "__main__":
    user_id = "233307092"
    plaintext = "Nama aku Hamdani"

    aes_cipher = AESCipher(user_id)

    ciphertext = aes_cipher.encrypt(plaintext)
    print(f"Ciphertext: {ciphertext}")

    decrypted_text = aes_cipher.decrypt(ciphertext)
    print(f"Decrypted Text: {decrypted_text}")
