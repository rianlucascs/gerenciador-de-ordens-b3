<img src="https://dougwils.com/wp-content/uploads/2024/12/Octogif.gif" style="width: 600px; height: 250px; object-fit: cover;">

<!-- <img src="https://i.gifer.com/EGU.gif" style="width: 600px; height: 250px; object-fit: cover;"> -->

# GERENCIAMENTO DE ORDENS B3

![Python 3.10](https://img.shields.io/badge/Python-3.10-blue?logo=python&logoColor=white&color=3776ab&style=flat-square) ![MetaTrader 5](https://www.icmcapital.com/assets/images/mt5-logo-mob.png)

Este projeto tem como objetivo automatizar o envio de ordens com base nas estratégias desenvolvidas no repositório predicao-dados-binarios, aplicando-as na conta `DMO` do `MetaTrader5`. Além disso, ele verifica em tempo real se os resultados obtidos na execução das estratégias coincidem com os resultados do backtest.

## Como usar

1. Clone o repositório:
    ```bash
    git clone https://github.com/rianlucascs/gerenciador-de-ordens-b3

2. Navegue até o diretório do projeto:
    ```bash
    cd b3-scraping-project

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt

4. Criação do arquivo de execução principal:
    - Abra o Bloco de Notas ou seu editor de texto favorito.
    - Copie e cole o seguinte código no arquivo de texto:
    ```bash
    @echo off
    REM Defina o caminho do projeto
    set PROJECT_DIR=C:\Caminho\Para\Seu\Diretorio\gerenciamento-ordens-b3

    REM Mude para o diretório do projeto
    cd /d "%PROJECT_DIR%"

    REM Execute o script Python
    python main.py
    ```
    - Substitua o caminho do diretório (C:\Caminho\Para\Seu\Diretorio\gerenciamento-ordens-b3) pela pasta onde o seu projeto está localizado no seu computador.
    - Salve o arquivo com a extensão `.bat`. Exemplo: `run.bat`.

5. Agende a execução do script para ser executado diariamente
    
    - Copie e cole essa instrução no `CMD`
    - Substitua o caminho do diretório (C:\Caminho\Para\Seu\Diretorio\GERENCIAMENTO-ORDENS-B3\run.bat)

    **Atualização**
    ```bash
    schtasks /create /tn "TAREFA UPDATE AM" /tr "C:\Caminho\Para\Seu\Diretorio\GERENCIAMENTO-ORDENS-B3\run.bat" /sc daily /st 08:30
    ```

    **Abertura**
    ```bash
    schtasks /create /tn "TAREFA OPEN AM" /tr "C:\Caminho\Para\Seu\Diretorio\GERENCIAMENTO-ORDENS-B3\run.bat" /sc daily /st 08:50
    ```

    **Fechamento**
    ```bash
    schtasks /create /tn "TAREFA CLOSE PM" /tr "C:\Caminho\Para\Seu\Diretorio\GERENCIAMENTO-ORDENS-B3\run.bat" /sc daily /st 16:35
    ```

    **Finalização**
    ```bash
    schtasks /create /tn "TAREFA CLOSURE PM" /tr "C:\Caminho\Para\Seu\Diretorio\GERENCIAMENTO-ORDENS-B3\run.bat" /sc daily /st 17:30
    ``` 