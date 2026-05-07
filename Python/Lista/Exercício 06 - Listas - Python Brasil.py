# Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com
# média maior ou igual a 7.0.

alunos = ['aluno1','aluno2','aluno3','aluno4','aluno5','aluno6','aluno7','aluno8','aluno9','aluno10']
mediatodos = []
contadoraluno = 0
alunosaprovados = 0

while contadoraluno < len(alunos):
    notainicio = 0

    for i in range (1,5):
        notas = float (input (f'Digite a {i}º nota do {alunos[contadoraluno]}: '))
        notainicio += notas
    media = notainicio/4
    mediatodos.append(media)

    if media >= 7:
        alunosaprovados += 1
    contadoraluno += 1 
alunosreprovados = 10 - alunosaprovados
                      
print (f'''
A quantidade de alunos aprovados (com nota maior ou igual a 7) foi de: {alunosaprovados}
A quantidade de alunos reprovados foi de: {alunosreprovados}

A média de cada aluno é:''')

i = 0
while i < len(mediatodos):
    print (f'{alunos[i]}: {mediatodos[i]}')
    i += 1
                
