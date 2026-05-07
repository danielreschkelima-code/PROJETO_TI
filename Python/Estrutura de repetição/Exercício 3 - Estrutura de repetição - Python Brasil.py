##Faça um programa que leia e valide as seguintes informações:
##Nome: maior que 3 caracteres;
##Idade: entre 0 e 150;
##Salário: maior que zero;
##Sexo: 'f' ou 'm';
##Estado Civil: 's', 'c', 'v', 'd'.

nome = input ('Digite o seu nome completo: ')
while len(nome) < 3:
    print ('O seu nome deve ser maior que 3 letras.')
    nome = input ('Digite o seu nome completo (que deve ser maior que 3 letras: ')

idade = int (input ('Digite a sua idade: '))
while idade < 0 or idade > 150:
    print ('Somente idades entre 0 e 150 são aceitas, digite uma válida.')
    idade = int (input ('Digite a sua idade: '))

salário = int (input ('Digite sua renda: '))
while salário <= 0:
    print ('O seu salário não pode ser nulo ou menor que zero.')
    salário = int (input ('Digite sua renda (maior que 0): '))

sexo = input ('Digite o seu sexo (M, F ou O): ').upper()
while sexo not in ' MFO':
    print ('Por favor, digite um sexo válido. M - masculino, F - Feminino, O - outros ou sem nada para omitir.')
    sexo = input ('Digite o seu sexo (M, F ou O): ').upper()

estado = input ('Digite seu estado civil (S, C, V OU D): ').upper()
while estado not in 'SCVD':
    print ('Por favor, digite um estado válido. S - solteiro, C - casado, V - viúvo e D - divorciado.')
    estado = input ('Digite seu estado civil (S, C, V OU D): ').upper()

print (f'''Informações validadas. Sendo elas:
Nome: {nome}
Idade: {idade}
Renda mensal: R${salário:.2f}
Sexo (em branco é não informado): {sexo}
Estado civil: {estado}''')


