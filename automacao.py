import pyautogui
import time
import keyboard

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

stop_flag = False

def stop_execution():
    global stop_flag
    stop_flag = True    

def executar(numeroNfe, planoPagamento, tipoFrete, dataNfe, numeroOci, tempo):
    global stop_flag
    stop_flag = False

    # Start a listener for the "Esc" key
    keyboard.add_hotkey('esc', stop_execution)
    try:
        # Etapas do fluxo
        pyautogui.click((1070, 100))  # ABRIR XMLS
        time.sleep(5)
        if stop_flag: return

        pyautogui.click((1117, 36))   # EXPANDIR A TELA
        time.sleep(2)
        if stop_flag: return
        pyautogui.click((680, 388))   # CAMPO NUMERO DA NOTA
        pyautogui.typewrite(numeroNfe)  # DIGITAR NÚMERO NFE
        if stop_flag: return
        time.sleep(2)
        pyautogui.doubleClick((404, 404))   # CLICAR NA NFE 2X
        if stop_flag: return
        time.sleep(7)
        pyautogui.click((217, 95)) # CLICAR NO CAMPO CFOP
        if stop_flag: return
        pyautogui.typewrite('1.101')   # DIGITAR CFOP
        if stop_flag: return
        time.sleep(0.5)
        pyautogui.press('tab')   # CLICAR NO TAB
        if stop_flag: return
        pyautogui.typewrite('5')   # DIGITAR CÓDIGO

        time.sleep(0.5)
        pyautogui.press('tab')   # DAR UM TAB
        if stop_flag: return
        time.sleep(int(tempo))

        pyautogui.click(295, 550) #clicar no filtro
        if stop_flag: return
        pyautogui.typewrite(numeroOci) #digitar o numero da oci
        if stop_flag: return
        time.sleep(1)
        pyautogui.click((200, 570))   # CLICAR 2X EM MARCAR
        if stop_flag: return
        pyautogui.click((170, 570))

        time.sleep(1)
        pyautogui.click((297, 637))   # CONFIRMAR VÍNCULO
        if stop_flag: return
        time.sleep(1)
        pyautogui.press('enter')   # CONFIRMAR VÍNCULO
        if stop_flag: return
        time.sleep(2)
        pyautogui.click(604,100)
        if stop_flag: return
        pyautogui.typewrite('1')   # DIGITAR APLICAÇÃO
        if stop_flag: return
        pyautogui.press('tab')   # DAR UM TAB
        if stop_flag: return
        time.sleep(2)
        pyautogui.click((60, 80))     # CLICAR EM "NOTA FISCAL"
        if stop_flag: return
        time.sleep(4)
        pyautogui.doubleClick((515, 256)) # CLICAR CAMPO DATA DE ENTRADA
        if stop_flag: return
        pyautogui.typewrite(dataNfe)   # DIGITAR DATA DE ENTRADA
        if stop_flag: return
        pyautogui.press('tab') # DAR UM TAB
        if stop_flag: return
        pyautogui.press('tab') # DAR UM TAB
        if stop_flag: return
        pyautogui.typewrite(planoPagamento)   # DIGITAR PLANO DE PAGAMENTO
        if stop_flag: return

        pyautogui.press('tab') # DAR UM TAB
        if stop_flag: return
        pyautogui.typewrite(tipoFrete)   # DIGITAR TIPO DE FRETE
        if stop_flag: return
        pyautogui.press('tab') # DAR UM TAB
        if stop_flag: return
        time.sleep(1)
        pyautogui.click((942, 677))   # CONFIRMAR ENTRADA
        if stop_flag: return
        time.sleep(1)
        pyautogui.click((1214, 711))  # CRIAR NFE
        if stop_flag: return
        time.sleep(1)
        pyautogui.press('enter')  # CLICAR SIM 1
        if stop_flag: return
        time.sleep(1)
        pyautogui.press('enter')  # CLICAR SIM 1
        if stop_flag: return
        time.sleep(1)
        pyautogui.press('enter')  # CLICAR SIM 1
        if stop_flag: return
        time.sleep(1)
        pyautogui.press('enter')  # CLICAR SIM 1
        if stop_flag: return
        time.sleep(1)
        pyautogui.press('enter')  # CLICAR SIM 1
        if stop_flag: return
        time.sleep(6)
        pyautogui.click(1060,654)
        if stop_flag: return
        time.sleep(3)
        pyautogui.press('enter')  # CLICAR SIM 1
        if stop_flag: return
        time.sleep(6)
        pyautogui.click(630,250)
        if stop_flag: return
        time.sleep(1)
        pyautogui.press('esc')
        if stop_flag: return
        time.sleep(1)
        pyautogui.press('enter')  # CLICAR SIM 1
        if stop_flag: return
        time.sleep(1)
        pyautogui.press('enter')  # CLICAR SIM 2
        if stop_flag: return
        time.sleep(4)
    finally:
        # Remove the hotkey listener
        keyboard.remove_hotkey('esc')