import os
import xml.etree.ElementTree as ET
import pyautogui
import time

class OC:
    def __init__(self, cnpj, plano_pagamento, plano_pagamento_frete, tipo_frete, justificativa_compra, codigo_material, descricao_material, quantidade_material, preco_unitario, almoxarifado, objeto_custo, data_emissao):
        self.cnpj = cnpj
        self.plano_pagamento = plano_pagamento
        self.plano_pagamento_frete = plano_pagamento_frete
        self.tipo_frete = tipo_frete
        self.justificativa_compra = justificativa_compra
        self.codigo_material = codigo_material
        self.descricao_material = descricao_material
        self.quantidade_material = quantidade_material
        self.preco_unitario = preco_unitario
        self.almoxarifado = almoxarifado
        self.objeto_custo = objeto_custo
        self.data_emissao = data_emissao

    def __str__(self):
        return (f'CNPJ: {self.cnpj}, Plano de Pagamento: {self.plano_pagamento}, Plano de Pagamento do Frete: {self.plano_pagamento_frete}, '
                f'Tipo de Frete: {self.tipo_frete}, Justificativa de Compra: {self.justificativa_compra}, Código do Material: {self.codigo_material}, '
                f'Descrição do Material: {self.descricao_material}, Quantidade do Material: {self.quantidade_material}, Preço Unitário: {self.preco_unitario}, '
                f'Almoxarifado: {self.almoxarifado}, Objeto de Custo: {self.objeto_custo}, Data de Emissão: {self.data_emissao}')

def parse_xml_file(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()

    # Namespaces in XML files
    namespaces = {'ns': 'http://www.portalfiscal.inf.br/nfe'}

    # Extracting the information
    cnpj = root.find('.//ns:emit/ns:CNPJ', namespaces).text
    plano_pagamento = root.find('.//ns:dup/ns:nDup', namespaces).text
    plano_pagamento_frete = "37" #root.find('.//ns:dup/ns:vDup', namespaces).text
    tipo_frete = "4" #root.find('.//ns:transp/ns:modFrete', namespaces).text
    justificativa_compra = root.find('.//ns:infAdic/ns:infCpl', namespaces).text
    descricao_material = root.find('.//ns:prod/ns:xProd', namespaces).text
    quantidade_material = root.find('.//ns:prod/ns:qCom', namespaces).text
    preco_unitario = root.find('.//ns:prod/ns:vUnCom', namespaces).text

    data_emissao_crua = root.find('.//ns:ide/ns:dhEmi', namespaces).text
    ano = data_emissao_crua.replace("-","")[0:4],
    mes = data_emissao_crua.replace("-","")[4:6]
    dia = data_emissao_crua.replace("-","")[6:8]
    data_emissao = str(dia) + str(mes) + str(ano)
    almoxarifado = "99"  # Placeholder, needs appropriate XML path
    if descricao_material.find("LARANJA") != -1: 
        codigo_material = "319"
        objeto_custo = "222"  # Placeholder, needs appropriate XML path
    else:
        codigo_material = "1135"
        objeto_custo = "223"

    # Creating an instance of OC
    oc_instance = OC(cnpj, plano_pagamento, plano_pagamento_frete, tipo_frete, justificativa_compra, codigo_material, descricao_material, quantidade_material, preco_unitario, almoxarifado, objeto_custo, data_emissao)
    return oc_instance

def executar2(dataOCI, codigoFornecedor, planoPagamento, planoFrete, tipoFrete, tipoCobranca, justificativa, codigoMaterial, quantidade, precoUnitario, almoxarifado, objetoCusto):
    # Etapas do fluxo
    time.sleep(6)
    pyautogui.press('f5')
    pyautogui.press('enter')
    pyautogui.click((494, 191))  # clicar na data
    time.sleep(0.2)

    print(float(str(quantidade).replace(",", ".")), " x ", float(str(precoUnitario).replace(",", ".")), " = ", float(str(quantidade).replace(",", ".")) * float(str(precoUnitario).replace(",", ".")))

    pyautogui.typewrite(dataOCI)  # DIGITAR data da oci
    time.sleep(0.2)
    pyautogui.press("tab")

    pyautogui.typewrite("281")  # codigo do funcionario
    time.sleep(0.2)
    pyautogui.press("tab")
    pyautogui.press("tab")
    
    pyautogui.typewrite(codigoFornecedor)  # codigo do fornecedor
    time.sleep(0.2)
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

    pyautogui.typewrite("AQUISICAO DE MATERIA PRINA")
    pyautogui.hotkey('ctrl', 'enter')
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
    
    if codigoMaterial == "319":
        quantidade = str(float(quantidade) / 1000)
        precoUnitario = float(precoUnitario)*1000
        quantidade = quantidade.replace(".", ",")
    pyautogui.typewrite(quantidade.replace(".",","))  # digitar a quantidade
    time.sleep(0.2)
    pyautogui.press("tab")

    pyautogui.typewrite(str(precoUnitario).replace(".",","))  # digitar o preço da unidade do material
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
    pyautogui.typewrite("AQUISICAO DE MATERIA PRIMA.\n"+str(justificativa))  # digitar o objeto de custo
    pyautogui.press('f2')
    time.sleep(0.2)
    pyautogui.click(334, 671)

def process_xml_files_in_directory(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.xml'):
            file_path = os.path.join(directory, filename)
            oc_instance = parse_xml_file(file_path)
            print(oc_instance)
            time.sleep(4)
            executar2(
                oc_instance.data_emissao,
                oc_instance.cnpj,
                oc_instance.plano_pagamento,
                oc_instance.plano_pagamento_frete,
                oc_instance.tipo_frete,
                "2",  # Tipo de cobrança, substitua se necessário
                oc_instance.justificativa_compra,
                oc_instance.codigo_material,
                oc_instance.quantidade_material,
                oc_instance.preco_unitario,
                oc_instance.almoxarifado,
                oc_instance.objeto_custo
            )

# Exemplo de uso
directory_path = 'xml/'
process_xml_files_in_directory(directory_path)
