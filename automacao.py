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

def executar(numeroNfe, dataNfe, numeroOci):
    # Etapas do fluxo
    pyautogui.click((1070, 100))  # ABRIR XMLS
    time.sleep(4)
    
    pyautogui.click((1117, 36))   # EXPANDIR A TELA
    time.sleep(2)

    pyautogui.click((680, 388))   # EXPANDIR A TELA
    pyautogui.typewrite(numeroNfe)  # DIGITAR NÚMERO NFE

    time.sleep(2)
    pyautogui.doubleClick((404, 404))   # CLICAR NA NFE 2X

    time.sleep(6)
    pyautogui.click((217, 95)) # CLICAR NO CAMPO CFOP
    pyautogui.typewrite('1.101')   # DIGITAR CFOP

    time.sleep(1)
    pyautogui.press('tab')   # CLICAR NO TAB
    pyautogui.typewrite('5')   # DIGITAR CÓDIGO

    time.sleep(1)
    pyautogui.press('tab')   # DAR UM TAB

    time.sleep(18)
    pyautogui.typewrite('1')   # DIGITAR APLICAÇÃO
    pyautogui.press('tab')   # DAR UM TAB
    time.sleep(13)

    pyautogui.click(295, 550) #clicar no filtro
    pyautogui.typewrite(numeroOci) #digitar o numero da oci

    time.sleep(1)
    pyautogui.click((200, 570))   # CLICAR 2X EM MARCAR
    pyautogui.click((170, 570))

    time.sleep(1)
    pyautogui.click((297, 637))   # CONFIRMAR VÍNCULO

    time.sleep(3)
    pyautogui.click((60, 80))     # CLICAR EM "NOTA FISCAL"

    time.sleep(2)
    pyautogui.click((515, 256)) # CLICAR CAMPO DATA DE ENTRADA
    pyautogui.typewrite(dataNfe)   # DIGITAR DATA DE ENTRADA
    pyautogui.press('tab') # DAR UM TAB
    pyautogui.press('tab') # DAR UM TAB
    pyautogui.typewrite('1')   # DIGITAR PLANO DE PAGAMENTO

    pyautogui.press('tab') # DAR UM TAB
    pyautogui.typewrite('4')   # DIGITAR TIPO DE FRETE
    pyautogui.press('tab') # DAR UM TAB

    time.sleep(1)
    pyautogui.click((942, 677))   # CONFIRMAR ENTRADA

    time.sleep(1)
    pyautogui.click((1214, 711))  # CRIAR NFE

    time.sleep(1)
    pyautogui.click((750, 508))  # CLICAR SIM 1
    
    time.sleep(1)
    pyautogui.click((750, 515))  # CLICAR SIM 2

    time.sleep(1)
    pyautogui.click((750, 530))  # CLICAR SIM 3
    
    time.sleep(1)
    pyautogui.click((750, 515))  # CLICAR SIM 4
    
    time.sleep(4)
    pyautogui.click((1057, 657))  # CLICAR EM FINALIZAR
    
    time.sleep(1)
    pyautogui.press('enter')  # PRESSIONAR ENTER
