import tkinter as tk
from tkinter import ttk
import Calculos

# Cria a janela principal
janela = tk.Tk()
janela.title("Calculadora do Teodolito")

print ("\nCALCULADORA DO TEODOLITO\nSe algum cáculo for realmente feito, seus resultados também serão impressos no terminal.")

# Frame para organizar os inputs
frame_entradas = ttk.Frame(janela, padding="10")
frame_entradas.pack()

# Escolha do tipo de distância
tipo_distancia = tk.StringVar(value="1") # Variável para guardar a escolha (1 ou 2)
ttk.Label(frame_entradas, text="Tipo de distância informada:").grid(row=0, column=0, columnspan=2, sticky="W")
ttk.Radiobutton(frame_entradas, text="Distância Transversal (hipotenusa)", variable=tipo_distancia, value="1").grid(row=1, column=0, sticky="W")
ttk.Radiobutton(frame_entradas, text="Distância Horizontal", variable=tipo_distancia, value="2").grid(row=1, column=1, sticky="W")

# Entrada da distância
ttk.Label(frame_entradas, text="Distância (metros):").grid(row=2, column=0, sticky="W", pady=5)
entry_distancia = ttk.Entry(frame_entradas, width=15)
entry_distancia.grid(row=2, column=1, sticky="E")

# Entrada do ângulo
ttk.Label(frame_entradas, text="Ângulo (graus):").grid(row=3, column=0, sticky="W", pady=5)
entry_angulo = ttk.Entry(frame_entradas, width=15)
entry_angulo.grid(row=3, column=1, sticky="E")

# --- Widget para o resultado ---
label_resultado = ttk.Label(janela, text="Resultado aparecerá aqui", font=("Helvetica", 12))
label_resultado.pack(pady=20)

contagem = 0
def executar_calculo():
    
    try:
        # Pega os valores dos campos de entrada
        distancia = float(entry_distancia.get())
        angulo = float(entry_angulo.get())
        distancia_obtida = tipo_distancia.get()
        
        
        # Converte o ângulo
        rad = Calculos.Converter(angulo)

        # Lógica de cálculo baseada na escolha do usuário
        if distancia_obtida == "1":
            h = Calculos.Calcularh1(rad, distancia)
            distancia_horizontal = Calculos.Calculardh(rad, distancia)
            resultado = f"Altura (h): {h:.2f} m\nDistância Horizontal: {distancia_horizontal:.2f} m"
            
            print(f"""
RESULTADOS:
Altura (h): {h:.2f} m
Distância Horizontal: {distancia_horizontal:.2f} m
Distância Transversal: {distancia:.2f} m
Ângulo: {angulo:.2f}°

---------------------------------------------------""")
           

        else:
            h = Calculos.Calcularh2(rad, distancia)
            distancia_transversal = Calculos.Calculardt(rad, distancia) # Nota: Há um erro no seu código original aqui, deveria ser tan ou outra relação. Assumindo que o cálculo esteja correto para o exemplo.
            resultado = f"Altura (h): {h:.2f} m\nDistância Transversal: {distancia_transversal:.2f} m"
            
            print(f"""
RESULTADOS:
Altura (h): {h:.2f} m
Distância Horizontal: {distancia:.2f} m
Distância Transversal: {distancia_transversal:.2f} m
Ângulo: {angulo:.2f}°

---------------------------------------------------""")

        # Atualiza o label de resultado
        label_resultado.config(text=resultado)

    except ValueError:
        label_resultado.config(text="Erro: Por favor, insira valores numéricos válidos.")

# Botão para calcular
botao_calcular = ttk.Button(janela, text="Calcular", command=executar_calculo)
botao_calcular.pack(pady=10)

# Inicia o loop da interface gráfica
janela.mainloop()