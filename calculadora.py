import tkinter as tk

# Função para calcular o resultado
def calcular(operacao):
    try:
        resultado = str(eval(operacao))  # Calcula a expressão
        entrada.set(resultado)
    except:
        entrada.set("Erro")  # Exibe "Erro" caso a operação seja inválida

# Função para atualizar a entrada da calculadora
def clicar(botao):
    atual = entrada.get()
    entrada.set(atual + botao)

# Função para limpar a entrada
def limpar():
    entrada.set("")

# Configuração da interface gráfica
janela = tk.Tk()
janela.title("Calculadora")

# Variável para armazenar o que foi digitado
entrada = tk.StringVar()

# Campo de entrada
campo_entrada = tk.Entry(janela, textvariable=entrada, font=("Arial", 20), bd=10, insertwidth=2, width=14, borderwidth=4)
campo_entrada.grid(row=0, column=0, columnspan=4)

# Botões da calculadora
botoes = [
    '7', '8', '9', '/', 
    '4', '5', '6', '*',
    '1', '2', '3', '-', 
    '0', '.', '=', '+'
]

# Posicionamento dos botões
linha = 1
coluna = 0

for botao in botoes:
    if botao == '=':
        tk.Button(janela, text=botao, padx=20, pady=20, font=("Arial", 20), command=lambda: calcular(entrada.get())).grid(row=linha, column=coluna)
    else:
        tk.Button(janela, text=botao, padx=20, pady=20, font=("Arial", 20), command=lambda botao=botao: clicar(botao)).grid(row=linha, column=coluna)
    
    coluna += 1
    if coluna > 3:
        coluna = 0
        linha += 1

# Botão para limpar
tk.Button(janela, text='C', padx=20, pady=20, font=("Arial", 20), command=limpar).grid(row=linha, column=coluna)

# Iniciar a interface
janela.mainloop()
