# coding: utf-8

import unittest
from source.converte_romano_kleyton import Roman

class TesteRomano(unittest.TestCase):
    def test_valida_numero(self):
        self.assertFalse(Roman("4000").valida_numero())  # maior que 3999
        self.assertFalse(Roman("0").valida_numero())  # zero
        self.assertFalse(Roman("-50").valida_numero())  # negativo
        self.assertTrue(Roman("2019").valida_numero())  # caso válido

    def teste_numero_para_romano(self):
        self.assertEqual(Roman("2019").numero_para_romano(),'MMXIX')  # teste de resultado
        self.assertEqual('MMMCMXCIX', Roman("3999").numero_para_romano())  # teste 3999
        self.assertNotEqual('IIV', Roman("3").numero_para_romano())  # Teste lógica subtração

if __name__ == "__main__":
    unittest.main()

