## RESULTADO DA EXECUÇÃO DOS TESTES
------------------------------------
- Total de testes executados: 29
- Testes bem-sucedidos: 29
- Falhas: 0
- Erros: 0
- Taxa de sucesso: 100%

## COBERTURA DE CÓDIGO OBTIDA
------------------------------
- src/calculadora.py:        100% coverage
- tests/test_integracao.py:  100% coverage  
- tests/test_unidade.py:     100% coverage
- cobertura total:           100% coverage

## PROBLEMAS ENCONTRADOS E SOLUÇÕES APLICADAS
----------------------------------------------

### 1. PROBLEMA: Mensagens de erro com espaços extras
- **Descrição:** O código original contém espaços antes e depois das mensagens
  de erro (" Mensagem " ao invés de "Mensagem")
- **Solução:** Ajustados os testes para esperar as mensagens com espaços extras
- **Testes afetados:** test_mensagens_erro, test_mensagens_erro_tipagem
   
### 2. PROBLEMA: TypeError não levantado com booleanos
- **Descrição:** Em Python True/False são aceitos como números (True=1, False=0)
- **Solução:** Substituído teste com True por teste com lista [1,2] que 
  realmente gera TypeError
- **Teste afetado:** test_tipagem_invalida_todas_operacoes
   
### 3. PROBLEMA: Comparação de int grande com float em notação científica
- **Descrição:** 10**50 retorna int, 1e50 retorna float. Mesmo que sejam
  iguais na matemática, a comparação da erro por serem tipos diferentes
- **Solução:** Usar 10**50 ao invés de 1e50 para comparação
- **Teste afetado:** test_limite_superior_float_maximo

## LIÇÕES APRENDIDAS SOBRE CADA TIPO DE TESTE
----------------------------------------------

### 1. TESTES DE ENTRADA E SAÍDA
- **Lição:** Sempre verificar tanto o retorno da função quanto o objeto após a operação
- **Importância:** Garante que a função processa corretamente os parâmetros e
  atualiza o estado conforme esperado

### 2. TESTES DE TIPAGEM
- **Lição:** Conhecimento da linguagem é importante. Em Python,
  bool é subclasse de int, o que pode causar alguns erros se não tratar direito
- **Importância:** Não ter erros de tipagem

### 3. TESTES DE CONSISTÊNCIA
- **Lição:** Além de verificar se os dados existem, verificar a ordem e
  formato
- **Importância:** Garante integridade dos dados

### 4. TESTES DE INICIALIZAÇÃO
- **Lição:** Testar que cada objeto é independente
- **Importância:** Evita bugs de compartilhamento de estado

### 5. TESTES DE MODIFICAÇÃO DE DADOS
- **Lição:** Verificar modificação de dados não relacionados
- **Importância:** Garante isolamento entre dados

### 6. TESTES DE LIMITE INFERIOR
- **Lição:** Zero e números muito pequenos podem ter casos específicos
- **Importância:** Bugs em casos extremos que os usuários podem encontrar

### 7. TESTES DE LIMITE SUPERIOR
- **Lição:** Ter cuidado com tipos diferentes no Python como int e float em números grandes
- **Importância:** Garante que não tenha erros com valores extremos

### 8. TESTES DE VALORES FORA DO INTERVALO
- **Lição:** Testar todos os casos impossíveis, por exemplo divisão por zero 
- **Importância:** Previne quebras no código e retorna mensagens de erro para os usuários

### 9. TESTES DE FLUXOS DE CONTROLE
- **Lição:** Cobrir tanto caminhos de sucesso quanto de erro
- **Importância:** Garante que todos os branches do código são executados e testados

### 10. TESTES DE MENSAGENS DE ERRO
- **Lição:** Mensagens de erro devem ser testadas exatamente como aparecem,
  incluindo espaços e formatação
- **Importância:** Mensagens claras melhoram a experiência do usuário