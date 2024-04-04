import pyautogui
import time

# Lista de posições para os cliques

# (494, 191) clicar data


def executar2(dataOCI, codigoFornecedor, planoPagamento, planoFrete, tipoFrete, tipoCobranca, justificativa, codigoMaterial, quantidade, precoUnitario, almoxarifado, objetoCusto):
    # Etapas do fluxo
    time.sleep(4)
    print(str(justificativa))
    pyautogui.press('f5')
    pyautogui.press('enter')
    pyautogui.click((494, 191))  # clicar da data
    time.sleep(0.2)

    
    pyautogui.typewrite(dataOCI)  # DIGITAR data da oci
    time.sleep(0.2)
    pyautogui.press("tab")

    pyautogui.typewrite("281")  # codigo do funcionario
    time.sleep(0.2)
    pyautogui.press("tab")
    
    pyautogui.typewrite(codigoFornecedor)  # codigo do fornecedor
    time.sleep(0.2)
    pyautogui.press("tab")
    pyautogui.press("tab")
    
    pyautogui.typewrite(planoPagamento)  # plano de pagamento
    time.sleep(0.2)
    pyautogui.press("tab")
        
    pyautogui.typewrite(planoFrete)  # plano de frete
    time.sleep(0.2)
    pyautogui.press("tab")
    
    pyautogui.typewrite(tipoFrete)  # tipo de frete
    time.sleep(0.2)
    pyautogui.press("tab")
    
    pyautogui.typewrite(tipoCobranca)  # tipo de cobrança
    time.sleep(0.2)
    for i in range(7):
        pyautogui.press("tab")

    pyautogui.typewrite(str(justificativa))  # justificativa central
    time.sleep(0.2)
    pyautogui.press("tab")
    
    pyautogui.hotkey("ctrl", "left")
    pyautogui.press("tab")
    
    pyautogui.typewrite(codigoMaterial[0])  # digitar o código do material
    pyautogui.press('enter')
    pyautogui.typewrite(codigoMaterial[1:])  # digitar o código do material
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
    for i in range(5):
        pyautogui.press("tab")

    pyautogui.typewrite(objetoCusto)  # digitar o objeto de custo
    time.sleep(0.2)
    for i in range(16):
        pyautogui.press("tab")
    
    pyautogui.press('f2')
    pyautogui.typewrite(str(justificativa))  # digitar o objeto de custo
    pyautogui.press('f2')
    time.sleep(0.2)
    pyautogui.click(334,671)
    

#quantidade = ["18927", "37644","18157","36055","15701","17840"]
#for i in range(len(quantidade)):
#    executar2("01042024","1252","125","37","4","2","AQUISICAO DE MATERIA-PRIMA PARA FINS DE INDUSTRIALIZACAO", "1135", quantidade[i],"0,2","99","223")
