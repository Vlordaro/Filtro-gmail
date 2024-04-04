import re
import os
from unidecode import unidecode

def substituir_numeros_e_nomes(xml_modelo, numeros, nomes):
    xmls_substituidos = []
    for numero, nome in zip(numeros, nomes):
        xml_substituido = re.sub(r'16667', str(numero), xml_modelo)
        xml_substituido = xml_substituido.replace('Sorocaba Comitre', nome)
        xmls_substituidos.append(xml_substituido)
    return xmls_substituidos

def remover_acentos_e_pontuacao(texto):
    texto_sem_acentos = unidecode(texto)
    texto_sem_pontuacao = ''.join(char if char.isalnum() else ' ' for char in texto_sem_acentos)
    return texto_sem_pontuacao

def salvar_xmls(xmls, pasta_saida, nome_arquivo):
    caminho_arquivo = f"{pasta_saida}/{nome_arquivo}.xml"
    with open(caminho_arquivo, "w") as arquivo:
        for i, xml in enumerate(xmls, 1):
            comentario = f"  <!-- XML {i} -->"
            comentario_sem_acentos_e_pontuacao = remover_acentos_e_pontuacao(comentario)
            arquivo.write(f"{comentario_sem_acentos_e_pontuacao}{xml.strip()}\n")
    print(f"Arquivo XML {caminho_arquivo} salvo com sucesso!")

# Modelo do XML
xml_modelo = """
    <entry>
        <category term='filter'></category>
        <title>Mail Filter</title>
        <id>tag:mail.google.com,2008:filter:z0000001712170392188*0762266119029245638</id>
        <updated>2024-04-03T18:53:39Z</updated>
        <content></content>
        <apps:property name='subject' value='BK-16667-WIN01 ( Alerta do Kernel-Power ID 41 )'/>
        <apps:property name='label' value='Lojas/16667Sorocaba Comitre'/>
        <apps:property name='sizeOperator' value='s_sl'/>
        <apps:property name='sizeUnit' value='s_smb'/>
    </entry>
"""

# Números para substituir
numeros = [
    15374, 16667, 17257, 17973, 18334, 18870, 18942, 19615, 19660, 20414,
    21530, 21532, 21830, 22516, 22709, 23740, 24742, 24744, 24764, 25446,
    25669, 26433, 26434, 26436, 26439, 26811, 26815, 26817, 26827, 26841,
    27466, 27468, 27476, 27593, 28086, 28365, 28370, 28372, 29095, 29919,
    30074, 30088, 30202, 30470, 30664, 30826, 30904, 31016, 31059, 31060,
    31061, 31062, 31063, 31065, 31066, 31068, 31302, 31303, 31306, 31306,
    31460, 31604, 31608
]

# Nomes para substituir
nomes = [
    "-Helio-Pellegrino-", "-Soroc-Comitre-", "-Jundiai-Av-Nove-de-Julho-",
    "-Prestes-Maia-", "-Radial-Leste-", "-Rib-Preto-Av-Portugal-", "-Jacu-Pessego-",
    "-Bandeirantes-", "-Extra-Jaguare-", "-Sorocaba-Av-SP-", "-M-Tiete-Pte-Aricanduva-",
    "-Sorocaba-Av-Pannunzio-", "-Soroc-Afonso-Vergueiro-", "-Sto-Andre-Dom-Pedro-",
    "-Marechal-Tito-I", "-Moreira-Guimaraes-", "-Bias-Fortes-", "-Vicente-Rao-",
    "-JK-", "-Ricardo-Jafet-", "-Marechal-Tito-II", "-Prestes-Maia-Sto-Andre-",
    "-Rebouças-", "-Suzano-", "-Sao-Miguel-", "-Ragueb-Chohfi-", "-Santos-Santa-Casa-",
    "-Sao-Vicente-Pres-Wilson-", "-Carapicuiba-", "-Aricanduva-", "-Barueri-Henriqueta-Mendes-",
    "-Salim-f-Maluf-", "-Guaruja-Dom-Pedro-", "-Itapetininga-R-Prudente-de-Moraes-",
    "-Luiz-Gushiken-", "-Aguas-Claras-Castaneiras-", "-Ribeirao-Maurilio-Biagi-",
    "-Itaquera-", "-CURITIBA-", "-Afonso-Vaz-", "-Capitao-Salomao-", "-Sao-Gonçalo-Av-Pres-Kennedy-",
    "-JUNDIAI-", "-ESTRADA-DE-ITAPECERICA-", "-Guaruja-Av-Ademar-Barros-", "-Felipe-Cardoso-",
    "-SALVADOR-AV-OCTAVIO-MANGABEIRA-", "-Brasilia-EPNB-", "-Aracaju-Av-Augusto-Franco-",
    "-Londrina-Saul-Elkind-", "-Maceio-Av-Menino-Marcelo-", "-Praia-Grande-Mal-Mallet-",
    "-SAO-PAULO-AV-ENG-ARMANDO-", "-DUQUE-DE-CAXIAS-RIO-", "-Estrada-Cachamorra-",
    "-MACEIÓ-FERNANDES-LIMA-", "-GUARULHOS-POSTO-SAKAMOTO-", "-CAMPINAS-AV-RUY-RODRIGUEZ-",
    "-João-Pessoa-", "-CANOAS-AV-DR-SEZEFREDO-AZAMBUJA-VIEIRA-1033-", "-RUA-PARAPUÃ-",
    "-IMPERATRIZ-DUQUE-DE-CAXIAS-", "-Brasilia-Noroeste-"
]

# Diretório de saída para o arquivo XML
pasta_saida = "C:/Users/Vinicius L/Downloads/teste"

# Nome do arquivo
nome_arquivo = "Filtro"

# Substituir números e nomes
xmls_substituidos = substituir_numeros_e_nomes(xml_modelo, numeros, nomes)

# Salvar XMLs em um único arquivo
salvar_xmls(xmls_substituidos, pasta_saida, nome_arquivo)
