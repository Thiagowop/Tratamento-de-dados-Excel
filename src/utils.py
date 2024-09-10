import pandas as pd
import re

# Função para padronizar números de telefone
def padronizar_telefone(telefone):
    telefone = re.sub(r'\D', '', str(telefone))  # Remove caracteres não numéricos
    if len(telefone) == 8:  # Se o telefone tiver 8 dígitos, adiciona o "9" e o DDD 31
        telefone = '319' + telefone
    elif len(telefone) == 9:  # Se tiver 9 dígitos, adiciona o DDD 31
        telefone = '31' + telefone
    elif len(telefone) == 10:  # Se tiver 10 dígitos, adiciona o "9" e o DDD 31
        telefone = '319' + telefone[2:]
    elif len(telefone) == 11:  # Telefones que já estão com o DDD (11 dígitos)
        if telefone.startswith('31'):  # Verifica se o DDD é "31"
            telefone = telefone  # Mantém o telefone existente
        else:
            telefone = '31' + telefone[2:]  # Adiciona o DDD 31
    else:
        telefone = ''  # Retorna vazio para qualquer formato inesperado
    return telefone

# Função para formatar a data de nascimento
def formatar_data(data):
    try:
        return pd.to_datetime(data).strftime('%Y-%m-%d')  # Formata como YYYY-MM-DD
    except:
        return ''

# Função para separar endereço em Rua, Número e Complemento
def separar_endereco(endereco):
    endereco = str(endereco).strip()  # Certifica que o endereço é tratado como string e sem espaços no início/fim
    padrao_numero = r'\d{1,5}[-/]?\d{0,5}'  # Expressão regular para capturar números (considerando possíveis traços e barras)
    meses = [
        'janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho',
        'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'
    ]
    contem_mes = any(mes in endereco.lower() for mes in meses)  # Verifica se o nome da rua contém um nome de mês
    numeros = re.findall(padrao_numero, endereco)  # Captura o número usando a regex
    if contem_mes and len(numeros) > 1:
        rua = re.sub(padrao_numero, '', endereco, count=1).strip()
        numero = numeros[1]
    else:
        rua = re.sub(padrao_numero, '', endereco).strip()
        numero = numeros[0] if numeros else ''
    rua = rua.title()  # Convertendo o nome da rua para "Title Case"
    complemento = ''
    if numero:
        pos_numero = endereco.find(numero) + len(numero)
        complemento = endereco[pos_numero:].strip()
        complemento = re.sub(r'^[^\w\s]+', '', complemento)  # Remove caracteres especiais no início
    if 'apt' in complemento.lower():
        complemento = complemento.replace('Apt', '').strip()
    return rua, numero, complemento
