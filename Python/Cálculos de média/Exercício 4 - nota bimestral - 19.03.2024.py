#Exercício 4 - Sequencial - Phyton Brasil - 19/03/2024
# Programa que peça as 4 notas bimestrais e mostre a média.

nota1= float (input ('Digite a nota do 1° bimestre: '))#float atribui o valor de entrada do input em números inteiros ou quebrados, mas gasta mais poder de processamento do computador comparado com o int. Esse só trabalha com inteiros.
nota2= float (input ('Digite a nota do 2° bimestre: '))
nota3= float (input ('Digite a nota do 3° bimestre: '))
nota4= float (input ('Digite a nota do 4° bimestre: '))
média= (nota1+nota2+nota3+nota4)/4
print ('Essa é sua média:')
print (média)
