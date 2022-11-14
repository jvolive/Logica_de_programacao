# Questão 2
# Aluno: João Victor Amaral de Oliveira
# RU:3973030

tamanho = ['P', 'M', 'G'] # Tabela

# Código: TR = Sabores Tradicionais - ES = Sabores Especiais - PR = Sabores Premium
codigos = {'TR': [6.00, 10.00, 18.00],
          'ES': [7.00, 12.00, 21.00],
          'PR': [8.00, 14.00, 21.00]}

compra = [] #Pedido

while True:
    qual_tamanho = input('Qual o tamanho do sorvete desejado? (P, M, G) '
    '>>')
    qual_sabor = input('Qual o código do sorvete desejado? TR = Sabores Tradicionais - ES = Sabores Especiais - PR = Sabores Premium'
    '>>')
    
    if qual_tamanho in tamanho and qual_sabor in codigos:
        pedido = codigos[qual_sabor][tamanho.index(qual_tamanho)]
        compra.append(pedido)
        resposta = input('Deseja mais alguma?\n'
    'Digite (S) para continuar...\n'
    'Ou pressione qualquer tecla para fechar a conta...\n')
    elif algo_mais.upper() == 'S':
        continue
    elif erro:
        print('Tamanho ou Código inválido(s)!')
        continue
    else:
        print ("Valor total da compra:", "R$",sum(compra))
        break

