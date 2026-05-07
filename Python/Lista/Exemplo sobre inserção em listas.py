# Exemplo sobre inserção em listas - 29/08/2024
import random
caracteres = []

i = 1
while i <= 10:
    c = input(f'Digite a {i}ª letra (de 10): ').lower()
    # c.isalpha() testa se c é uma letra do alfabeto
    if c.isalpha() and len(c) == 1:
        caracteres.append(c)  # insere o caractere digitado como um novo elemento
        i += 1
    else:
        print('Erro: Digite apenas letras individuais do alfabeto!')

# repetição para sortear caracteres
print('Gerando mais 10 caracteres aleatórios...')
limite = len(caracteres) + 10
while len(caracteres) < limite:  # repete até que a lista tenha 20 elementos
    # a tem posição 97 na tabela ascii e z tem posição 122
    c = chr(random.randint(97, 122))  # gera letra minúscula aleatória de a até z
    caracteres.append(c)  # insere na lista o caractere gerado

i = 0
while i < len(caracteres):
    print(caracteres[i], end=', ')  # imprime cada caractere, lado a lado
    i += 1




