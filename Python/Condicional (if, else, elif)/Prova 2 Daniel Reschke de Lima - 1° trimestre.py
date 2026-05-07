# Feito por Daniel Reschke de Lima.
#O Supermercado Selbach está com uma promoção de grãos que é imperdível. Confira:
# *Tabela
#Cada cliente poderá levar apenas um dos tipos de grão da promoção, porém não há limite para a quantidade de grãos por cliente.
#Se a compra for feita no cartão Selbach o cliente receberá ainda um desconto de 5% sobre o total a compra. Escreva um programa que peça o tipo e a quantidade
# de grãos comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de grãos, preço total, tipo de pagamento,
# valor do desconto e valor a pagar.
#Obs.: Informe uma mensagem de erro caso seja escolhido algum outro produto fora da promoção.
#Obs. 2: Inclua seu nome no nome do arquivo e nos comentários do cabeçalho do código.
print ('O Supermercado Selbach está com uma promoção de grãos que é imperdível. Confira:')
print ('Feiijão preto (apartir de 5kg) - R$ 4,90.')
print ('Ervilha (apartir de 5kg) - R$ 5,90.')
print ('Grão-de-Bico (apartir de 5kg) - R$ 13,90.')
grao = int (input ('Digite 1 para feijão, 2 para ervilha e 3 para grão-de-bico: '))
if grao == 1 or grao == 2 or grao == 3:
    pesograo = float (input ('Digite a pesagem do produto selecionado: '))
    if pesograo <= 0:
        print ('O produto deve ter a pesagem positiva, não há como algo pesar menos que 0.')
    else:        
        if grao == 1:
            preçoKg1 = 5.8
            graonome = 'Feijão'
        elif grao == 2:
            preçoKg1 = 6.8
            graonome = 'Ervilha'
        elif grao == 3:
            preçoKg1 = 14.8
            graonome = 'Grão-de-bico'
else:
    print ('Por favor, selecione um produto válido.')
    preçoKg1 = 0
if preçoKg1 > 0 and pesograo > 0:
    if pesograo  >= 5:
        preçoKg2 = preçoKg1 - 0.9
    else:
        preçoKg2 = preçoKg1
    valor = preçoKg2 * pesograo
    pagamento = int (input ('Se a forma de pagamento for o cartão Selbach, digite 1. Caso seja qualquer outra, digite qualquer coisa sem ser o 1: '))
    if pagamento == 1:
        desconto = 5
        pagnome = 'Cartão Selbach'
    else:
        desconto = 0
        pagnome = 'Diversos'
    descontoR = valor * desconto/100
    valorfinal = valor - descontoR
    print (f'O grão selecionado foi: {graonome}')
    print (f'A pesagem informada dele foi de: {pesograo:.2f}kg')
    print (f'A forma de pagamento foi: {pagnome}')
    print (f'O valor total sem o desconto foi de: R$ {valor:.2f}')
    print (f'O desconto recebido pela forma de pagamento foi de: {desconto}%')
    print (f'Gerando um desconto de: {descontoR:.2f}')
    print (f'O valor total a pagar, com o desconto, foi de: R$ {valorfinal:.2f}')
        
