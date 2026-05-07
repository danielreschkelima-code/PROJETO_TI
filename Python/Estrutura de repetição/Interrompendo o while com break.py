# Interrompendo repetições (com break) - 08/08/2024

# EXEMPLO DE VALIDAÇÃO DE DADOS (com while True e break)

while True:
    n = int(input('Digite um número entre 0 e 100: '))
    if n >= 0 and n <= 100:  # verificar se está correto
        break  # essa instrução interrompe o while imediatamente
        print('essa linha jamais será executada')
    # o print a seguir não é executado quando faz o break
    print('Erro: digite apenas valores entre 0 e 100!')

# essa linha fora do while é executada logo após o break
print('FIM')


# EXEMPLO DE SOMATÓRIO DE NÚMEROS
soma = 0
x = 0
while True:
    n = float(input('Digite um número p/ somar ou 0 para sair: '))
    if n == 0:
        break
    soma += n
    x += 1
print(f'Soma: {soma:.2f}')
print(f'Média: {soma/x:.2f}')       
