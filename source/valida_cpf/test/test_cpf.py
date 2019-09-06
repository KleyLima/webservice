# coding: utf-8

import unittest
from source.valida import ValidaCPF


class Test_cpf(unittest.TestCase):


    def test_retira_formatacao(self):
        """
        Método para teste da função de retirada de formatação.
        """
        self.assertEqual(ValidaCPF("123.456.789-10").retira_formatacao(), "12345678910")  # padrão
        self.assertEqual(ValidaCPF("12345678910").retira_formatacao(), "12345678910")  # sem formatação
        self.assertEqual(ValidaCPF("123/456*789.10").retira_formatacao(), "12345678910")  # mista
        self.assertEqual(ValidaCPF("12*34&56#789@10").retira_formatacao(), "12345678910")  # overformated
        self.assertEqual(ValidaCPF("003+456;7@89/10").retira_formatacao(), "00345678910")  # antigo, overformated
        self.assertEqual(ValidaCPF("3+456;7@89/10").retira_formatacao(), "345678910")  # antigo, over, sem zeros inicio
    def test_valida_cpf(self):
        """
        Método para teste da função de validação de CPF.
        """
        self.assertFalse(ValidaCPF("11111111111").valida_cpf())  # verificação ok, mas não passa
        self.assertTrue(ValidaCPF("52998224725").valida_cpf())  # Válido
        self.assertTrue(ValidaCPF("00351655964").valida_cpf())  # Antigo válido dois zeros
        self.assertFalse(ValidaCPF("00351855964").valida_cpf())  # Antigo inválido dois zeros
        self.assertTrue(ValidaCPF("351655964").valida_cpf())  # Antigo válido omite dois zeros
        self.assertFalse(ValidaCPF("351659964").valida_cpf())  # Antigo inválido omite dois zeros
        self.assertTrue(ValidaCPF("00034452915").valida_cpf())  # Antigo válido três zeros
        self.assertFalse(ValidaCPF("00034452919").valida_cpf())  # Antigo inválido três zeros
        self.assertTrue(ValidaCPF("34452915").valida_cpf())  # Antigo válido omite três zeros
        self.assertFalse(ValidaCPF("34452919").valida_cpf())  # Antigo inválido omite três zeros


if __name__ == '__main__':
    unittest.main()
