class RC4:
    def __init__(self, key: str):
        self.key = [ord(c) for c in key]

    def _init_sbox(self):
        S = list(range(256))
        j = 0
        for i in range(256):
            j = (j + S[i] + self.key[i % len(self.key)]) % 256
            S[i], S[j] = S[j], S[i]
        return S

    def crypt(self, text: str) -> str:
        S = self._init_sbox()
        i = j = 0
        result = []
        for char in text:
            i = (i + 1) % 256
            j = (j + S[i]) % 256
            S[i], S[j] = S[j], S[i]
            t = (S[i] + S[j]) % 256
            k = S[t]
            result.append(chr(ord(char) ^ k))
        return ''.join(result)

# Example usage of RC4
if __name__ == "__main__":
    key = "233307092"
    plaintext = "Halo, namaku ahmad, nama kamu siapa?"
    
    rc4 = RC4(key)
    ciphertext = rc4.crypt(plaintext)
    print(f"Ciphertext: {ciphertext}")

    decrypted_text = rc4.crypt(ciphertext)  # Decrypting is the same operation
    print(f"Decrypted Text: {decrypted_text}")
