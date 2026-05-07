# Imprima de 1 até número selecionando
n = int (input ('Selecione um número teto: '))
if n >= 1:
    x = 1
    while x <= n:
        print (x)
        x += 1
    
else:
    print ('Só são válidos números positivos...')
