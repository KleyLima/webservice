# -*- coding: utf-8 -*-

from hashlib import sha256, md5
from sys import argv

class HashSenha:
    def __init__(self, pwd):
        self.pwd = pwd

    def hash_md5(self):
        code = md5((self.pwd).encode())  # Transforma a senha dada em bytes e aplica o md5
        return code.hexdigest()  # Retorna o hash da string de senha em hexadecimal

    def hash_sha256(self):
        code = sha256((self.pwd).encode())  # Transforma a senha em uma string de bytes e aplica o algoritmo sha256
        return code.hexdigest()

if __name__ == '__main__':
    print(HashSenha(argv[1]).hash_md5())
    print(HashSenha(argv[1]).hash_sha256())

