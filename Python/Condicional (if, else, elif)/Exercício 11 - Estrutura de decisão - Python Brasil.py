# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5%
# Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.

salario = int (input ('Forneça o salário do colabolador: '))
if salario <= 280:
    aumento = 20/100
elif salario <= 700:
    aumento = 15/100
elif salario <= 1500:
    aumento = 10/100
else:
    aumento = 5/100
aumentodesalario = salario*aumento 
salarionovo = salario + aumentodesalario
if salario > 0:
    print (f'Este é o salário informado antes do reajuste: R$ {salario:.2f};')
    print (f'Este é o salário com o reajuste: R$ {salarionovo:.2f};')
    print (f'O percentual de aumento aplicado (em decimal de porcentagem) foi de: {aumento};')
    print (f'O qual gerou uma diferença entre o salário velho e o novo de: R$ {aumentodesalario:.2f}.')
a = int (input ('Digite um 1 caso queira saber mais sobre o reajuste de salário: '))
if a == 1:
    print ('Os reajustes de salário variam conforme a renda antiga, seguindo os seguintes percentuais de acordo:')
    print ('Salários até R$ 280,00 (incluindo) - aumento de 20%')
    print ('Salários entre R$ 280,00 e R$ 700,00 (incluindo) - aumento de 15%')             
    print ('Salários entre R$ 700,00 e R$ 1500,00 - aumento de 10%')
else:
    print ('Opção indisponível, sinto muito; você escolheu algo além de 1?')
        
