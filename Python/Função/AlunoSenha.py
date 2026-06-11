#FUNCOES QUE VALIDAM A ENTRADA
def validarTamanho(sen):
    if len(sen) < 8:
        return False
    else:
        return True 

def validarNumero(sen):
    numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for caracter in sen:
        if caracter in numeros:
            return True
    return False

def validarMaiuscula(sen):
    if sen != sen.lower():
        return True
    else:
        return False

def validarMinuscula(sen):
    if sen != sen.upper():
        return True
    else:
        return False

#LOOP
tentativas = 1
while tentativas < 6 and tentativas != -1:
    
    #ENTRADA
    senha = input("")
    falhas = f"Tentativa <{tentativas}>: "

    #SAIDA
    if not validarTamanho(senha):
        falhas += "falta pelo menos 8 carcteres; "  
    
    if not validarNumero(senha):
        falhas += "falta um número; "
    
    if not validarMaiuscula(senha):
        falhas += "falta uma letra maiúscula; "

    if not validarMinuscula(senha):
        falhas += "falta uma letra minúscula; "

    if falhas == f"Tentativa <{tentativas}>: ":
        print ("Senha alterada com sucesso!")
        tentativas = -1 
    
    else:
        falhas = falhas[0 : -2]
        print(falhas)
        tentativas += 1

if tentativas >= 6:
    print("Limite de tentativas atingido. Conta bloqueada.")