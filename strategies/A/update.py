import requests
import config_model
from os.path import join, dirname, abspath
from datetime import date
import json

# Baixar o script do repositório
response = requests.get("https://raw.githubusercontent.com/rianlucascs/predicao-dados-binarios/master/api.py")

# Executar o código do script
exec(response.text, globals())

# Realizar previsão utilizando o script local (com download e importação local)
mb = MarketBehaviorForecasterLocal(
    ticker=config_model.TICKER, 
    features=config_model.FEATURES, 
    start=config_model.START, 
    end=config_model.END, 
    ml_model=config_model.ML_MODEL, 
    p=config_model.P,
    contracts=config_model.CONTRACTS
    ).run_forecast_local()


path = dirname(abspath(__file__))

# Dados do arquivo que contem a informação da previsão
dias_da_semana = ["segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira", "sábado", "domingo"]
data = {
    "Data da atualização" : [str(date.today()), dias_da_semana[date.today().weekday()]],
    "Última data do preço " : [str(mb["df"]["df"].index[-1])[:10], dias_da_semana[mb["df"]["df"].index[-1].weekday()]],
    "Alvo binário": mb["df"]["df"]["alvo_binario"][-1],
    "Predição": mb["df"]["df"]["predicao"][-1]
}

# Salvando a informação da previsão
with open(join(path, "forecast.json"), "w", encoding="utf-8") as arquivo:
    json.dump(data, arquivo, indent=4, ensure_ascii=False)

# Salvando a informação da previsão no histórico 
with open(join(path, "previsoes", f"forecast_{date.today()}.json"), "w", encoding="utf-8") as arquivo:
    json.dump(data, arquivo, indent=4, ensure_ascii=False)

# Salvando tabela
mb["df"]["df"].tail(20).to_excel(join(path, 'table.xlsx'), index=False)

mb["graphs"](
    mb["df"]["df"], 
    "resultado_predicao_acumulado", 
    (15, 5), 
    2, 
    ylabel="resultado_predicao_acumulado", 
    title=f"Resultado Predição Acumulado - {config_model.TICKER}", 
    seta=True
    ).linha().savefig(join(path, "img_resultado_predicao_acumulado"))

mb["graphs"](
    None, 
    None, 
    figsize=(10, 5)).comparar_metricas(mb["metrics"]["model"]).savefig(join(path, "img_comparacao_metricas"))

mb["graphs"](
    mb["df"]["df"], 
    "resultado_predicao_acumulado", 
    (15, 5), 
    1, 
    ylabel="Retorno Anual (Reais)", 
    title="Train, Test and After Test"
    ).barplot().savefig(join(path, "img_retorno_anual"))

mb["graphs"](
    mb["df"]["train"][["predicao"]],
    "predicao", 
    (3, 3), 
    xlabel='', 
    title=f"Distribuição - Sinais - Predição (Train)",
    fontsize_title=10, 
    tick_params_labelsize=2).pio().savefig(join(path, "img_distribuicao_sinais_predicao_treino"))

mb["graphs"](
    mb["df"]["test"][["predicao"]],
    "predicao", 
    (3, 3), 
    xlabel='', 
    title=f"Distribuição - Sinais - Predição (Test)",
    fontsize_title=10, 
    tick_params_labelsize=2).pio().savefig(join(path, "img_distribuicao_sinais_predicao_teste"))

mb["graphs"](
    mb["df"]["after_test"][["predicao"]],
    "predicao", 
    (3, 3), 
    xlabel='', 
    title=f"Distribuição - Sinais - Predição (After Test)",
    fontsize_title=10, 
    tick_params_labelsize=2).pio().savefig(join(path, "img_distribuicao_sinais_predicao_apos_o_teste"))


