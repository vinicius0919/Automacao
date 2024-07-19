import pyautogui
import time

def tabular(x):
    if x>1:
        for i in range(x):
            pyautogui.press('tab')
            time.sleep(0.1)
    else:
        pyautogui.press('tab')


def infoNota(data, nnota, snota, cfornecedor, pagamento, valor):
    pyautogui.click(710,100)
    time.sleep(0.5)
    
    pyautogui.doubleClick(540,100)
    time.sleep(0.4)

    pyautogui.typewrite(data)
    time.sleep(0.3)
    tabular(1)
    
    pyautogui.typewrite(nnota)
    time.sleep(0.3)
    tabular(1)

    pyautogui.typewrite(snota)
    time.sleep(0.3)
    tabular(1)
    
    pyautogui.typewrite(cfornecedor)
    time.sleep(0.3)
    tabular(2)
    
    pyautogui.typewrite('4')
    time.sleep(0.3)
    tabular(1)

    pyautogui.typewrite('1')
    time.sleep(0.3)
    tabular(1)
    
    pyautogui.typewrite(pagamento)
    time.sleep(0.3)
    tabular(23)
    
    pyautogui.typewrite(valor)
    time.sleep(0.3)
    tabular(4)
    
    pyautogui.typewrite(valor)
    time.sleep(0.3)
    tabular(1)
    
    pyautogui.press('enter')

def vincularOCI(noci):
    pyautogui.click(353,126)
    time.sleep(0.3)
    
    pyautogui.click(506,253)
    time.sleep(1)
    
    pyautogui.click(405,165)
    time.sleep(1)
    
    pyautogui.typewrite("1.933")
    time.sleep(0.3)
    tabular(1)
    
    pyautogui.typewrite("1")
    time.sleep(0.3)
    tabular(1)
    
    pyautogui.typewrite("1")
    time.sleep(0.3)
    tabular(1)
    
    pyautogui.click(425,245)
    time.sleep(0.3)

    pyautogui.typewrite(noci)
    time.sleep(0.3)
    tabular(1)
    
    pyautogui.click(468,389)
    time.sleep(0.3)
    
    pyautogui.click(649,422)
    time.sleep(0.3)
    
    pyautogui.click(922,700)
    time.sleep(0.3)

    pyautogui.press('enter')
    time.sleep(0.3)
    pyautogui.press('enter')
    time.sleep(4)

def gerarFinanceiro():
    pyautogui.click(412,126)
    time.sleep(0.3)
    
    pyautogui.click(1026,327)
    time.sleep(0.3)
    
    pyautogui.press('enter')
    time.sleep(0.3)
    
    pyautogui.click(295,126)
    time.sleep(0.3)
    
    pyautogui.click(1045,650)
    time.sleep(0.3)
    
    pyautogui.press('enter')
    time.sleep(0.3)

def lancarservico(data, nnota, snota, cfornecedor, pagamento, valor, noci):
    
    infoNota(data, nnota, snota, cfornecedor, pagamento, valor)
    
    vincularOCI(noci)
    
    gerarFinanceiro()
    



time.sleep(4)
lancarservico("11042024","115","0","1616","125","3348,75","12722")

