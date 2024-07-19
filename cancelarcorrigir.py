import pyautogui
import time

a = [
#["23291","1,55"],
]


def tabular(n):
    for i in range(n):
        pyautogui.press('tab')

def desintegrar(i):
    pyautogui.doubleClick(355,94)
    pyautogui.typewrite(a[i][0])
    pyautogui.press('enter')
    time.sleep(3)
    
    pyautogui.click(633,124)
    time.sleep(1)
    
    pyautogui.click(433,663)
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(5)
    #pyautogui.hotkey("alt", "tab")
    #time.sleep(1)
    #pyautogui.hotkey("alt", "tab")
    #time.sleep(0.6)
    pyautogui.press('enter')

    
def corrigiriten():
    pyautogui.click(354,126) #clicar na aba iten
    time.sleep(1)
    
    pyautogui.click(1006,661) #desfazer vinculo
    time.sleep(3)
    
    pyautogui.click(385,495)
    time.sleep(1)
    
    pyautogui.doubleClick(385,495)
    time.sleep(1)
    
    pyautogui.press('0')
    
    pyautogui.click(526, 163)
    time.sleep(1)
    
    pyautogui.click(833,96)
    time.sleep(0.6)
    
def vincular(i):
    pyautogui.click(640,253)
    tabular(3)
    
    pyautogui.typewrite("1")
    time.sleep(0.6)
    
    pyautogui.press('tab')
    time.sleep(0.6)
    
    pyautogui.typewrite(a[i][1])
    time.sleep(1)
    
    pyautogui.click(1001, 492)
    
def rotinafiscal():
    pyautogui.click(902, 122)
    time.sleep(1)
    
    pyautogui.click(848, 94)
    time.sleep(1)
    
    pyautogui.typewrite("40")
    tabular(6)
    
    pyautogui.typewrite("7")
    time.sleep(0.2)
    
    tabular(5)
    
    pyautogui.typewrite("26")
    time.sleep(0.2)
    
    tabular(2)
    
    pyautogui.typewrite("59")
    time.sleep(0.2)
    
    pyautogui.click(910, 666)
    time.sleep(0.5)
    
    pyautogui.press("f9")
    
    pyautogui.click(1011, 659)
    time.sleep(0.5)

def financeiro():
    pyautogui.click(416,124)
    time.sleep(0.5)
    
    pyautogui.click(1029,325)
    time.sleep(0.5)
    
    pyautogui.press("enter")

def dadosnf():
    pyautogui.click(295,124)
    time.sleep(1)
    
    pyautogui.doubleClick(622,401)
    time.sleep(0.5)
    
    pyautogui.typewrite("0")
    
    pyautogui.press("tab")
    
    pyautogui.typewrite("0")
    
    pyautogui.click(744,654)
    time.sleep(1)
    pyautogui.press("enter")
    
    pyautogui.click(1060, 656)
    time.sleep(1)
    pyautogui.press("enter")
    
    
for i in range(5):    
    time.sleep(4)

    desintegrar(i)
    time.sleep(2)
    corrigiriten()
    time.sleep(2)
    vincular(i)
    time.sleep(2)
    rotinafiscal()
    time.sleep(2)
    financeiro()
    time.sleep(1)
    dadosnf()

    pyautogui.click(600,300)
    pyautogui.press('esc')
    time.sleep(1)
    pyautogui.press('enter')