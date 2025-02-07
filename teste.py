import requests

# Baixar o script do repositório
response = requests.get('https://raw.githubusercontent.com/rianlucascs/predicao-dados-binarios/master/api.py')

# Executar o código do script
exec(response.text, globals())

# Realizar previsão utilizando o script local (com download e importação local)
mb = MarketBehaviorForecasterLocal('^BVSP', features=[1, 2], start='2012-05-11', end='2022-05-11', step_size=None).run_forecast_local()

# Gerar gráfico
mb['graphs'](mb['df']['df'], 'Adj Close', (15, 5), 2, ylabel='Adj Close', title='^BVSP', seta=True).linha()


