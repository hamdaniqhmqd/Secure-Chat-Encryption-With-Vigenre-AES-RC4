from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import binascii
import base64


def simple_hash(data):
    if isinstance(data, str):
        data = data.encode('Windows-1252')

    result = bytearray([0x42] * 32)

    if not data:
        data = b'\x00'

    for i, byte in enumerate(data):
        pos = i % 32
        result[pos] = (result[pos] + byte + i) % 256

    for _ in range(8):
        for i in range(32):
            prev = (i - 1) % 32
            next_pos = (i + 1) % 32
            result[i] = (result[i] + result[prev]) % 256
            result[i] = (result[i] ^ result[next_pos]) % 256

    return bytes(result)


class AESCipher:
    def __init__(self, user_id: str):
        hashed = simple_hash(user_id)
        self.key = hashed[:16]
        self.iv = hashed[16:32]

    def _print_block(self, title, block):
        print(f"{title}: {binascii.hexlify(block).decode().upper()}")

    def encrypt(self, plaintext: str | bytes, output_format='bytes') -> bytes | str:
        if isinstance(plaintext, str):
            plaintext = plaintext.encode('Windows-1252')

        padded = pad(plaintext, AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        ciphertext = cipher.encrypt(padded)

        # print("\n==== PROSES ENKRIPSI AES-128 ====")
        # self._print_block("Key", self.key)
        # self._print_block("IV", self.iv)
        # self._print_block("Plaintext (Hex)", padded)
        # self._print_block("Ciphertext", ciphertext)

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
            # print("\n==== PROSES DEKRIPSI AES-128 ====")
            # self._print_block("Key", self.key)
            # self._print_block("IV", self.iv)
            # self._print_block("Ciphertext", ciphertext)
            # self._print_block("Decrypted Plaintext (Hex)", plaintext)
            # print(f"Decrypted Plaintext: {plaintext.decode(errors='ignore')}")
            return plaintext
        except ValueError:
            print("Error: Padding is incorrect. Data mungkin rusak atau kunci salah.")
            return b''
