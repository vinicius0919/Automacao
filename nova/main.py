import xml.etree.ElementTree as ET
import pandas as pd

def processar_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()

    # Namespace usado no XML
    ns = {'nfe': 'http://www.portalfiscal.inf.br/nfe'}

    # Encontrando informações gerais da NF-e
    protNFe = root.find('nfe:protNFe', ns)
    nProt = protNFe.find('nfe:infProt/nfe:nProt', ns).text
    dhRecbto = protNFe.find('nfe:infProt/nfe:dhRecbto', ns).text
    chNFe = protNFe.find('nfe:infProt/nfe:chNFe', ns).text
    xMotivo = protNFe.find('nfe:infProt/nfe:xMotivo', ns).text

    # Encontrando detalhes dos produtos
    produtos = []
    for det in root.findall('nfe:NFe/nfe:infNFe/nfe:det', ns):
        nItem = det.find('nfe:nItem', ns).text
        cProd = det.find('nfe:prod/nfe:cProd', ns).text
        xProd = det.find('nfe:prod/nfe:xProd', ns).text
        ncm = det.find('nfe:prod/nfe:NCM', ns).text
        qCom = det.find('nfe:prod/nfe:qCom', ns).text
        vProd = det.find('nfe:prod/nfe:vProd', ns).text
        uCom = det.find('nfe:prod/nfe:uCom', ns).text
        vUnCom = det.find('nfe:prod/nfe:vUnCom', ns).text
        CFOP = det.find('nfe:prod/nfe:CFOP', ns).text

        produtos.append({
            'nItem': nItem,
            'cProd': cProd,
            'NCM': ncm,
            'xProd': xProd,
            'qCom': qCom,
            'vProd': vProd,
            'uCom': uCom,
            'vUnCom': vUnCom,
            'CFOP': CFOP
        })

    # Exibindo as informações extraídas
    print(f'Número do Protocolo: {nProt}')
    print(f'Data/Hora do Recebimento: {dhRecbto}')
    print(f'Chave da NF-e: {chNFe}')
    print(f'Motivo da Autorização: {xMotivo}')
    print('Detalhes dos Produtos:')
    for produto in produtos:
        print(f" - Item {produto['nItem']}: {produto['xProd']} - Quantidade: {produto['qCom']} {produto['uCom']} - Valor Total: R$ {produto['vProd']}")
    return produtos


def salvar_para_excel(detalhes_produtos, excel_file):
    # Criando um DataFrame com os detalhes dos produtos
    df = pd.DataFrame(detalhes_produtos)

    # Escrevendo no arquivo Excel
    df.to_excel(excel_file, index=False)

    print(f"Dados salvos com sucesso em {excel_file}")
    
# Caminho para o arquivo XML local
file_path = "input.xml"
# Processando o XML
salvar_para_excel(processar_xml(file_path), "output.xlsx")