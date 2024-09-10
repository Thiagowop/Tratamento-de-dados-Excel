# Tratamento-de-dados-Excel

Este é um script Python que lê um arquivo Excel, trata os dados e salva as informações em novas planilhas.

O script realiza as seguintes ações:

Lê um arquivo Excel (dados_pacientes.xlsx) e armazena os dados em um DataFrame do pandas.
Trata os dados, incluindo:
Padronização de números de telefone
Separação de endereços em rua, número e complemento
Formatação de datas de nascimento
Remoção de duplicatas
Validação de e-mails
Salva as informações tratadas em um novo arquivo Excel (dados_pacientes_tratados.xlsx).
Cria planilhas separadas com informações específicas (nomes, celulares, endereços, e-mails) e salva-as em arquivos separados.
O script também inclui tratamento de erros para lidar com possíveis problemas durante a execução.

paciente_data_cleaning/
├── data/
│   ├── dados_pacientes.xlsx  # Dados de exemplo (não deve conter dados reais)
├── src/
│   ├── main.py               # Script principal que utiliza as funções de tratamento
│   ├── utils.py              # Arquivo de funções utilitárias (padronização, separação, etc.)
├── outputs/
│   ├── ...                   # Planilhas geradas após o tratamento de dados
├── README.md                 # Documentação do projeto
├── requirements.txt          # Dependências do Python
└── .gitignore                # Arquivo para ignorar arquivos/diretórios específicos
