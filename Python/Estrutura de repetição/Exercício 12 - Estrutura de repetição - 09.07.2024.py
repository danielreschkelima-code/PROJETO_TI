# Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada.

n = int (input ('Digite o número da tabuada desejada: '))
tabuada = 1
print (f'Tabuada do {n}:')
while tabuada <= 10:
    resultado = n * tabuada
    print (f'{n} X {tabuada:2} = {resultado}')
    tabuada += 1
