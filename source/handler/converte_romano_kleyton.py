# coding: utf-8

from functools import reduce
#from source.ref import Ref
from sys import argv


class Roman:

    def __init__(self, num):
        self.num = num

    def valida_numero(self):
        if int(self.num) > 0 and int(self.num) < 4000:
            return True
        else:
            return False

    def numero_para_romano(self):
        if self.valida_numero():
            lst = []
            for ind, num in enumerate(self.num[::-1]):
                if int(num)>=1 and int(num)<=3:
                    for _ in range(int(num)):
                        #lst.append(Roman.get_num(self, ind=ind, num=int(num)))
                        lst.append(Roman.get_num(self, ind=ind, num=1))
                elif num == '4':
                    lst.append(Roman.get_num(self, ind=ind, num=1))
                    lst.append(Roman.get_num(self, ind=ind, num=5))
                elif int(num) >= 5 and int(num) <= 8:
                    lst.append(Roman.get_num(self, ind=ind, num=5))
                    for _ in range(int(num) - 5):
                        lst.append(Roman.get_num(self, ind=ind, num=1))
                elif int(num) == 9:
                    lst.append(Roman.get_num(self, ind=ind+1, num=1))
                    lst.append(Roman.get_num(self, ind=ind, num=1))
                else:
                    pass
       
            reduce(lambda a, b: b + a, lst)
            result = (reduce(lambda a, b: b + a, lst))
            return result
        else:
            print("Número Inválido.")

        

    def get_num(self, ind, num):
        return Ref.ref[ind][num]


if __name__ == '__main__':
    #Roman(input()).serial()
    from os import getcwd
    print(getcwd())

    #from ref import Ref
    print(Roman(argv[1]).numero_para_romano())     # alternativa para execução pelo terminal, remover "source." do import
else:
    #from source.ref import Ref
    from handler.ref import Ref
    from os import getcwd
    print(getcwd())
