# O cardápio de uma lanchonete é o seguinte:
# Especificação   Código  Preço
# Cachorro Quente 100     R$ 1,20
# Bauru Simples   101     R$ 1,30
# Bauru com ovo   102     R$ 1,50
# Hambúrguer      103     R$ 1,20
# Cheeseburguer   104     R$ 1,30
# Refrigerante    105     R$ 1,00
# Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido.
# Considere que o cliente deve informar quando o pedido deve ser encerrado.

print ('''----Cardápio----
Especificação   Código  Preço
Cachorro Quente 100     R$ 1,20
Bauru Simples   101     R$ 1,30
Bauru com ovo   102     R$ 1,50
Hambúrguer      103     R$ 1,20
Cheeseburguer   104     R$ 1,30
Refrigerante    105     R$ 1,00
''')

quantidade100 = 0 # denominando todas as quantidades de cada item
quantidade101 = 0
quantidade102 = 0
quantidade103 = 0
quantidade104 = 0
quantidade105 = 0

while True: # enquanto não for emitido o break do encerramento do pedido, esse é o "ínicio" do programa.
    comida = int (input ('Digite o código do item desejado: '))  
    while comida not in (100, 101, 102,103, 104, 105): 
        comida = int(input ('Por favor, digite uma comida existente: '))
    quantidade = int (input ('Digite a quantidade do item já selecionado: ')) 
    while quantidade < 0:
        quantidade = int (input ('Por favor, digite uma quantidade positiva: '))

    if comida == 100: # a quantidade será somada a quantidade correspondente do código de comida selecionado
        quantidade100 += quantidade
    
    elif comida == 101:
        quantidade101 += quantidade

    elif comida == 102:
        quantidade102 += quantidade

    elif comida == 103:
        quantidade103 += quantidade

    elif comida == 104:
        quantidade104 += quantidade

    else:
        quantidade105 += quantidade

    continuar = input ('Caso queira encerrar o pedido, digite "E"; do contrário digite qualquer outra letra para continuar comprando: ').upper()
    print ('')
    if continuar == 'E':
        soma0 = quantidade100 * 1.2 # denominando o preço de cada item.
        soma1 = quantidade101 * 1.3
        soma2 = quantidade102 * 1.5
        soma3 = quantidade103 * 1.2
        soma4 = quantidade104 * 1.3
        soma5 = quantidade105 * 1
        somatória = soma0 + soma1 + soma2 + soma3 + soma4 + soma5
        print (f'Confirme o pedido:')
        print ('PRODUTO - PREÇO')
        print ('')
        if quantidade100 > 0: # o produto só será mostrado se for maior que zero.
            print (f'{quantidade100} Cachorro Quente(s) - R$ {soma0:.2f}')
            
        if quantidade101 > 0:
            print (f'{quantidade101} Bauru(s) Simples - R$ {soma1:.2f}')

        if quantidade102 > 0:
            print (f'{quantidade102} Bauru(s) com ovo - R$ {soma2:.2f}')

        if quantidade103 > 0:    
            print (f'{quantidade103} Hambúrguer(s) - R$ {soma3:.2f}')

        if quantidade104 > 0:
            print (f'{quantidade104} Cheeseburguer(s) - R$ {soma4:.2f}')

        if quantidade105 > 0:
            print (f'{quantidade105} Refrigerante(s) - R$ {soma5:.2f}')
        print ('')
        print (f'PREÇO TOTAL: R$ {somatória:.2f}') 
        print ('')
        
        encerrar = input ('Para confirmar, digite "C", do contrário digite qualquer letra para interromper o pedido: ').upper()

        if encerrar == 'C':
            print ('PEDIDO REALIZADO!') 
            print ('')
            repetir = input ('Caso queira fazer outro pedido, digite "R", do contrário digite qualquer outra letra para concluir o pedido: ').upper()

        else:
            repetir = input ('Caso deseje o alterar, digite "A"; do contrário digite qualquer outra letra para o cancelar: ').upper()
        if repetir != 'R' and repetir != 'A':
            print ('Tchau, tchau...')
            break
        else:
            print ('')
            print ('NOVO PEDIDO:')
        # caso repetir retorne True, o programa para.
        
    
