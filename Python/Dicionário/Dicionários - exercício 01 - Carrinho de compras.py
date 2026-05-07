# Dicionários - exercício 01 - Carrinho de compras - 31/10/2024

# Implemente um sitema de carrinho de compras de loja virtual.
# Pergunte quais produtos deseja adicionar no carrinho até que digite fim.
# No fim, calcule o total a pagar, considerando os preços dos produtos e a
# quantidade do produto no carrinho.


tabela = {'Alface': 1.45, 'Batata': 1.20,
          'Tomate': 2.3, 'Feijão': 1.50,
          'Milho': 2.50, 'Arroz': 3.45,
          'Ervilha': 5.67}

carrinho = {'Tomate': 5.0, 'Arroz': 10.0, 'Feijão': 8.0, 'Milho': 6.0}

print ('''TABELA DE PRODUTOS
Produto --- Preço''')

for produto, preço in tabela.items():
    print (f'{produto} --- R$ {preço:.2f}', end='\n')
print()



while True:
    produto = input('Digite um produto disponível na lista ou, então, digite "Fim" para finalizar a compra: ').capitalize()
    print()
    if produto.upper() == 'FIM':
        break
    elif produto in tabela:
        quantidade = float(input(f'Digite a quantidade de {produto}: '))
        if produto in carrinho:
            carrinho[produto] += carrinho[produto]
        else:
            carrinho[produto] = quantidade
    else:
        produto = input('Por favor, digite um produto válido, o qual deve estar na tabela: ')

total = 0

for produto, quantidade in carrinho.items():
    preço = tabela[produto]
    subtotal = preço * quantidade
    total += subtotal

print (f'O total de sua compra é de R$ {total:.2f}.')
