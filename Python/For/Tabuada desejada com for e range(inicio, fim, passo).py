# Tabuada desejada com for e range(inicio, fim, passo) - 10/10/2024
# validar tabuada (entre 1 e 10)

while True:
    tabuada = int(input('Digite a tabuada desejada: '))
    if tabuada in range(1,11):  # validação com range()
        break
    else:
        print('A tabuada escolhida deve estar entre 1 e 10!')

limite = tabuada * 11
# enumerate iniciando em 1:
intervalo = range(tabuada, limite, tabuada)
for multiplicador, produto in enumerate(intervalo, 1):
    print(f'{tabuada} x {multiplicador} = {produto}')
