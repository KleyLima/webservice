# coding: utf-8

from random import randrange

class GeraSenha:
    def gera_senha(self):
        res = ""
        for _ in range(randrange(2,30)):
            res+="".join([sym for sym in chr(randrange(32, 127))])
        return res

if __name__ == '__main__':
    print(GeraSenha().gera_senha())

