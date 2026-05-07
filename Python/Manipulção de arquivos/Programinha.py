#Crie um programa que cadastra os dados de clientes (nome, cpf, telefone, e-mail e endereço) em um arquivo. O usuário deve poder 
#cadastrar clientes. O programa deve ser capaz de:
#Buscar clientes pelo cpf
#Alterar dados de um cliente
#Apagar um cliente
#Mostrar todos os clientes na tela
import json
import os

print("\n---------------------------CLIENTEZINHOS---------------------------")

def limpar_tela():
    if os.name == 'nt': #windows
        os.system('cls')
    else:
        os.system('clear')
    print("---------------------------CLIENTEZINHOS---------------------------")

def validarcpf(cpf):
    return len(cpf) == 11 and cpf.isdigit()
    
def salvardados(conteudo):
    try:
        with open ("Banquinho.json", "w", encoding="utf-8") as  arq:
            json.dump(conteudo, arq, indent=4, ensure_ascii=False)
    except Exception as e:
            print(f"Erro ao salvar dados: {e}")

def baixardados():
    if not os.path.exists("Banquinho.json"):
            return {}
    
    try:
        with open ("Banquinho.json", "r", encoding="utf-8") as arq:
            clientes = json.load(arq)
            return(clientes)
    except json.JSONDecodeError:
        print(f"Aviso: O arquivo  de salvamento está corrompido ou vazio.")
        return {}
    except Exception as e:
            print(f"Erro ao carregar dados: {e}")
            return {}

def buscar(cpf):
    if not validarcpf(cpf):
        impressao = "CPF inválido. Deve conter 11 dígitos numéricos."
        return(impressao)
    clientes = baixardados()
    try:
        cliente = clientes[cpf]
        impressao = f"""
Cliente de cpf {clientes[cpf][nome]} encontrado! Seus dados são:
Nome: {clientes[cpf][nome]}
Cpf: {cpf}
Telefone: {clientes[cpf][telefone]}
E-mail: {clientes[cpf][email]}
Endereço: {clientes[cpf][endereco]}"""
        return(impressao)
    except KeyError:                
        impressao = "Cliente não encontrado."
        return(impressao)
        
def adicionar(nome, cpf, telefone, email, endereco):
    clientes = baixardados()
    if not validarcpf(cpf):
        impressao  = "CPF inválido. Deve conter 11 dígitos numéricos."
        return(impressao)
    if cpf in clientes:
        impressao = f"Erro: Cliente com CPF {cpf} já cadastrado."
        return(impressao)
    novo_cliente = {
        "nome": nome,
        "telefone": telefone,
        "email": email,
        "endereco": endereco
    }
    clientes[cpf] = novo_cliente
    salvardados(clientes)
    impressao = f"Cliente '{nome}' cadastrado com sucesso."
    return(impressao)

def alterar(cpf, nome=None, telefone=None, email=None, endereco=None):
    clientes = baixardados()
    if not validarcpf(cpf):
        impressao = "CPF inválido."
        return(impressao)
    if cpf not in clientes:
        impressao = f"Cliente com CPF {cpf} não encontrado. Não foi possível alterar."
        return(impressao)
    cliente = clientes[cpf]
    if nome:
        cliente['nome'] = nome
    if telefone:
        cliente['telefone'] = telefone
    if email:
        cliente['email'] = email
    if endereco:
        cliente['endereco'] = endereco
    salvardados(clientes)
    impressao =f"Dados do cliente com CPF {cpf} atualizados com sucesso."
    return(impressao)

def apagar(cpf):
    clientes = baixardados()
    if not validarcpf(cpf):
        impressao = "CPF inválido. Deve conter 11 dígitos numéricos."
        return(impressao)
    if cpf in clientes:
            nome_removido = clientes[cpf]['nome']
            del clientes[cpf]
            salvardados(clientes)
            print(f"Cliente '{nome_removido}' (CPF: {cpf}) removido com sucesso.")
    
def mostrar():
    print("\nIMPRIMINDO CLIENTES SALVOS...")
    clientes = baixardados()
    for cpf, cliente in clientes.items():
        print(f"""
Cliente de cpf {cpf}:
Nome: {cliente["nome"]}
Telefone: {cliente["telefone"]}
E-mail: {cliente["email"]}
Enereço: {cliente["endereco"]}
""")

print("Esse programa cadastra muitos clientes.")
while True:
    escolha = input("""
Escolha a operação a ser realizada:
(1) Buscar cliente pelo cpf
(2) Adicionar um cliente
(3) Alterar dados de um cliente
(4) Apagar um cliente
(5) Mostrar todos os clientes
(6) Encerrar o programa
>>> """) 
    
    if escolha == "1":
        limpar_tela()
        cpf = input("\nPor favor, digite o CPF do cliente a ser buscado: ")
        print(buscar(cpf))

    elif escolha == "2":
        limpar_tela()
        print("\nInsira os dados do novo cliente: ")
        nome = input("Nome: ")
        cpf = input("CPF: ")
        telefone = input("Telefone: ")
        email = input("E-mail: ")
        endereco = input("Endereço: ")
        print(adicionar(nome,cpf,telefone,email,endereco))
    
    elif escolha == "3":
        limpar_tela()
        cpf = input("\nInforme o cpf do cliente cujos dados serem alterados: ")
        print("Altere os dados necessário e deixe em branco aqueles que não precisam de alteração (cpf é imutável): ")
        nome = input("Nome: ")
        telefone = input("Telefone: ")
        email = input("E-mail: ")
        endereco = input("Endereço: ")
        print(alterar(cpf, nome, telefone, email, endereco))
    
    elif escolha == "4":
        limpar_tela()
        cpf = input("\nPor favor, digite o CPF do cliente a ser apagado: ")
        print(apagar(cpf))
    
    elif escolha == "5":
        limpar_tela()
        mostrar()
    
    elif escolha == "6":
        break
    
    else:
        print("\nOperação inválida! Por favor, escolha uma opção existente.")