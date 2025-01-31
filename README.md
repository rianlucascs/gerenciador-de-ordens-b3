![coin-flip-24](https://i.gifer.com/EGU.gif)

# GERENCIAMENTO DE ORDENS B3

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

4. Criação do arquivo .bat dentro da pasta GERENCIAMENTO-ORDENS-B3:
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
    ```bash
    # É necessário editar o PATH para o arquivo run.bat que está na pasta GERENCIAMENTO-ORDENS-B3

    schtasks /create /tn "A1_UPDATE" /tr "X:\Caminho\Para\GERENCIAMENTO-ORDENS-B3\run.bat" /sc daily /st 08:30






