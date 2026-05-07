##Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes
##com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a
##população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.
A = int (input ('Digite o número de habitantes do país A: '))
B = int (input ('Digite o número de habitantes do país B: '))
while A < 0 or B < 0:
    print ('O país necessita ter uma contagem positiva de habitantes')
    A = int (input ('Digite o número de habitantes do país A: '))
    B = int (input ('Digite o número de habitantes do país B: '))

pA = float (input ('Digite a taxa de crescimento em porcentagem do país A: '))
pB = float (input ('Digite a taxa de crescimento em porcentagem do país B: '))
while pA <= pB:
    print ('O país A precisa ter uma taxa de crescimento maior que o do país B.')
    pA = float (input ('Digite a taxa de crescimento em porcentagem do país A: '))
    pB = float (input ('Digite a taxa de crescimento em porcentagem do país B: '))

pb = pB/100
pa = pA/100

anos = 0

while A < B:
    A += A * pa
    B += B * pb
    anos += 1

print (f'''Demorou {anos} anos para o número de habitantes do país A superar o número de habitantes de B.
O país A ficou com {A:.0f} habitantes.
O país B ficou com {B:.0f} habitantes.''')

     
 
