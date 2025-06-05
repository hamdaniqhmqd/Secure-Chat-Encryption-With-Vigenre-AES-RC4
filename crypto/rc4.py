# FINAL RC NO BUG
class RC4:
    def __init__(self, key: str):
        self.key_bytes = [ord(character) for character in key]

    def _init_sbox(self):
        sbox = list(range(256))
        key_index = 0
        for i in range(256):
            key_index = (key_index + sbox[i] + self.key_bytes[i % len(self.key_bytes)]) % 256
            sbox[i], sbox[key_index] = sbox[key_index], sbox[i]
        return sbox

    def crypt(self, plaintext: str) -> str:
        sbox = self._init_sbox()
        index_i = 0
        index_j = 0
        ciphertext_chars = []

        for character in plaintext:
            index_i = (index_i + 1) % 256
            index_j = (index_j + sbox[index_i]) % 256
            sbox[index_i], sbox[index_j] = sbox[index_j], sbox[index_i]

            keystream_index = (sbox[index_i] + sbox[index_j]) % 256
            keystream_byte = sbox[keystream_index]

            encrypted_char = chr(ord(character) ^ keystream_byte)
            ciphertext_chars.append(encrypted_char)

        return ''.join(ciphertext_chars)

# key = "yudha"
# plaintext = "aku yudha"
# obj = RC4(key)
# sbox = obj._init_sbox()

# ciphertext = obj.crypt(plaintext)
# decrypted = obj.crypt(ciphertext)

# print(f"Key: {obj.key_bytes}")
# print(f"SBox: {sbox}")
# print(f"Hail Enskripsi: {ciphertext}")
# print(f"Hasil Dekripsi: {decrypted}")

# WITH PROCESS
# class RC4:
#     def __init__(self, key: str):
#         self.key_bytes = [ord(character) for character in key]

#     def _init_sbox(self):
#         sbox = list(range(256))
#         key_index = 0
#         for i in range(256):
#             key_index = (key_index + sbox[i] + self.key_bytes[i % len(self.key_bytes)]) % 256
#             sbox[i], sbox[key_index] = sbox[key_index], sbox[i]
#         return sbox

#     def crypt(self, plaintext: str) -> str:
#         sbox = self._init_sbox()
#         index_i = 0
#         index_j = 0
#         ciphertext_chars = []

#         print("\n=== PROSES ENKRIPSI ===")
#         for idx, character in enumerate(plaintext):
#             index_i = (index_i + 1) % 256
#             index_j = (index_j + sbox[index_i]) % 256
#             sbox[index_i], sbox[index_j] = sbox[index_j], sbox[index_i]

#             keystream_index = (sbox[index_i] + sbox[index_j]) % 256
#             keystream_byte = sbox[keystream_index]

#             encrypted_char = chr(ord(character) ^ keystream_byte)
#             ciphertext_chars.append(encrypted_char)

#             print(f"[{idx}] '{character}' -> ord: {ord(character)} | keystream: {keystream_byte} | XOR result: {ord(character) ^ keystream_byte} -> '{encrypted_char}'")

#         return ''.join(ciphertext_chars)


# key = "yu"
# plaintext = "aku yudha"
# obj = RC4(key)
# sbox = obj._init_sbox()

# ciphertext = obj.crypt(plaintext)
# decrypted = obj.crypt(ciphertext)

# print(f"\nKey: {obj.key_bytes}\n")
# print(f"SBox: {sbox}\n")
# print(f"Hail Enskripsi: {ciphertext}")
# print(f"Hasil Dekripsi: {decrypted}\n")


# OGIGINAL
# class RC4:
#     def __init__(self, key: str):
#         self.key = [ord(c) for c in key]

#     def _init_sbox(self):
#         S = list(range(256))
#         j = 0
#         for i in range(256):
#             j = (j + S[i] + self.key[i % len(self.key)]) % 256
#             S[i], S[j] = S[j], S[i]
#         return S

#     def crypt(self, text: str) -> str:
#         S = self._init_sbox()
#         i = j = 0
#         result = []
#         for char in text:
#             i = (i + 1) % 256
#             j = (j + S[i]) % 256
#             S[i], S[j] = S[j], S[i]
#             t = (S[i] + S[j]) % 256
#             k = S[t]
#             result.append(chr(ord(char) ^ k))
#         return ''.join(result)


# key = "yudha"
# plaintext = "Halo, aku Yudha!"
# obj = RC4(key)

# ciphertext = RC4(key).crypt(plaintext)
# decrypted = RC4(key).crypt(ciphertext)

# print(f"Key: {obj.key}")
# print(f"Hail Enskripsi: {ciphertext}")
# print(f"Hasil Dekripsi: {decrypted}")

# SIMPLIER WITH COMMENT
# class RC4:
#     def __init__(self, key: str):
#         # ubah setiap karakter pada key jadi angka ASCII
#         self.key_bytes = [ord(character) for character in key]

#     def _init_sbox(self):
#         # buat sbox berisi angka 0 sampai 255
#         sbox = list(range(256))
#         key_index = 0

#         # proses KSA (Key Scheduling Algorithm) untuk ngacak isi sbox
#         for sbox_index in range(256):
#             key_index = (key_index + sbox[sbox_index] + self.key_bytes[sbox_index % len(self.key_bytes)]) % 256
#             # tukar nilai sbox[sbox_index] dengan sbox[key_index]
#             sbox[sbox_index], sbox[key_index] = sbox[key_index], sbox[sbox_index]
#         return sbox

#     def crypt(self, plaintext: str) -> str:
#         sbox = self._init_sbox()  # inisialisasi sbox
#         index_i = 0  # index i untuk PRGA
#         index_j = 0  # index j untuk PRGA
#         ciphertext_chars = []  # list buat simpan hasil enkripsi karakter demi karakter

#         for character in plaintext:
#             index_i = (index_i + 1) % 256
#             index_j = (index_j + sbox[index_i]) % 256
#             # tukar posisi sbox[index_i] dan sbox[index_j]
#             sbox[index_i], sbox[index_j] = sbox[index_j], sbox[index_i]

#             # ambil byte dari keystream
#             keystream_index = (sbox[index_i] + sbox[index_j]) % 256
#             keystream_byte = sbox[keystream_index]

#             # XOR karakter plaintext dengan keystream byte
#             encrypted_char = chr(ord(character) ^ keystream_byte)
#             ciphertext_chars.append(encrypted_char)

#         # gabungkan semua karakter terenkripsi jadi satu string
#         return ''.join(ciphertext_chars)