import requests

# Baixar o script do repositório
response = requests.get('https://raw.githubusercontent.com/rianlucascs/predicao-dados-binarios/master/api.py')

# Executar o código do script
exec(response.text, globals())

# Realizar previsão utilizando o script local (com download e importação local)
mb = MarketBehaviorForecasterLocal(ticker='BBDC4.SA', features=[3], start='2012-05-11', end='2022-05-11', step_size=None,
                                    ml_model="train_decision_tree", p=1).run_forecast_local()

print(mb["df"]["df"])

# Gerar gráfico
# mb['graphs'](mb['df']['df'], 'resultado_predicao_acumulado', (15, 5), 2, 
#              ylabel='resultado_predicao_acumulado', title='BBDC4', seta=True).linha()
