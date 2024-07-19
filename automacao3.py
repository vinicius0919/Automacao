import tkinter as tk
from tkinter import ttk

import pyautogui
import time

# Variável global para armazenar o valor de x
last_x_position = 627   

# Lista para armazenar os itens
itens_array = []

def executar3(justificativa, codigoMaterial, quantidade, precoUnitario, almoxarifado, objetoCusto):
    global last_x_position
    
    time.sleep(4)
    pyautogui.hotkey("ctrl", "left")
    time.sleep(0.2)
    pyautogui.press("tab")
    
    pyautogui.typewrite(codigoMaterial)  
    for i in range(3):
        time.sleep(0.2)
        pyautogui.press("tab")
        
    time.sleep(0.2)
    pyautogui.typewrite(quantidade)  
    time.sleep(0.2)
    pyautogui.press("tab")
    
    pyautogui.typewrite(precoUnitario)  
    time.sleep(0.2)
    pyautogui.click(739, 627)
    time.sleep(0.2)
    pyautogui.click(739, 627)
    time.sleep(0.2)
    pyautogui.click(831, 627)
    for i in range(16):
        pyautogui.press("tab")

    pyautogui.typewrite(almoxarifado)  
    time.sleep(0.2)
    for i in range(5):
        pyautogui.press("tab")

    pyautogui.typewrite(objetoCusto)  
    time.sleep(0.2)
    for i in range(16):
        pyautogui.press("tab")
    
    pyautogui.press('f2')
    pyautogui.typewrite(str(justificativa))  
    pyautogui.press('f2')
    time.sleep(0.2)
    pyautogui.press('down')
    
    # Atualiza a posição x para o próximo item
    if last_x_position< 622:
        last_x_position += 17

def submit_item():
    item = {
        "justificativa": justificativa_entry.get(),
        "codigoMaterial": codigo_entry.get(),
        "quantidade": quantidade_entry.get(),
        "precoUnitario": preco_entry.get(),
        "almoxarifado": almoxarifado_entry.get(),
        "objetoCusto": objeto_custo_entry.get()
    }
    itens_array.append(item)
    print(itens_array)

def clear_entries():
    justificativa_entry.delete(0, tk.END)
    codigo_entry.delete(0, tk.END)
    quantidade_entry.delete(0, tk.END)
    preco_entry.delete(0, tk.END)
    almoxarifado_entry.delete(0, tk.END)
    objeto_custo_entry.delete(0, tk.END)

def execute_items():
    global last_x_position
    J = justificativa_entry.get()
    for item in itens_array:
        codigoMaterial = item["codigoMaterial"]
        quantidade = item["quantidade"]
        precoUnitario = item["precoUnitario"]
        almoxarifado = item["almoxarifado"]
        objetoCusto = item["objetoCusto"]
        executar3(J, codigoMaterial, quantidade, precoUnitario, almoxarifado, objetoCusto)

def clear_items():
    global last_x_position
    last_x_position = 440
    itens_array.clear()

def update_x():
    global last_x_position
    new_x = x_entry.get()
    try:
        last_x_position = int(new_x)
    except ValueError:
        pass
    x_value_label.config(text=str(last_x_position))

root = tk.Tk()
root.title("Formulário de Itens")

# Criação dos campos do formulário
tk.Label(root, text="Justificativa:").grid(row=0, column=0, sticky="w")
justificativa_entry = tk.Entry(root)
justificativa_entry.grid(row=0, column=1)

tk.Label(root, text="Código do Material:").grid(row=1, column=0, sticky="w")
codigo_entry = tk.Entry(root)
codigo_entry.grid(row=1, column=1)

tk.Label(root, text="Quantidade:").grid(row=2, column=0, sticky="w")
quantidade_entry = tk.Entry(root)
quantidade_entry.grid(row=2, column=1)

tk.Label(root, text="Preço Unitário:").grid(row=3, column=0, sticky="w")
preco_entry = tk.Entry(root)
preco_entry.grid(row=3, column=1)

tk.Label(root, text="Almoxarifado:").grid(row=4, column=0, sticky="w")
almoxarifado_entry = tk.Entry(root)
almoxarifado_entry.grid(row=4, column=1)

tk.Label(root, text="Objeto de Custo:").grid(row=5, column=0, sticky="w")
objeto_custo_entry = tk.Entry(root)
objeto_custo_entry.grid(row=5, column=1)

# Exibir e alterar valor de x
tk.Label(root, text="Valor de x:").grid(row=6, column=0, sticky="w")
x_value_label = tk.Label(root, text=str(last_x_position))
x_value_label.grid(row=6, column=1, sticky="w")

tk.Label(root, text="Novo valor de x:").grid(row=7, column=0, sticky="w")
x_entry = tk.Entry(root)
x_entry.grid(row=7, column=1)

# Botões
submit_button = tk.Button(root, text="Adicionar Item", command=submit_item)
submit_button.grid(row=8, column=0, columnspan=2, pady=10)

clear_button = tk.Button(root, text="Limpar Itens", command=clear_items)
clear_button.grid(row=9, column=0, columnspan=2, pady=10)

execute_button = tk.Button(root, text="Executar Itens", command=execute_items)
execute_button.grid(row=10, column=0, columnspan=2, pady=10)

update_x_button = tk.Button(root, text="Atualizar x", command=update_x)
update_x_button.grid(row=7, column=2, padx=10)

root.mainloop()
