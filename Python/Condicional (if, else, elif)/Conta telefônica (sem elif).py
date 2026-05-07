# Calcular a conta de telefone celular da empresa "Telefonet: Celular bom é em
# atacado."
# Abaixo de 200 min : R$ 0,20
# Entre 200 a 400 min: R$ 0,18
# Acima de 400: R$ 0, 15
# Os valores são para cada minuto
minu = int (input('Informe a quantidade de minutos da rede utilizados: '))
if minu < 200:
    preçominuto = 0.20
else:
    if minu > 400:
        preçominuto = 0.18
    else:
        preçominuto = 0.15    
preçototal = minu * preçominuto
print (f'O tempo total utilizado da rede foi de {minu} min, e será cobrado R$ {preçominuto:.2f} por minuto.')
print (f'Com isso, o valor inteiro da conta é de R$ {preçototal:.2f}')
print ('Por conta do varejo e atacado, quanto maior a quantidade de minutos, menos se pagará pelo preço por minuto.')
a =int (input ('Saiba mais sobre os preços digitando 1: '))
if a == 1:
    print ('Os valores por minuto, baseado no tempo total é:')
    print ('Abaixo de 200 min: R$ 0,20;')
    print ('Entre 200 a 400 min: R$ 0,18;')
    print ('Acima de 400 min: R$ 0,15.')

