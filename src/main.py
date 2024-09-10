

import pandas as pd
from utils import padronizar_telefone, formatar_data, separar_endereco

# Caminho para o arquivo Excel de entrada e saída
caminho_arquivo = r"data/dados_pacientes.xlsx"
caminho_saida = r"outputs/dados_pacientes_tratados.xlsx"

def tratar_dados(caminho_arquivo, caminho_saida):
    try:
        df = pd.read_excel(caminho_arquivo, header=0)
        print("Arquivo lido com sucesso!")

        df.columns = df.columns.str.strip()
        print("Colunas disponíveis no DataFrame:")
        print(df.columns)

        # Padronizar telefones
        for coluna_telefone in ['Telefone', 'Celular', 'Telefone Comercial']:
            if coluna_telefone in df.columns:
                df[coluna_telefone] = df[coluna_telefone].apply(padronizar_telefone)
                print(f"Telefones na coluna '{coluna_telefone}' padronizados com sucesso!")
            else:
                print(f"A coluna '{coluna_telefone}' não foi encontrada no DataFrame.")

        # Formatar datas de nascimento
        if 'Data de Nascimento' in df.columns:
            df['Data de Nascimento'] = df['Data de Nascimento'].apply(formatar_data)
            print("Datas de nascimento formatadas com sucesso!")
        else:
            print("A coluna 'Data de Nascimento' não foi encontrada no DataFrame.")

        # Separar endereço
        if 'Endereço' in df.columns:
            df[['Rua', 'Número', 'Complemento']] = df['Endereço'].apply(lambda x: pd.Series(separar_endereco(x)))
            print("Endereços separados com sucesso!")
            df['Endereço'] = df['Rua']  # Atualiza a coluna Endereço com a Rua sem o número
        else:
            print("A coluna 'Endereço' não foi encontrada no DataFrame.")

        # Remover duplicatas
        cols_duplicatas = ['Nome', 'Telefone', 'CPF']
        cols_existentes = [col for col in cols_duplicatas if col in df.columns]
        if cols_existentes:
            df = df.drop_duplicates(subset=cols_existentes, keep='first')
            print("Duplicatas removidas com sucesso!")
        else:
            print("Colunas necessárias para remover duplicatas não foram encontradas no DataFrame:", cols_duplicatas)

        # Limpar e-mails inválidos
        if 'E-mail' in df.columns:
            df['E-mail'] = df['E-mail'].apply(lambda x: x if re.match(r"[^@]+@[^@]+\.[^@]+", str(x)) else '')
            print("Campos com e-mails inválidos limpos com sucesso!")
        else:
            print("A coluna 'E-mail' não foi encontrada no DataFrame.")

        # Salvando o DataFrame tratado
        df.to_excel(caminho_saida, index=False)
        print(f"Dados tratados salvos com sucesso no arquivo: {caminho_saida}")

    except FileNotFoundError:
        print("Arquivo não encontrado. Verifique o caminho e o nome do arquivo.")
    except KeyError as e:
        print(f"Ocorreu um erro de chave: {e}")
    except Exception as e:
        print(f"Ocorreu um erro durante o processamento: {e}")

if __name__ == "__main__":
    tratar_dados(caminho_arquivo, caminho_saida)
