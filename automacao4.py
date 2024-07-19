import pyautogui
import time

# Lista de posições para os cliques

# (1070, 100) ABRIR XMLS
# (1117, 36) EXPANDIR A TELA
# (680, 388) FILTRAR POR NÚMERO NFE
# DIGITAR NÚMERO DA NFE
# (404, 404) CLICAR NA NFE 2X
# (224, 94) CLICAR NO CAMPO CFOP
# DIGITAR CFOP 1.101
# CLICAR NO TAB
# DIGITAR CÓDIGO 5
# CLICAR NO TAB
# DIGITAR APLICAÇÃO 1
# (295, 550) CLICAR NO FILTRO
# DIGITAR NÚMERO DA OCI
# (170, 570) CLICAR 2X EM MARCAR
# (297, 637) CONFIRMAR VÍNCULO
# (60, 80) CLICAR EM "NOTA FISCAL"
# (515, 256) DIGITAR DATA DA NOTA
# (515, 256) DIGITAR 1
# (515, 256) DIGITAR 4
# (942, 677) CONFIRMAR ENTRADA
# (1214, 711) CRIAR NFE

def executar4(codigoMaterial):
    time.sleep(4)
    
    # Etapas do fluxo
    pyautogui.doubleClick((425, 270))  # codigo do material
    time.sleep(0.1)
    
    pyautogui.typewrite(codigoMaterial)
    time.sleep(0.5)
    
    pyautogui.press('tab')
    pyautogui.typewrite("2")
    time.sleep(0.1)
    
    pyautogui.press('tab')
    pyautogui.typewrite("11")
    time.sleep(0.1)
    
    pyautogui.press('tab')
    pyautogui.typewrite("01012024")
    time.sleep(0.1)
    pyautogui.press('tab')
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.press('enter')
    
    
codigos = [
90, 91, 199, 203, 267, 268, 270, 272, 313, 348, 538, 676, 2197, 3408, 3682
]
for codigo in codigos:
    executar4(str(codigo))