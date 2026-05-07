# Tabuada com função

def tabuada(multiplicador):
    tabulista = []
    for i in range(multiplicador,(multiplicador*10)+1,multiplicador):
        tabulista.append(i)
    return tabulista
print ('TABUADA COM DEF\n')
número = int(input('Digite um número para obter sua tabauda: '))
print (f'\nTABUADA DO {número}\n')
for i in range(len(tabuada(número))):
    print (f'{i+1} X {número} = {tabuada(número)[i]}')


        
        
