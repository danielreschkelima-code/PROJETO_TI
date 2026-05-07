print("ORGANIZADOR DE LISTA EM ORDEM CRESCENTE\n")

lista = [535,144,545,4,213,3342,556,5,4,3,2,1,0]

for elem in range(len(lista)-1):
        if lista[elem] <= lista[elem+1]:
            continue
        else:
            lista[elem], lista[elem+1] = lista[elem+1], lista[elem]
            for posiçãoatual in range (elem,0,-1):
                if lista[posiçãoatual] < lista[posiçãoatual-1]:
                    lista[posiçãoatual], lista[posiçãoatual-1] = lista[posiçãoatual-1], lista[posiçãoatual]
                    print(lista)
                    print(f"Houve troca de {lista[posiçãoatual]} com {lista[posiçãoatual-1]}")
                else:
                    break
print(lista)