# STRING
print ('MANUAL STRING\n')

# lower
print ('\n', '----------------LOWER-------------')

a = 'OI'
a1 = a.lower()
print (a,'\n',a1)

# upper
print ('\n', '---------------UPPER--------------')

a = 'oi'
a1 = a.upper()
print (a,'\n',a1)

# capitalize
print ('\n', '----------------CAPITALIZE--------------')

a = 'oi oi'
a1 = a.capitalize()
print (a,'\n',a1)

# title
print ('\n', '----------------TITLE--------------')

a = 'oi oi'
a1 = a.title()
print (a,'\n',a1)

# join
print ('\n', '----------------JOIN--------------')

a = 'oi oi'
a1 = list(a)
print ('Em lista: ', a1)
print ('Retomando em string com join: ', ''.join(a1))
print ('Retomando em string com "-" entre os carcateres: ','-'.join(a1),'\n')

# sartswith
print ('\n', '----------------STARTSWITH--------------')

a = 'oi oi'
print ('''a = "oi oi"
a começa com "oi"?''')
if a.startswith('oi'):
    print ('True\n')
else:
    print ('False\n')

# endswith
print ('\n', '----------------ENDSWITH--------------')

a = 'oi oi'
print ('''a = "oi oi"
a termina com "oi"?''')
if a.endswith('oi'):
    print('True\n')
else:
    print('False\n')

# count (conta)
print ('\n', '----------------COUNT--------------')

a = 'oi oi'
print (f'''a = "oi oi"
Há {a.count('i')} i na frase de a.''')

# find (procura)
print ('\n', '----------------FIND--------------')

a = 'oi oi'
print (f'''a = "oi oi"
O termo oi aparece na posição {a.find('oi')} e na posição {a.find('oi', 2)} (as posições começam em 0)''')

# center
print ('\n', '----------------CENTER--------------')
a = 'oi'
print (f'Centralizando:\nCom espaço: {a.center(10)}\nCom hífen: {a.center(10,"-")}')

#ljust
print ('\n', '----------------LJUST--------------')
a = 'oi'
print (f'Alinhando à esquerda:\nCom espaço: {a:>20}\nCom ponto: {a:.>20}')

#rjust
print ('\n', '----------------RJUST--------------')

a = 'oi'
print (f'Alinhando à direita:\nCom espaço: {a:<20}\nCom ponto: {a:.<20}')
