# coding: utf-8

from re import findall
from sys import argv

class ClassificaSenha:
    def __init__(self, pwd):
        self.pwd = pwd

    def classifica_senha(self):
        """
        Método para a classificação de senha. São requeridos um minimo de 8 caracteres para a senha ser aceita.
        Ser minimamente aceita a classifica como fraca, para média e forte deve-se fazer uso de números e caracteres
        especiais. Uma senha de 9 caracteres no total contendo num, letras e simbolos é forte. O mesmo caso usando
        letras e números apenas é classificada como média.
        """
        lvl = 0
        if len(self.pwd) > 7:  # Checa tamanho min. da senha
            lvl = lvl + 1 if findall('\w\D', self.pwd) else lvl  # checa letras
            lvl = lvl + 1 if findall('\d', self.pwd) else lvl  # checa num
            lvl = lvl + 1 if findall('\W', self.pwd) else lvl  # checa símbolos
            return lvl - 1


if __name__ == '__main__':
    print(ClassificaSenha(argv[1]).classifica_senha())
