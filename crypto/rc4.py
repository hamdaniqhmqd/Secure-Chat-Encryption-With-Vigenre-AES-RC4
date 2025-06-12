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
#         idx = 0  

#         for character in plaintext:
#             index_i = (index_i + 1) % 256
#             index_j = (index_j + sbox[index_i]) % 256
#             sbox[index_i], sbox[index_j] = sbox[index_j], sbox[index_i]

#             keystream_index = (sbox[index_i] + sbox[index_j]) % 256
#             keystream_byte = sbox[keystream_index]

#             encrypted_char = chr(ord(character) ^ keystream_byte)
#             ciphertext_chars.append(encrypted_char)

#             print(f"[{idx}] '{character}' -> ord: {ord(character)} | keystream: {keystream_byte} | XOR result: {ord(character) ^ keystream_byte} -> '{encrypted_char}'")
#             idx += 1  

#         return ''.join(ciphertext_chars)

# key = "yudha"
# plaintext = "aku yudha"
# obj = RC4(key)
# sbox = obj._init_sbox()

# ciphertext = obj.crypt(plaintext)
# decrypted = obj.crypt(ciphertext)

# print(f"\nKey: {obj.key_bytes}\n")
# print(f"SBox: {sbox}\n")
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


# class RC4:
#     def __init__(self, key: str):
#         # konstruktor RC4: menerima input key dalam bentuk string
#         # setiap karakter pada string key diubah menjadi nilai ASCII-nya menggunakan ord()
#         # misal: key = "abc" -> [97, 98, 99]
#         self.key_bytes = [ord(character) for character in key]

#     def _init_sbox(self):
#         # membuat list sbox berisi angka 0 sampai 255 (total 256 nilai)
#         sbox = list(range(256))

#         # key_index digunakan untuk melacak posisi index dari key saat mengacak sbox
#         key_index = 0

#         # algoritma KSA (Key Scheduling Algorithm)
#         # proses pengacakan elemen-elemen di dalam sbox berdasarkan isi key
#         for i in range(256):
#             # menghitung index baru berdasarkan sbox saat ini dan karakter key
#             # i % len(self.key_bytes): memastikan pengaksesan key berulang jika key lebih pendek dari 256
#             key_index = (key_index + sbox[i] + self.key_bytes[i % len(self.key_bytes)]) % 256

#             # pertukaran posisi antara elemen sbox[i] dengan sbox[key_index] (proses swap)
#             # fungsi tuple swap di Python:
#             # x, y = y, x akan menukar nilai x dan y secara langsung
#             sbox[i], sbox[key_index] = sbox[key_index], sbox[i]

#         # setelah proses KSA selesai, sbox akan berisi susunan acak berdasarkan key
#         return sbox

#     def crypt(self, plaintext: str) -> str:
#         # memanggil _init_sbox untuk mendapatkan sbox hasil KSA
#         sbox = self._init_sbox()

#         # index_i dan index_j digunakan pada algoritma PRGA (Pseudo-Random Generation Algorithm)
#         index_i = 0
#         index_j = 0

#         # list kosong untuk menyimpan hasil enkripsi karakter demi karakter
#         ciphertext_chars = []

#         # proses PRGA dimulai, untuk setiap karakter di plaintext
#         for character in plaintext:
#             # index_i terus bertambah 1 (dan dibungkus 256 agar tetap dalam rentang 0-255)
#             index_i = (index_i + 1) % 256

#             # index_j dihitung berdasarkan nilai sbox saat ini
#             index_j = (index_j + sbox[index_i]) % 256

#             # pertukaran sbox[index_i] dan sbox[index_j] untuk menjaga keacakan
#             sbox[index_i], sbox[index_j] = sbox[index_j], sbox[index_i]

#             # menentukan keystream index dari hasil penjumlahan sbox[index_i] dan sbox[index_j]
#             keystream_index = (sbox[index_i] + sbox[index_j]) % 256

#             # ambil byte dari sbox berdasarkan keystream_index sebagai byte kunci (keystream_byte)
#             keystream_byte = sbox[keystream_index]

#             # enkripsi karakter dengan operasi XOR antara byte plaintext dan byte keystream
#             # ord(character): mengubah karakter ke nilai ASCII
#             # chr(...): mengubah hasil XOR kembali ke karakter
#             encrypted_char = chr(ord(character) ^ keystream_byte)

#             # simpan karakter terenkripsi ke dalam list ciphertext_chars
#             ciphertext_chars.append(encrypted_char)

#         # gabungkan semua karakter terenkripsi menjadi satu string dengan ''.join()
#         return ''.join(ciphertext_chars)
