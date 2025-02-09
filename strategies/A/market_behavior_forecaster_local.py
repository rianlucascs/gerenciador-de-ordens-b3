import requests
import config_model
from os.path import join, dirname, abspath

# Baixar o script do repositório
response = requests.get('https://raw.githubusercontent.com/rianlucascs/predicao-dados-binarios/master/api.py')

# Executar o código do script
exec(response.text, globals())

# Realizar previsão utilizando o script local (com download e importação local)
mb = MarketBehaviorForecasterLocal(
    ticker=config_model.TICKER, 
    features=config_model.FEATURES, 
    start=config_model.START, 
    end=config_model.END, 
    ml_model=config_model.ML_MODEL, 
    p=config_model.P
    ).run_forecast_local()


path = dirname(abspath(__file__))

mb['graphs'](
    mb['df']['df'], 
    'resultado_predicao_acumulado', 
    (15, 5), 
    2, 
    ylabel='resultado_predicao_acumulado', 
    title=f'Resultado Predição Acumulado - {config_model.TICKER}', 
    seta=True
    ).linha().savefig(join(path, "img_resultado_predicao_acumulado"))


mb["graphs"](
    None, 
    None, 
    figsize=(10, 5)).comparar_metricas(mb["metrics"]["model"]).savefig(join(path, "img_comparacao_metricas"))