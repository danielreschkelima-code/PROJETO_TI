# Sistema de votos
print('CONTABILIZAÇÃO DE VOTOS\n')
listadecandidatos = []
qcandidatos = int(input('Digite a quantidade de candidatos: '))
candidatof = []
print ('\nNOMES DOS CANDIDATOS')

for i in range(qcandidatos+1):
    candidatof.append(0)

for i in range(qcandidatos):
    candidato = input(f'Digite o nome do candidato {i+1}: ')
    listadecandidatos.append(candidato)

qvotantes = int(input('\nDigite a quantidade de votantes: '))

print ('''\nLISTA DE CANDIDATOS:
''')
for i in range(len(listadecandidatos)):
    print('CANDIDATO', i+1, ':', listadecandidatos[i])
print('')

for i in range(qvotantes):
    try:
        voto = int(input(f'Votante número {i+1}, digite o número do seu candidato: '))
        candidatof[voto-1] += 1
    except:
        print("Digite um candidato válido!")

for i in range(qcandidatos):
    if len(candidatof)-1 > i: 
        if candidatof[i] > candidatof[i+1]:
            del candidatof[i+1]
            candidatovencedor = listadecandidatos[i] 
            qvotos = candidatof[i]
        elif candidatof[i] < candidatof[i+1]:
            del candidatof[i]
            candidatovencedor = listadecandidatos[i+1]
            qvotos = candidatof[i+1]
        else:
            print (f'\nEmpate entre os candidatos {i} e {i+1}')
    else:
        break
    
print (f'\nCom base na maioria dos votos, o candidato vencedor é o(a) {candidatovencedor}, com {qvotos} voto(s)')
