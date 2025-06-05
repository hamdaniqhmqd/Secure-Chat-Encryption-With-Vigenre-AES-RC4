from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import binascii
import base64
from hashlib import sha256

class AESCipher:
    def __init__(self, user_id: str):
        hashed = sha256(user_id.encode("Windows-1252")).digest()
        print(f"Hash: {hashed}")
        self.key = hashed[:16]
        self.iv = hashed[16:32]

    def encrypt(self, plaintext: str | bytes, output_format='bytes') -> bytes | str:
        if isinstance(plaintext, str):
            plaintext = plaintext.encode('Windows-1252')

        padded = pad(plaintext, AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        ciphertext = cipher.encrypt(padded)

        print("\n==== PROSES ENKRIPSI AES-128 ====")
        print("Hash", self.key + self.iv)
        print("Key", self.key)
        print("IV", self.iv)
        print("Plaintext (Hex)", padded)
        print("Ciphertext", ciphertext)

        if output_format == 'hex':
            return ciphertext.hex()
        elif output_format == 'base64':
            return base64.b64encode(ciphertext).decode('Windows-1252')
        return ciphertext

    def decrypt(self, ciphertext: str | bytes, input_format='bytes') -> bytes:
        if input_format == 'hex' and isinstance(ciphertext, str):
            ciphertext = bytes.fromhex(ciphertext)
        elif input_format == 'base64' and isinstance(ciphertext, str):
            ciphertext = base64.b64decode(ciphertext)

        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        decrypted = cipher.decrypt(ciphertext)

        try:
            plaintext = unpad(decrypted, AES.block_size)
            print("\n==== PROSES DEKRIPSI AES-128 ====")
            print("Key", self.key)
            print("IV", self.iv)
            print("Ciphertext", ciphertext)
            print("Decrypted Plaintext (Hex)", plaintext)
            print(f"Decrypted Plaintext: {plaintext.decode(errors='ignore')}")
            return plaintext
        except ValueError:
            print("Error: Padding is incorrect. Data mungkin rusak atau kunci salah.")
            return b''

# Contoh penggunaan
if __name__ == "__main__":
    user_id = "233307092"
    plaintext = "Halo, namaku ahmad, nama kamu siapa?"

    aes_cipher = AESCipher(user_id)
    
    ciphertext = aes_cipher.encrypt(plaintext, output_format='base64')
    print(f"Ciphertext (Base64): {ciphertext}")

    decrypted_text = aes_cipher.decrypt(ciphertext, input_format='base64')
    print(f"Decrypted Text: {decrypted_text.decode('Windows-1252')}") 