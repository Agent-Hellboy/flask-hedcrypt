import os, random, struct
import sys
from Crypto.Cipher import AES


class FileEncryptDecrypt:
    """
    class which provide APIs for file encryption and decryption.
    """

    def __init__(self, key):
        self.key = key
        if not isinstance(self.key, bytes):
            self.key = key.encode("utf-8")

        print(self.key)

    def encrypt_file(self, in_filename, out_filename=None, chunksize=64 * 1024):
        # used to encrypt the file
        l = in_filename.split(".")
        if not out_filename:
            out_filename = l[0] + ".enc"

        # iv = ''.join(chr(random.randint(0, 0xFF)) for i in range(16))
        iv = os.urandom(16)
        # print(sys.getsizeof(iv))
        encryptor = AES.new(self.key, AES.MODE_CBC, iv)
        filesize = os.path.getsize(in_filename)

        with open(in_filename, "rb") as infile:
            with open(out_filename, "wb") as outfile:
                outfile.write(
                    struct.pack("<Q", filesize)
                )  # <Q little-endian unsigned long long formatting
                outfile.write(iv)

                while True:
                    chunk = infile.read(chunksize)
                    if len(chunk) == 0:
                        break
                    elif len(chunk) % 16 != 0:
                        chunk += b" " * (16 - len(chunk) % 16)

                    outfile.write(encryptor.encrypt(chunk))

    def decrypt_file(self, in_filename, out_filename=None, chunksize=24 * 1024):
        """ Decrypts a file using AES (CBC mode) with the
            given key. Parameters are similar to encrypt_file,
            with one difference: out_filename, if not supplied
            will be in_filename without its last extension
            (i.e. if in_filename is 'pg.pdf.enc' then
            out_filename will be 'pg.pdf')
        """
        if not out_filename:
            out_filename = os.path.splitext(in_filename)[0] + ".pdf"

        with open(in_filename, "rb") as infile:
            origsize = struct.unpack("<Q", infile.read(struct.calcsize("Q")))[0]
            iv = infile.read(16)
            decryptor = AES.new(self.key, AES.MODE_CBC, iv)

            with open("after_decryption.pdf", "wb") as outfile:
                while True:
                    chunk = infile.read(chunksize)
                    if len(chunk) == 0:
                        break
                    outfile.write(decryptor.decrypt(chunk))

                outfile.truncate(origsize)
