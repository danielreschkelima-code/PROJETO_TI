# Exercício Operações com string - 8 Python Brasil
# Faça um programa que pergunte quanto você ganha por hora, o número de horas trabalhadas por mês e calcule (mostrando) o total do seu salário no referido no mês.

print ('Calculo do total do seu salário por mês, ajuda na sua economia.')
salario_hora = float (input ('Digite o valor das suas difíceis horas trabalhadas: ')) 
hora_mes = float (input ('E, agora, digite quantas horas você trabalhou ou trabalhará por mês: '))
salario_total = salario_hora * hora_mes
print (f'Esse é o seu salário por mês: R${salario_total:.2f}')
if salario_total<0:
    print ('Isso é impossível, como ganhar menos do que o nada?')
