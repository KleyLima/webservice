# coding: utf-8

from sys import argv
from functools import reduce
from re import sub


class ValidaCPF:
    def __init__(self, num_cpf):
        self.num_cpf = num_cpf

    def valida_cpf(self):
        self.num_cpf = self.retira_formatacao()
        cpf = [int(num) for num in self.num_cpf.zfill(11)]
        if len(set(cpf)) != 1:
            first_check = int(
                (10 * reduce(lambda a, b: a + b, [x * y for x, y in zip(cpf[:9], range(10, 1, -1))])) % 11)
            if first_check == cpf[9]:
                sec_check = int(
                    10 * reduce(lambda a, b: a + b, [x * y for x, y in zip(cpf[:10], range(11, 1, -1))])) % 11
                if sec_check == cpf[10]:
                    print("O CPF {} é válido.".format(self.num_cpf))
                    return True
                else:
                    print("O CPF {} não  é válido.".format(self.num_cpf))
            else:
                print("O CPF {} não é válido".format(self.num_cpf))
        else:
            print("O CPF {} não é válido.".format(self.num_cpf))

    def retira_formatacao(self):
        cpf = sub('\D', '', self.num_cpf)
        return cpf


if __name__ == '__main__':
    print("CPF: {}".format(ValidaCPF(argv[1]).retira_formatacao()))
    ValidaCPF(argv[1]).valida_cpf()
