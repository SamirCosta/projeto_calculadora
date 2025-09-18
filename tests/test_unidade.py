import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from calculadora import Calculadora

class TestesUnitarios(unittest.TestCase):
    
    # 3.1 Testes de Entrada e Saída
    
    def test_entrada_saida_soma(self):
        # Teste de entrada e saída para soma
        calc = Calculadora()
        resultado = calc.somar(5, 3)
        self.assertEqual(resultado, 8)
        self.assertEqual(calc.obter_ultimo_resultado(), 8)
    
    def test_entrada_saida_subtracao(self):
        # Teste de entrada e saída para subtração
        calc = Calculadora()
        resultado = calc.subtrair(10, 3)
        self.assertEqual(resultado, 7)
        self.assertEqual(calc.obter_ultimo_resultado(), 7)
    
    def test_entrada_saida_multiplicacao(self):
        # Teste de entrada e saída para multiplicação
        calc = Calculadora()
        resultado = calc.multiplicar(4, 5)
        self.assertEqual(resultado, 20)
        self.assertEqual(calc.obter_ultimo_resultado(), 20)
    
    def test_entrada_saida_divisao(self):
        # Teste de entrada e saída para divisão
        calc = Calculadora()
        resultado = calc.dividir(20, 4)
        self.assertEqual(resultado, 5)
        self.assertEqual(calc.obter_ultimo_resultado(), 5)
    
    def test_entrada_saida_potencia(self):
        # Teste adicional: entrada e saída para potência
        calc = Calculadora()
        resultado = calc.potencia(2, 3)
        self.assertEqual(resultado, 8)
        self.assertEqual(calc.obter_ultimo_resultado(), 8)
    
    # 3.2 Testes de Tipagem
    
    def test_tipagem_invalida(self):
        # Teste de tipagem com valores inválidos
        calc = Calculadora()
        with self.assertRaises(TypeError):
            calc.somar("5", 3)  # String no lugar de número
        with self.assertRaises(TypeError):
            calc.dividir(10, None)  # None no lugar de número
    
    def test_tipagem_invalida_todas_operacoes(self):
        # Teste de tipagem para todas as operações
        calc = Calculadora()
        
        # Teste soma
        with self.assertRaises(TypeError):
            calc.somar("abc", 5)
        with self.assertRaises(TypeError):
            calc.somar(5, [1, 2, 3])
            
        # Teste subtração
        with self.assertRaises(TypeError):
            calc.subtrair(None, 5)
        with self.assertRaises(TypeError):
            calc.subtrair(5, {"chave": "valor"})
            
        # Teste multiplicação
        with self.assertRaises(TypeError):
            calc.multiplicar([1, 2], 5)
        with self.assertRaises(TypeError):
            calc.multiplicar(5, "texto")
            
        # Teste divisão
        with self.assertRaises(TypeError):
            calc.dividir([], 5)
        with self.assertRaises(TypeError):
            calc.dividir(5, None)
            
        # Teste potência
        with self.assertRaises(TypeError):
            calc.potencia("2", 3)
        with self.assertRaises(TypeError):
            calc.potencia(2, "3")
    
    def test_tipagem_com_booleanos(self):
        # Teste adicional: tipagem com valores booleanos
        calc = Calculadora()
        resultado = calc.somar(True, False)
        self.assertEqual(resultado, 1)
    
    # 3.3 Testes de Consistência
    
    def test_consistencia_historico(self):
        # Teste de consistência do histórico
        calc = Calculadora()
        calc.somar(2, 3)
        calc.multiplicar(4, 5)
        self.assertEqual(len(calc.historico), 2)
        self.assertIn("2 + 3 = 5", calc.historico)
        self.assertIn("4 * 5 = 20", calc.historico)
    
    def test_consistencia_ordem_historico(self):
        # Teste adicional: verifica se a ordem do histórico é mantida
        calc = Calculadora()
        calc.somar(1, 1)
        calc.subtrair(5, 3)
        calc.multiplicar(2, 3)
        calc.dividir(10, 2)
        calc.potencia(2, 4)
        
        self.assertEqual(len(calc.historico), 5)
        self.assertEqual(calc.historico[0], "1 + 1 = 2")
        self.assertEqual(calc.historico[1], "5 - 3 = 2")
        self.assertEqual(calc.historico[2], "2 * 3 = 6")
        self.assertEqual(calc.historico[3], "10 / 2 = 5.0")
        self.assertEqual(calc.historico[4], "2 ^ 4 = 16")
    
    # 3.4 Testes de Inicialização
    
    def test_inicializacao(self):
        # Teste de inicialização da calculadora
        calc = Calculadora()
        self.assertEqual(calc.resultado, 0)
        self.assertEqual(len(calc.historico), 0)
    
    def test_inicializacao_multiplas_instancias(self):
        # Teste adicional: verifica independência entre instâncias
        calc1 = Calculadora()
        calc2 = Calculadora()
        
        calc1.somar(5, 3)
        
        self.assertEqual(calc1.resultado, 8)
        self.assertEqual(calc2.resultado, 0)
        self.assertEqual(len(calc1.historico), 1)
        self.assertEqual(len(calc2.historico), 0)
    
    # 3.5 Testes de Modificação de Dados
    
    def test_modificacao_historico(self):
        # Teste de modificação do histórico
        calc = Calculadora()
        calc.somar(1, 1)
        self.assertEqual(len(calc.historico), 1)
        calc.limpar_historico()
        self.assertEqual(len(calc.historico), 0)
    
    def test_modificacao_resultado_permanece(self):
        # Teste adicional: verifica se resultado permanece após limpar histórico
        calc = Calculadora()
        calc.somar(10, 20)
        resultado_antes = calc.obter_ultimo_resultado()
        calc.limpar_historico()
        resultado_depois = calc.obter_ultimo_resultado()
        
        self.assertEqual(resultado_antes, resultado_depois)
        self.assertEqual(resultado_depois, 30)
        self.assertEqual(len(calc.historico), 0)
    
    # 3.6 Testes de Limite Inferior
    
    def test_limite_inferior(self):
        # Teste com valores mínimos
        calc = Calculadora()
        # Teste com zero
        resultado = calc.somar(0, 5)
        self.assertEqual(resultado, 5)
        # Teste com números negativos muito pequenos
        resultado = calc.multiplicar(-1e-10, 2)
        self.assertEqual(resultado, -2e-10)
    
    def test_limite_inferior_negativos(self):
        # Teste adicional: operações com números negativos grandes
        calc = Calculadora()
        
        # Teste com números negativos
        resultado = calc.somar(-1000, -2000)
        self.assertEqual(resultado, -3000)
        
        # Teste com números próximos ao menor float
        resultado = calc.multiplicar(-1e308, 0.5)
        self.assertEqual(resultado, -5e307)
        
        # Teste subtração com negativos
        resultado = calc.subtrair(-100, -50)
        self.assertEqual(resultado, -50)
    
    # 3.7 Testes de Limite Superior
    
    def test_limite_superior(self):
        # Teste com valores máximos
        calc = Calculadora()
        # Teste com números grandes
        resultado = calc.somar(1e10, 1e10)
        self.assertEqual(resultado, 2e10)
    
    def test_limite_superior_float_maximo(self):
        # Teste adicional: valores próximos ao limite máximo de float
        calc = Calculadora()
        
        # Teste com números muito grandes (próximos ao limite de float)
        resultado = calc.somar(1e308, 1e307)
        self.assertAlmostEqual(resultado, 1.1e308, places=293)
        
        # Teste multiplicação com números grandes
        resultado = calc.multiplicar(1e100, 1e100)
        self.assertEqual(resultado, 1e200)
        
        # Teste potência com resultado grande
        resultado = calc.potencia(10, 50)
        self.assertEqual(resultado, 10**50)
    
    # 3.8 Testes de Valores Fora do Intervalo
    
    def test_divisao_por_zero(self):
        # Teste de divisão por zero
        calc = Calculadora()
        with self.assertRaises(ValueError):
            calc.dividir(10, 0)
    
    def test_divisao_zero_por_numero(self):
        # Teste adicional: divisão de zero por número
        calc = Calculadora()
        resultado = calc.dividir(0, 5)
        self.assertEqual(resultado, 0)
    
    def test_potencia_com_expoente_negativo(self):
        # Teste adicional: potência com expoente negativo
        calc = Calculadora()
        resultado = calc.potencia(2, -3)
        self.assertEqual(resultado, 0.125)  # 2^-3 = 1/8 = 0.125
    
    # 3.9 Testes de Fluxos de Controle
    
    def test_fluxos_divisao(self):
        # Teste de diferentes fluxos na divisão
        calc = Calculadora()
        # Caminho normal
        resultado = calc.dividir(10, 2)
        self.assertEqual(resultado, 5)
        # Caminho de erro
        with self.assertRaises(ValueError):
            calc.dividir(10, 0)
    
    def test_fluxos_todas_operacoes(self):
        # Teste adicional: fluxos de todas as operações
        calc = Calculadora()
        
        # Fluxo normal de soma
        self.assertEqual(calc.somar(3, 4), 7)
        # Fluxo de erro de soma
        with self.assertRaises(TypeError):
            calc.somar("3", 4)
        
        # Fluxo normal de subtração
        self.assertEqual(calc.subtrair(10, 3), 7)
        # Fluxo de erro de subtração
        with self.assertRaises(TypeError):
            calc.subtrair(10, "3")
        
        # Fluxo normal de multiplicação
        self.assertEqual(calc.multiplicar(3, 4), 12)
        # Fluxo de erro de multiplicação
        with self.assertRaises(TypeError):
            calc.multiplicar(None, 4)
        
        # Fluxo normal de potência
        self.assertEqual(calc.potencia(2, 3), 8)
        # Fluxo de erro de potência
        with self.assertRaises(TypeError):
            calc.potencia(2, "3")
    
    # 3.10 Testes de Mensagens de Erro
    
    def test_mensagens_erro(self):
        # Teste de mensagens de erro
        calc = Calculadora()
        try:
            calc.dividir(5, 0)
        except ValueError as e:
            self.assertEqual(str(e), " Divisao por zero nao permitida ")
    
    def test_mensagens_erro_tipagem(self):
        # Teste adicional: mensagens de erro de tipagem
        calc = Calculadora()
        
        # Teste mensagem de erro para tipo inválido em soma
        try:
            calc.somar("texto", 5)
        except TypeError as e:
            self.assertEqual(str(e), " Argumentos devem ser numeros ")
        
        # Teste mensagem de erro para tipo inválido em divisão
        try:
            calc.dividir(10, None)
        except TypeError as e:
            self.assertEqual(str(e), " Argumentos devem ser numeros ")
        
        # Teste mensagem de erro para tipo inválido em potência
        try:
            calc.potencia([], 2)
        except TypeError as e:
            self.assertEqual(str(e), " Argumentos devem ser numeros ")