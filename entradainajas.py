import pyautogui
import time

def tabular(x):
    if x>1:
        for i in range(x):
            pyautogui.press('tab')
            time.sleep(0.1)
    else:
        pyautogui.press('tab')


def infoNota(data, nnota, snota, cfornecedor, pagamento, valor, chave):
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

    pyautogui.typewrite('55')
    time.sleep(0.3)
    tabular(1)
    
    pyautogui.typewrite(pagamento)
    time.sleep(0.3)
    tabular(6)
    
    pyautogui.typewrite(chave)
    time.sleep(0.3)
    tabular(3)
    
    pyautogui.typewrite(str(valor).replace(".",","))
    time.sleep(0.3)
    tabular(1)
    
    pyautogui.typewrite(str(float(valor)*0.19).replace(".",","))
    time.sleep(0.3)
    tabular(11)
    1712,20 

    pyautogui.typewrite(str(valor).replace(".",","))
    time.sleep(0.3)
    tabular(6)
    
    pyautogui.typewrite(str(valor).replace(".",","))
    time.sleep(0.3)
    tabular(1)
    
    pyautogui.press('enter')

def vincularOCI(noci):
    pyautogui.click(353,126)
    time.sleep(1)
    
    pyautogui.click(506,253)
    time.sleep(3)
    
    tabular(8)
    
    pyautogui.typewrite("1.101")
    time.sleep(0.3)
    tabular(1)
    
    pyautogui.typewrite("2")
    time.sleep(0.3)
    tabular(1)
    
    pyautogui.typewrite("1")
    time.sleep(0.3)
    tabular(1)
    
    pyautogui.click(425,245)
    time.sleep(0.3)

    pyautogui.typewrite(str(noci))
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
    time.sleep(0)
    
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

def lancarcavaco(data, nnota, snota, cfornecedor, pagamento, valor, noci, chave):
    
    infoNota(data, nnota, snota, cfornecedor, pagamento, valor, chave)
    
    vincularOCI(noci)
    
    gerarFinanceiro()
    
keys = [
"15240412230816000190550010000067571127819938",
"15240412230816000190550010000067581303168148",
"15240412230816000190550010000067591303206691",
"15240412230816000190550010000067601303255022"
]

num = [
    "6757","6758","6759","6760"
]

preco = [
    "1239.00","1842.40","1664.60","1635.20"
]
datas = [
    "15042024","170420224","170420224","170420224"
]
time.sleep(4)
oci = 12852

for i in range(len(keys)):
    print(keys[i])
    lancarcavaco(datas[i],num[i],"1","163","125",preco[i], str(oci), keys[i])
    oci +=1
