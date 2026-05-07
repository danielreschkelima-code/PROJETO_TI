# Faça um programa que gera uma lista dos números primos existentes entre 1 e um número inteiro informado pelo usuário.
numlimite = int (input ('Digite até onde você deseja saber os números primos: '))
a = 2 # Define o primeiro número primo, inibindo a utilização de uma verificação (if) para números abaixo de 2 na função primo. 
def primo(a): # Define o que é a função primo.
    for i in range(2, int(a ** 0.5) + 1): # O for faz um loop do 2 até o número limite, no qual o número é testado para ver se ele é primo ou não. 
        if a % i == 0: # Caso o resto de um do número seja zero, ele é considerado um não primo.
            return False
    return True
while a <= numlimite: 
    if primo(a): # Invoca a função preestabelecida e, se ela retornar como True, imprimirá o número primo.
        numprimo = a
        print (numprimo)
    a += 1
        

                
