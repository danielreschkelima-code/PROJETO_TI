def calcularMedia(notas: float) -> float :
    return (notas)/3

alunosTurma = int(input("\nDigite quantos alunos sua turma tem: "))
print()

somaTurma = 0
mediaAlunos = []
for i in range(1, alunosTurma + 1):
    totalNotaAluno = 0
    for j in range(1, 4):
        totalNotaAluno += float(input(f"Digite a nota {j} do aluno {i}: "))
    print()
    media = calcularMedia(totalNotaAluno)
    mediaAlunos.append(media)
    somaTurma += media
    
for i in range(1, 1 + len(mediaAlunos)): 
    print(f"Média do Aluno {i}: {mediaAlunos[i-1]:.2f}")

print(f"\nMédia da turma: {somaTurma/alunosTurma:.2f}\n")