# Dicionários - exercício 02 - 06/11/2024
# Carrinho de compras e Sistema de Estoque

# Implementar um controle de estoque dos produtos, com lista dentro de dicionário
# Anterior:
# Implemente um sitema de carrinho de compras de loja virtual.
# Pergunte quais produtos deseja adicionar no carrinho até que digite fim.
# No fim, calcule o total a pagar, considerando os preços dos produtos e a
# quantidade do produto no carrinho.

tabela = {'alface': [1.45, 50], 'batata': [1.20, 250],
          'tomate': [2.30, 380], 'feijão': [1.50, 1000],
          'milho': [2.50, 15], 'arroz': [3.45, 700],
          'ervilha': [5.67, 20]}

carrinho = {'tomate': 5.0, 'arroz': 10.0, 'feijão': 8.0, 'milho': 6.0}

print ('''TABELA DE PRODUTOS
Produto --- Preço''')

for produto, preço in tabela.items():
    print (f'{produto} --- R$ {preço[0]:.2f}', end='\n')
print()

while True:
    produto = input('Digite um produto disponível na lista ou, então, digite "Fim" para finalizar a compra: ').lower()
    print()
    if produto.upper() == 'FIM':
        break
    elif produto in tabela:
        if produto in carrinho:
            while True:
                try:
                    quantidade = float(input(f'Digite a quantidade de {produto} que esteja disponível no estoque: '))
                except:
                    quantidade = float(input(f'Digite uma quantidade, em números, válida: '))
                if quantidade + carrinho[produto] > tabela[produto][1]:
                    try:
                        quantidade = float(input(f'Esta quantidade estrapola o nosso estoque de {produto}, que é de {tabela[produto][1]} Kg. E, portanto, por favor, escolha uma quantidade menor: '))  
                    except:
                        quantidade = float(input(f'Digite uma quantidade, em números, válida: '))
                else:
                    carrinho[produto] += carrinho[produto]
                    break
        else:
            while True:
                try:
                    quantidade = float(input(f'Digite a quantidade de {produto} que esteja disponível no estoque: '))
                except:
                    quantidade = float(input(f'Digite uma quantidade, em números, válida: '))
                if quantidade > tabela[produto][1]:
                    try:
                        quantidade = float(input(f'Esta quantidade estrapola o nosso estoque de {produto}, que é de {tabela[produto][1]}. Portanto, por favor, escolha uma quantidade menor: '))
                    except:
                        quantidade = float(input(f'Digite uma quantidade, em números, válida: '))
                else:
                    carrinho[produto] = quantidade
                    break
    else:
        produto = input('Por favor, digite um produto válido, o qual deve estar na tabela: ')

total = 0

for produto, quantidade in carrinho.items():
    tabela[produto][1] -= quantidade
    preço = tabela[produto][0]
    subtotal = preço * quantidade
    total += subtotal

print (f'O total de sua compra é de R$ {total:.2f}.')

