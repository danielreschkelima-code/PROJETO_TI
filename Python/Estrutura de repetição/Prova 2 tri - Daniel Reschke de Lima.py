# Daniel Reschke de Lima 
# 1) Crie um programa que leia as notas de uma avaliação para cada um dos alunos de uma turma.
# A informação sobre a quantidade de alunos na turma deve ser fornecida pelo usuário no momento da execução (validar: nota deve ser valor entre zero e dez).
#    a) Imprima a média das notas da turma.
#    b) Imprima a quantidade de alunos com nota dentro da média mínima para aprovação (7,0) e a quantidade de alunos abaixo da média mínima para aprovação.
#    c) Imprima a nota mais alta da turma e a nota mais baixa da turma.
#    d) DESAFIO OPCIONAL: depois de concluir todos os outros requisitos do enunciado, modifique o programa para perguntar o nome de cada aluno antes de perguntar pela nota dele.
# Ao fim do programa imprima o nome do aluno com nota mais alta.

alunos = int (input ('Digite a quantidade de alunos na turma: '))
contador = 1
soma = 0
maior = 0    
menor = 10
contadormediapositiva = 0
contadormedianegativa = 0
while contador <= alunos:
    nota = float (input (f'Digite a nota do aluno {contador} (lembrando que a média é 7): '))
    while nota < 0 or nota > 10:
        print ('As notas só são válidas entre 0 e 10. Por favor, digite uma nota válida.')
        nota = float (input (f'Digite a nota do aluno {contador}: '))
    if nota > maior:
        maior = nota
    if nota < menor:
        menor = nota
    if nota >= 7:
        contadormediapositiva += 1
    else:
        contadormedianegativa += 1
    soma += nota
    contador += 1
mediaturma = soma/alunos

print (f'Com a quantidade {alunos} de alunos, a média geral da turma é de: {mediaturma:.2f}')
print (f'A quantidade de alunos acima da média é de: {contadormediapositiva}')
print (f'A quantidade de alunos abaixo da média é de: {contadormedianegativa}')
print (f'A nota mais alta da turma foi de: {maior:.2f}')
print (f'A menor nota da turma foi de: {menor:.2f}')

