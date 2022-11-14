# Questão 1
# Aluno: João Victor Amaral de Oliveira
# RU:3973030

valor_unitario = float(input('Entre com o valor do produto: '))  # Define a variavel valor_unitario
quantidade = int(input('Entre com o valor da quantidade: '))  # Define a variavel quantidade
valor_frete = 0  # Variavel que receberá o valor do frete dependendo da quantidade de

if 0 <= quantidade < 11:
    valor_frete = 30
elif 11 <= quantidade < 101:
    valor_frete = 60
elif 101 <= quantidade < 1001:
    valor_frete = 120
else:
    valor_frete = 240

valor_parcial = float(valor_unitario * quantidade)  # Define a variavel valor_parcial com o valor
valor_total = float(valor_parcial + valor_frete)  # Define a variavel valor_total com o valor

print('O valor sem frete foi: R$ {:.2f}'.format(valor_parcial))  # imprime o valor_parcial formatado
print('O valor com desconto foi: R$ {:.2f} '.format(valor_total) + '(frete de R$ {:.2f})'.format(valor_frete))