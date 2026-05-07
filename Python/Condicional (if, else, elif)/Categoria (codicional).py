# Porgrama 4.6 do livro azul - Categoria X Preço

categoria = int (input ('Digite a categoria do produto: '))
if categoria == 1:
    preço == 10.00
elif categoria == 2:
    preço = 18.00
elif categoria == 3:
    preço = 23.00
elif categoria ==4:
    preço = 26.00
elif categoria == 5:
    preço = 31.00
else:
    print ('Categoria inválida! Obviamente, não há preço. Consulte novamente as categorias.')
if categoria >= 1 and categoria <= 5: # uma redundância necessária, já foi testado o valor das categorias.
    print (f'O preço dos produtos da categoria {categoria} é : R$ {preço:.2f}.')
    
    
