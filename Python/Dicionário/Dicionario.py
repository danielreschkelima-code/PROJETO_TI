print("\nDICIONÁRIOS")

produtos = []

for i in range(5):
    produto = {}
    print(f"\nINFORME OS DADOS DO PRODUTO {i}")
    produto["id"] = i
    produto["nome"] = input("Digite o nome do produto: ")
    produto["preco"] = float(input("E informe o seu preço: "))
    produtos.append(produto)

print("\nIMPRESSÃO DE DADOS\n")
for produto in produtos:
    print(f"PRODUTO {produto["id"]}")
    print(f"Nome: {produto["nome"]}")
    print(f"Preço: R$ {produto["preco"]:.2f}\n")