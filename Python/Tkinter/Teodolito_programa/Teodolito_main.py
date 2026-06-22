import Calculos

print("\n---------------CALCULADORA DO TEODOLITO---------------")
print("Com base em uma distância e o ângulo medido pelo teodolito, é possível achar as outras duas distâncias.")

distânciaobtida = input("\nInforme (1) se a distância já obtida for a transversal (hipotenusa) e 2 se ela for a horizontal (teodolito-h): \n(1)Distância Horizontal\n(2)Distância Vertical\n> ")
while distânciaobtida != "1" and distânciaobtida != "2":
    distânciaobtida = input("Por favor, digite apenas (1) para a distância transversal e (2) para a horizontal: ")

while True:
    try:
        distância = float (input("\nDigite em metros a distância obtida: "))
        break
    except ValueError():
        distância = float (input("Entrada inválida. Digite apenas o número de metros da distância obtida: ")) 

while True:
    try:
        ângulo = float (input("Digite o ângulo em graus obtido pelo teodolito: "))
        break
    except ValueError():
        ângulo = float (input("Entrada inválida. Digite apenas o número de graus do ângulo obtido pelo teodolito: ")) 

rad = Calculos.Converter(ângulo)

if distânciaobtida == "1":
    h = Calculos.Calcularh1(rad, distância)
    distânciahorizontal = Calculos.Calculardh(rad,distância)
    print(f"""
RESULTADOS:
Altura (h): {h:.2f} m
Distância Horizontal: {distânciahorizontal:.2f} m
Distância Transversal: {distância:.2f} m
Ângulo: {ângulo:.2f}°

---------------------------------------------------""")
    
else:
    h = Calculos.Calcularh2(rad, distância)
    distânciatransversal = Calculos.Calculardt(rad, distância)
    print(f"""
RESULTADOS:
Altura (h): {h:.2f} m
Distância Horizontal: {distância:.2f} m
Distância Transversal: {distânciatransversal:.2f} m
Ângulo: {ângulo:.2f}°

---------------------------------------------------""")