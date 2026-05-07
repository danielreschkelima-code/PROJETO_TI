#Exercício: Peça uma frase e imprima a segunda metade da frase.

frase = input ('Digite uma frase: ')
f = len (frase) // 2 # 2 / indicam que só apareceram números inteiros.
frase2 = frase[f:]
print (frase2)


