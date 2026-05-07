# A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.

limite = int (input ('Quantos números deseja gerar da sequência de Fibonacci: '))
anterior = 0
n = 1
atual = 1
fib = anterior + atual

while n <= limite:
    print ( anterior, end=',')
    anterior = atual
    atual = fib
    fib = anterior + atual
    n += 1


print ('Fibonacci até 500.')
anterior = 0
atual = 1
fib = anterior + atual
print (anterior, end=',')

while fib <= 500:
    anterior = atual
    atual = fib
    fib = anterior + atual
    print (anterior, end=',')
