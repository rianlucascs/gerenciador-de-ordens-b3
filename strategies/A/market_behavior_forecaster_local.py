import requests
import config_model
from os.path import join, dirname, abspath

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

html_table = mb["df"]["df"].tail(7).to_html(index=False)
with open(join(path, "table.html"), "w") as file:
    file.write(html_table)
