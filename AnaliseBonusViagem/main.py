import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "xxxx"
# Your Auth Token from twilio.com/console
auth_token = "xxxx"
client = Client(account_sid, auth_token)

# Passo a passo de solução

# Abrir os 6 arquivos em Excel de forma dinamica(f'{valor que eu quero})
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mês de {mes} alguém bateu a meta. Vendedor {vendedor}, Vendas {vendas}')
        message = client.messages.create(
            to="+xxx",
            from_="+17606153872",
            body=f'No mês de {mes} alguém bateu a meta. Vendedor {vendedor}, Vendas {vendas}')
        print(message.sid)

# Para cada arquivo:

# Verificar se algum valor na coluna Vendas daquele arquivo é maior que 55.000:

# Se for maior do que 55.000 -> Envia um SMS com o Nome, o mês e as vendas do vendedor:

# Caso não seja maior do que 55.000 não quero fazer nada
