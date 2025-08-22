import requests
import json
import os


# Função para carregar cookies de um arquivo JSON da pasta 'Cookies'
def carregar_cookies(pasta_cookies, nome_arquivo_cookies):
    caminho_arquivo = os.path.join(pasta_cookies, nome_arquivo_cookies)
    with open(caminho_arquivo, 'r') as file:
        cookies = json.load(file)
    return cookies


# Função para converter os cookies exportados para o formato esperado pelo requests
def converter_cookies(cookies):
    session_cookies = {}
    for cookie in cookies:
        session_cookies[cookie['name']] = cookie['value']
    return session_cookies


# Criar pastas 'Relatorio_Acesso' e 'Cookies' se elas não existirem
pasta_relatorios = 'Relatorio_Acesso'
pasta_cookies = 'Cookies'

if not os.path.exists(pasta_relatorios):
    os.makedirs(pasta_relatorios)

if not os.path.exists(pasta_cookies):
    os.makedirs(pasta_cookies)

# Nome do arquivo de cookies e caminho
nome_arquivo_cookies = 'cookies.json'

# URL base
url_base = 'https://painel.skymail.net.br/ajax/report/login?page=undefined&username=LOGINDOUSUARIO&domain_name=agesbec.com.br&date_from=30&date_upto=1&report_type=access-history&type=csv'


# Lista de usuários
usuarios = [
"adm",
"aduaneiro",
"agb.conta.bkp",
"agendamento",
"agesbec",
"andre.villela",
"apoio.adm",
"apoio.com",
"apoio.fin2",
"apoio.fin",
"apoio.fin2",
"apoiorfb2",
"apoiorfb",
"atendimento2",
"atendimento1",
"atendimento",
"balanca",
"carlos.nakata",
"carregamento",
"ccso",
"charles.silva",
"comercial",
"compras2",
"compras",
"compras2",
"contrato.agb",
"contrato2.agb",
"contrato2.agb",
"controle",
"controleaduaneiro",
"cristina.drago",
"customer.service",
"cv",
"deslacre",
"diretoria.geral",
"diretoria.ti",
"entreposto",
"expedicao1",
"expedicao",
"farrah.koch",
"faturamento1",
"faturamento2",
"faturamento",
"financeiro",
"fpa",
"giovana.gobbo",
"isabelli.franca",
"jaime.urrutia",
"jakeline.sobrinho",
"juridico1",
"juridico",
"luiz.pazine",
"mailing",
"mapa",
"naoresponda1",
"naoresponda2",
"naoresponda",
"nfe.agb",
"operacional1",
"operacional",
"pmo",
"portal",
"presencadecarga2",
"presencadecarga3",
"presencadecarga",
"presidencia",
"qualidade",
"recepcao",
"renato.demarchi",
"rh1",
"rh2",
"rh",
"ri",
"ricardo.drago",
"rt2",
"rt",
"sandro",
"sd",
"seg",
"ti1",
"ti2",
"ti3",
"transporte"
]

# Carregar cookies do arquivo JSON da pasta 'Cookies'
cookies_arquivo = carregar_cookies(pasta_cookies, nome_arquivo_cookies)
cookies_convertidos = converter_cookies(cookies_arquivo)

# Criar uma sessão e configurar os cookies
with requests.Session() as session:
    session.cookies.update(cookies_convertidos)

    for usuario in usuarios:
        try:
            # Substituir 'LOGINDOUSUARIO' pelo nome do usuário
            url = url_base.replace('LOGINDOUSUARIO', usuario)

            # Fazer a requisição com os cookies
            response = session.get(url)
            response.raise_for_status()  # Verifica se houve erro na requisição

            # Definir o caminho e nome do arquivo na pasta 'Relatorio_Acesso'
            nome_arquivo = f'{usuario}.csv'
            caminho_arquivo = os.path.join(pasta_relatorios, nome_arquivo)

            # Salvar o arquivo no diretório específico
            with open(caminho_arquivo, 'wb') as file:
                file.write(response.content)

            print(f"{usuario} baixado com sucesso!")
        except requests.exceptions.RequestException as e:
            print(f"Erro ao baixar {usuario}")







# usuarios = [
# "adm",
# "aduaneiro",
# "agb.conta.bkp",
# "agendamento",
# "agesbec",
# "andre.villela",
# "apoio.adm",
# "apoio.com",
# "apoio.fin2",
# "apoio.fin",
# "apoio.fin2",
# "apoiorfb2",
# "apoiorfb",
# "atendimento1",
# "atendimento",
# "balanca",
# "carlos.nakata",
# "carregamento",
# "ccso",
# "charles.silva",
# "comercial",
# "compras2",
# "compras",
# "compras2",
# "contrato.agb",
# "contrato2.agb",
# "contrato2.agb",
# "controle",
# "controleaduaneiro",
# "cristina.drago",
# "customer.service",
# "cv",
# "deslacre",
# "diretoria.geral",
# "diretoria.ti",
# "entreposto",
# "expedicao1",
# "expedicao",
# "farrah.koch",
# "faturamento1",
# "faturamento2",
# "faturamento",
# "financeiro",
# "fpa",
# "giovana.gobbo",
# "isabelli.franca",
# "jaime.urrutia",
# "jakeline.sobrinho",
# "juridico1",
# "juridico",
# "luiz.pazine",
# "mailing",
# "mapa",
# "naoresponda1",
# "naoresponda2",
# "naoresponda",
# "nfe.agb",
# "operacional1",
# "operacional",
# "pmo",
# "portal",
# "presencadecarga2",
# "presencadecarga3",
# "presencadecarga",
# "presidencia",
# "qualidade",
# "recepcao",
# "renato.demarchi",
# "rh1",
# "rh2",
# "rh",
# "ri",
# "ricardo.drago",
# "rt2",
# "rt",
# "sandro",
# "sd",
# "seg",
# "ti1",
# "ti2",
# "ti3",
# "transporte"
# ]