import pyautogui
import time
import pandas as pd

def addItens(codigoMaterial, quantidade, precoUnitario, almoxarifado, justificativa):
    pyautogui.press('down')
    pyautogui.hotkey("ctrl", "left")
    pyautogui.press("tab")
    
    pyautogui.typewrite(codigoMaterial)  # digitar o código do material
    for i in range(3):
        pyautogui.press("tab")
    
    pyautogui.typewrite(quantidade)  # digitar a quantidade
    time.sleep(0.2)
    pyautogui.press("tab")

    pyautogui.typewrite(precoUnitario)  # digitar o preço da unidade do material
    time.sleep(0.2)
    for i in range(16):
        pyautogui.press("tab")

    pyautogui.typewrite(almoxarifado)  # almoxarifado de destino
    time.sleep(0.2)
    for i in range(11):
        pyautogui.press("tab")
    
    pyautogui.press('f2')
    pyautogui.typewrite(str(justificativa))  # digitar o objeto de custo
    pyautogui.press('f2')
    time.sleep(0.2)

def lerTabela(tabela):
    time.sleep(4)
    # Lendo a tabela
    df = pd.read_csv(tabela, sep=';')
    
    # Iterando sobre as linhas da tabela
    for index, row in df.iterrows():
        codigoMaterial = str(row['Codigo Interno'])
        quantidade = str(row['Quantidade']).replace(".",",")
        precoUnitario = str(row['Valor Unitario']).replace(".",",")
        almoxarifado = '1'
        justificativa = 'MATERIAL PARA USO NA MANUTENCAO, SOLDA E AMPLIACAO DA FABRICA'
        if index>=17:
            addItens(codigoMaterial, quantidade, precoUnitario, almoxarifado, justificativa)


# Chamar a função lerTabela com o nome do arquivo da tabela como argumento
lerTabela('new.csv')
