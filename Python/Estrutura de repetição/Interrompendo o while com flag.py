# Interrompendo repetições (com Flag) - 08/08/2024
import random
continuar = True  # a flag (bandeira) está levantada
# segredo = 999
while continuar:  # várias partidas
    segredo = random.randint(1,1000)  # gera nº aleatório entre 1 e 1000 (incluindo)
    tentativas = 0
    while continuar:  # uma partida
        adivinhe = int(input('\nDigite um número p/ tentar adivinhar o segredo: '))
        tentativas += 1  # conta quantas tentativas foram usadas
        if adivinhe == segredo:
            print(f'Parabéns! Você acertou em {tentativas} tentativas!')
            continuar = False
        else:
            print('Você errou... tente novamente!')
            if adivinhe < segredo:
                print('Dica: tente um número maior!')
            else:
                print('Dica: tente um número menor!')
            
            diferença = abs(adivinhe - segredo)  # valor absoluto (sempre positivo)
            if diferença >= 100:  # mais de 100
                print('Seu palpite está frio...')
            elif diferença >= 50:  # 99 - 50
                print('Seu palpite está morno...')
            elif diferença >= 10:  # 49 - 10
                print('Seu palpite está quente!')
            else:  # menos de 10
                print('Seu palpite está muito quente!')

    repetir = int(input('Digite 1 para uma nova partida ou outro para parar: '))
    if repetir == 1:
        continuar = True
