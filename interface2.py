import tkinter as tk
from tkinter import ttk
import time

from automacao2 import executar2
from automacao import executar  # Certifique-se de que a função 'executar' está definida no arquivo 'automacao.py'

listaOCI = []

# Variáveis para personalizar o layout
fonte = ("Arial", 12)
cor_texto = "black"
espacamento = 10

# Criar janela principal
root = tk.Tk()
root.title("Exemplo de Abas")

# Criar o notebook para as abas
notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand=True)

def inserirOCI(entradas):
    valores = []
    for entry in entradas:
        valor = entry.get()
        print(valor)
        valores.append(valor)
    print("Valores digitados:")
    oci = {
        "dataOCI": valores[0],
        "codigoFornecedor": valores[1],
        "planoPagamento": valores[2],
        "planoFrete": valores[3],
        "tipoFrete": valores[4],
        "tipoCobranca": valores[5],
        "justificativa": valores[6],
        "codigoMaterial": valores[7],
        "quantidade": valores[8],
        "precoUnitario": valores[9],
        "almoxarifado": valores[10],
        "objetoCusto": valores[11]
    }
    listaOCI.append(oci)
    print(listaOCI)
    # Atualizar a exibição na aba 1
    texto_lista.configure(state='normal')
    texto_lista.delete('1.0', tk.END)
    texto_lista.insert(tk.END, ' '.join(str(oci)))
    texto_lista.configure(state='disabled')

# Função para criar campos de entrada com alinhamento vertical
def criar_campos_verticais(master, campos):
    entradas = []
    for i, (texto, valor) in enumerate(campos):
        tk.Label(master, text=texto, font=fonte, fg=cor_texto).grid(row=i, column=0, sticky='w', padx=(10, 5), pady=(10, 0))
        entry = tk.Entry(master, font=fonte)
        entry.insert(0, valor)  # Insere o valor padrão no campo de entrada
        entry.grid(row=i, column=1, sticky='ew', padx=(0, 10), pady=(10, 0))
        entradas.append(entry)
    return entradas

# Função para obter os dados digitados nos campos
def obter_dados(entradas):
    valores = []
    for entry in entradas:
        valor = entry.get()
        print(valor)
        valores.append(valor)
    print("Valores digitados:")
    for valor in valores:
        print(valores)

# Aba 1
aba1 = ttk.Frame(notebook)
notebook.add(aba1, text='LISTAR OCI')

campos_entrada_aba1 = [
    ("Data da Nota:", ""),
    ("Código do Funcionário:", ""),
    ("Código do Fornecedor:", ""),
    ("Plano de Pagamento:", ""),
    ("Pagamento de Frete:", ""),
    ("Tipo de Frete:", ""),
    ("Tipo de Cobrança:", ""),
    ("Justificativa:", ""),
    ("Código do Material:", ""),
    ("Quantidade:", ""),
    ("Preço:", ""),
    ("Almoxarifado: ", ""),
    ("Objeto de Custo: ", "")
]

def executarOCI():
    for oci in listaOCI:
        executar2(
            oci["dataOCI"],
            oci["codigoFornecedor"],
            oci["planoPagamento"],
            oci["planoFrete"],
            oci["tipoFrete"],
            oci["tipoCobranca"],
            oci["justificativa"],
            oci["codigoMaterial"],
            oci["quantidade"],
            oci["precoUnitario"],
            oci["almoxarifado"],
            oci["objetoCusto"]
        )


entradas_aba1 = criar_campos_verticais(aba1, campos_entrada_aba1)

# Botão para adicionar OCI na aba 1
btn_adicionar_oci_aba1 = tk.Button(aba1, text="Adicionar OCI", font=fonte, command=lambda: inserirOCI(entradas_aba1))
btn_adicionar_oci_aba1.grid(row=len(campos_entrada_aba1), columnspan=2, pady=(espacamento, 0))

btn_executar_oci_aba1 = tk.Button(aba1, text="Executar OCI", font=fonte, command=executarOCI)
btn_executar_oci_aba1.grid(row=len(campos_entrada_aba1) + 1, columnspan=2, pady=(espacamento, 0))

# Widget de texto para exibir listaOCI na aba 1
texto_lista = tk.Text(aba1, font=fonte, width=40, height=10, state='disabled')
texto_lista.grid(row=len(campos_entrada_aba1) + 2, columnspan=2, pady=(espacamento, 0))

# Aba 2
aba2 = ttk.Frame(notebook)
notebook.add(aba2, text='OCI FRUTAS')

