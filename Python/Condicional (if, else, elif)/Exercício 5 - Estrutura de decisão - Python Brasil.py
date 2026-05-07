# Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor do que sete;
# A mensagem "Aprovado com Distinção", se a média for igual a dez.

print ('Cálculo de média para duas notas parciais')
n = float (input ('Digite a primeira nota: '))
n1 = float (input ('Digite a segunda nota: '))
m = (n + n1)/2
print (f'Essa é sua média: {m:.2f}')
if m >= 7 and m < 10:
    print ('Você foi aprovado!!')
else:
    if m < 7 and m > 0:
        print ('Sinto muito, mas você foi reprovado.')
    else:
        print ('Parabéns, você foi aprovado com distinção!')

    
