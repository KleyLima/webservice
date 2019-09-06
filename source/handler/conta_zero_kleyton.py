# coding: utf-8

from sys import argv
from re import findall


class ContaZero:
    def __init__(self, num):
        self.num = num

    def conta_zeros(self):
        zeros = findall("0+", self.num)
        if len(zeros) != 0:
            occur = [len(_) for _ in zeros]
            return max(occur)
        else:
            return 0


if __name__ == '__main__':
    print(ContaZero(str(argv[1:])).conta_zeros())