# Campos de entrada com alinhamento vertical na aba 2
campos_entrada_aba2 = [
    ("Data da Nota:", ""),
    ("Código do Funcionário:", ""),
    ("Código do Fornecedor:", ""),
    ("Plano de Pagamento:", ""),
    ("Pagamento de Frete:", ""),
    ("Tipo de Frete:", ""),
    ("Tipo de Cobrança:", ""),
    ("Justificativa:", ""),
    ("Código do Material:", ""),
    ("Quantidade:", ""),
    ("Preço:", ""),
    ("Almoxarifado: ", ""),
    ("Objeto de Custo: ", "")
]

entradas_aba2 = criar_campos_verticais(aba2, campos_entrada_aba2)

# Botão para obter os dados na aba 2
btn_obter_dados_aba2 = tk.Button(aba2, text="Obter Dados", font=fonte, command=lambda: obter_dados(entradas_aba2))
btn_obter_dados_aba2.grid(row=len(campos_entrada_aba2), columnspan=2, pady=(espacamento, 0))

# Aba 3
aba3 = ttk.Frame(notebook)
notebook.add(aba3, text='XML FRUTAS')

# Usando a mesma estrutura da aba 2 na aba 3
entradas_aba3 = criar_campos_verticais(aba3, campos_entrada_aba2)

# Botão para obter os dados na aba 3
btn_obter_dados_aba3 = tk.Button(aba3, text="Obter Dados", font=fonte, command=lambda: obter_dados(entradas_aba3))
btn_obter_dados_aba3.grid(row=len(campos_entrada_aba2), columnspan=2, pady=(espacamento, 0))



# Aba 4
aba4 = ttk.Frame(notebook)
notebook.add(aba4, text='Manipular OCI')

# Função para adicionar um novo item à listaOCI
def adicionarItem():
    oci = {
        "dataOCI": entradas_aba4[0].get(),
        "codigoFornecedor": entradas_aba4[1].get(),
        "planoPagamento": entradas_aba4[2].get(),
        "planoFrete": entradas_aba4[3].get(),
        "tipoFrete": entradas_aba4[4].get(),
        "tipoCobranca": entradas_aba4[5].get(),
        "justificativa": entradas_aba4[6].get(),
        "codigoMaterial": entradas_aba4[7].get(),
        "quantidade": entradas_aba4[8].get(),
        "precoUnitario": entradas_aba4[9].get(),
        "almoxarifado": entradas_aba4[10].get(),
        "objetoCusto": entradas_aba4[11].get()
    }
    listaOCI.append(oci)
    print(listaOCI)

# Função para remover o item selecionado da listaOCI
def removerItem():
    index_selecionado = lista_oci_lista.curselection()[0]
    listaOCI.pop(index_selecionado)
    print(listaOCI)

# Campo de entrada e rótulo para cada atributo de OCI
campos_entrada_aba4 = [
    ("Data da Nota:", ""),
    ("Código do Fornecedor:", ""),
    ("Plano de Pagamento:", ""),
    ("Pagamento de Frete:", ""),
    ("Tipo de Frete:", ""),
    ("Tipo de Cobrança:", ""),
    ("Justificativa:", ""),
    ("Código do Material:", ""),
    ("Quantidade:", ""),
    ("Preço:", ""),
    ("Almoxarifado: ", ""),
    ("Objeto de Custo: ", "")
]

entradas_aba4 = []
for i, (texto, valor) in enumerate(campos_entrada_aba4):
    tk.Label(aba4, text=texto, font=fonte, fg=cor_texto).grid(row=i, column=0, sticky='w', padx=(10, 5), pady=(10, 0))
    entry = tk.Entry(aba4, font=fonte)
    entry.insert(0, valor)  # Insere o valor padrão no campo de entrada
    entry.grid(row=i, column=1, sticky='ew', padx=(0, 10), pady=(10, 0))
    entradas_aba4.append(entry)

# Botão para adicionar um novo item à listaOCI
btn_adicionar_aba4 = tk.Button(aba4, text="Adicionar OCI", font=fonte, command=adicionarItem)
btn_adicionar_aba4.grid(row=len(campos_entrada_aba4), columnspan=2, pady=(espacamento, 0))

# Listabox para exibir os itens da listaOCI
lista_oci_lista = tk.Listbox(aba4, font=fonte, width=40, height=10)
lista_oci_lista.grid(row=len(campos_entrada_aba4) + 1, columnspan=2, pady=(espacamento, 0))

# Botão para remover o item selecionado da listaOCI
btn_remover_aba4 = tk.Button(aba4, text="Remover OCI", font=fonte, command=removerItem)
btn_remover_aba4.grid(row=len(campos_entrada_aba4) + 2, columnspan=2, pady=(espacamento, 0))



root.mainloop()