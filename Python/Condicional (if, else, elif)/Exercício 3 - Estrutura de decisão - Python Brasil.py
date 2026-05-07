# Faça um Programa que verifique se uma letra digitada é "F" ou "M".
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

print ('Informe o seu gênero, e, se preferir, não informe.')
print ('M para masculino, F para feminino, O para outro e deixe em branco para não informar.')
genero = input ('Digite aqui: ')
if genero == 'M' or genero == 'm' or genero == 'Masculino' or genero == 'masculino':
    print ('Masculino')
else:
    if genero == 'F' or genero == 'f' or genero == 'Feminino' or genero == 'feminino':
        print ('Feminino')
    else:
        if genero == 'O' or genero == 'o':
            print('Outros')
        else:
            print ('Não informado.')
        
        
        

