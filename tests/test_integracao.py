import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from calculadora import Calculadora

class TestCalculadoraIntegracao(unittest.TestCase):
    
    # 4.1 Teste de Operações Sequenciais
    
    def test_operacoes_sequenciais(self):
        calc = Calculadora()
        # Sequência: 2 + 3 = 5, depois 5 * 4 = 20, depois 20 / 2 = 10
        calc.somar(2, 3)
        resultado1 = calc.obter_ultimo_resultado()
        
        calc.multiplicar(resultado1, 4)
        resultado2 = calc.obter_ultimo_resultado()
        
        calc.dividir(resultado2, 2)
        resultado_final = calc.obter_ultimo_resultado()
        
        self.assertEqual(resultado_final, 10)
        self.assertEqual(len(calc.historico), 3)
    
    def test_operacoes_sequenciais_complexas(self):
        #Teste adicional: sequência mais complexa de operações
        calc = Calculadora()
        
        # (5 + 3) * 2 - 6 / 2 + 2^3
        calc.somar(5, 3)
        self.assertEqual(calc.obter_ultimo_resultado(), 8)
        
        calc.multiplicar(calc.obter_ultimo_resultado(), 2)
        self.assertEqual(calc.obter_ultimo_resultado(), 16)
        
        calc.dividir(6, 2)
        self.assertEqual(calc.obter_ultimo_resultado(), 3)
        
        calc.subtrair(16, calc.obter_ultimo_resultado())
        self.assertEqual(calc.obter_ultimo_resultado(), 13)
        
        calc.potencia(2, 3)
        self.assertEqual(calc.obter_ultimo_resultado(), 8)
        
        calc.somar(13, calc.obter_ultimo_resultado())
        self.assertEqual(calc.obter_ultimo_resultado(), 21)
        
        self.assertEqual(len(calc.historico), 6)
    
    # 4.2 Teste de Interface entre Métodos
    
    def test_integracao_historico_resultado(self):
        calc = Calculadora()
        calc.potencia(2, 3)  # 2^3 = 8
        calc.somar(calc.obter_ultimo_resultado(), 2)  # 8 + 2 = 10
        
        self.assertEqual(calc.obter_ultimo_resultado(), 10)
        self.assertEqual(len(calc.historico), 2)
        self.assertIn("2 ^ 3 = 8", calc.historico)
        self.assertIn("8 + 2 = 10", calc.historico)
    
    def test_integracao_todas_operacoes(self):
        #Teste adicional: integração usando todas as operações disponíveis
        calc = Calculadora()
        
        calc.somar(10, 5)
        calc.subtrair(calc.obter_ultimo_resultado(), 3)
        calc.multiplicar(calc.obter_ultimo_resultado(), 2)
        calc.dividir(calc.obter_ultimo_resultado(), 4)
        calc.potencia(calc.obter_ultimo_resultado(), 2)
        
        self.assertEqual(calc.obter_ultimo_resultado(), 36)
        self.assertEqual(len(calc.historico), 5)
        
        self.assertEqual(calc.historico[0], "10 + 5 = 15")
        self.assertEqual(calc.historico[1], "15 - 3 = 12")
        self.assertEqual(calc.historico[2], "12 * 2 = 24")
        self.assertEqual(calc.historico[3], "24 / 4 = 6.0")
        self.assertEqual(calc.historico[4], "6.0 ^ 2 = 36.0")