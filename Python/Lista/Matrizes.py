# Crie um programa que peça para o usuário preencher o conteúdo de uma matriz de dimensões 3x4. Αρόs
# inseridos os dados, realize uma busca na matriz e informe quais são os valores das linhas e colunas (posição) 
# do maior e do menor elemento de toda a matriz.

print("\nMATRIZES")
print("Preencha-a!\n")

#CRIAÇÃO DA MATRIZ
matriz = [[],[],[]]
for linhas in range(len(matriz)):
    for colunas in range(4):
        conteudo = int(input(f"Digite o número inteiro a ser posto na linha {linhas} e coluna {colunas}: "))
        matriz[linhas].append(conteudo)

#IMPRESSÃO
print("\nIMPRESSÃO DA MATRIZ")
for linhas in range(len(matriz)):
    print(f"[{matriz[linhas]}]")

#BUSCA DO MAIOR E MENOR ELEMENTO
print("\nPROCESSAMENTO")

ordem = []
for linhas in range(len(matriz)):
    for colunas in range(len(matriz[linhas])):
        atual = [[matriz[linhas][colunas]],[linhas, colunas]]
        ordem.append(atual)

for elem in range(len(ordem)-1):
        if ordem[elem][0] <= ordem[elem + 1][0]:
            continue
        else:
            ordem[elem], ordem[elem+1] = ordem[elem+1], ordem[elem]
            for troca in range(ordem.index(ordem[elem]), 0, -1):
                if ordem[troca][0] < ordem[troca-1][0]:
                        ordem[troca], ordem[troca-1] = ordem[troca-1], ordem[troca]
                        print(f"Troca {ordem[troca][0]} com {ordem[troca-1][0]}")  
                else:
                    break
#RESULTADOS
print("\nRESULTADOS")
print("A ordem crescente dos elementos é: ", end="")
for elem in range(len(ordem)):
    print(f"{ordem[elem][0]}", end=" ")

print(f"\nO menor elemento é {ordem[0][0]}, que está na posição {ordem[0][1]}.")
print(f"O maior elemento é {ordem[-1][0]}, que está na posição {ordem[-1][1]}.")