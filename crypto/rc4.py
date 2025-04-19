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


key = "123456789"
pesan = "Bagas Yudha"

rc4 = RC4(key)

ciphertext = rc4.crypt(pesan)
print("Ciphertext:", ciphertext)

# Karena RC4 bersifat simetris, cukup panggil lagi `crypt` untuk dekripsi
decrypted = rc4.crypt(ciphertext)
print("Decrypted :", decrypted)
