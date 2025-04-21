from crypto.aes import AESCipher
from crypto.rc4 import RC4
from crypto.vigenere import VigenereCipher

class EncryptionPipeline:
    def __init__(self, user_id: str):
        self.user_id = user_id
        self.vigenere = VigenereCipher(user_id)
        self.rc4 = RC4(user_id)
        self.aes = AESCipher(user_id)

    def encrypt(self, plaintext: str) -> str:
        print("\n===== Mulai Proses Enkripsi =====")
        # Enkripsi tahap 1 - AES128
        ciphertext_aes = self.aes.encrypt(plaintext, output_format='base64')
        print(f"\n[+] Ciphertext setelah AES128: {ciphertext_aes}")

        # Enkripsi tahap 2 - Vigenere
        ciphertext_vigenere = self.vigenere.encrypt(ciphertext_aes)
        print(f"[+] Ciphertext setelah Vigenere: {ciphertext_vigenere}")

        # Enkripsi tahap 3 - RC4
        ciphertext_rc4 = self.rc4.crypt(ciphertext_vigenere)
        print(f"[+] Ciphertext setelah RC4: {ciphertext_rc4}")
        
        print("\n===== Final Ciphertext =====")
        finally_ciphertext = ciphertext_rc4
        print(f"[+] Final Ciphertext: {finally_ciphertext}")

        return finally_ciphertext

    def decrypt(self, final_ciphertext: str) -> str:
        print("\n===== Mulai Proses Dekripsi =====")

        # Dekripsi tahap 1 - RC4
        decrypted_rc4 = self.rc4.crypt(final_ciphertext)
        print(f"[+] Setelah dekripsi RC4: {decrypted_rc4}")

        # Dekripsi tahap 2 - Vigenere
        decrypted_vigenere = self.vigenere.decrypt(decrypted_rc4)
        print(f"[+] Setelah dekripsi Vigenere: {decrypted_vigenere}")

        # Dekripsi tahap 3 - AES128
        decrypted_aes = self.aes.decrypt(decrypted_vigenere, input_format='base64')
        print(f"[+] Setelah dekripsi AES128: {decrypted_aes.decode('Windows-1252')}")
        
        print("\n===== Hasil Dekripsi =====")
        finally_decrypted = decrypted_aes.decode('Windows-1252')
        print(f"[+] Hasil Dekripsi: {finally_decrypted}")
      
        return finally_decrypted

# Contoh Penggunaan
if __name__ == "__main__":
    user_id = "233307092"
    plaintext = "Halo, namaku ahmad, nama kamu siapa?, Halo, namaku ahmad, nama kamu siapa?, Halo, namaku ahmad, nama kamu siapa?"
    
    print(f"User ID: {user_id}")
    print(f"Pesan: {plaintext}")

    # Membuat instance dari EncryptionPipeline
    pipeline = EncryptionPipeline(user_id)

    # Enkripsi pesan
    final_cipher = pipeline.encrypt(plaintext)

    # Dekripsi pesan
    hasil_dekripsi = pipeline.decrypt(final_cipher)
