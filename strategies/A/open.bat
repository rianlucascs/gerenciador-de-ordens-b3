
@echo off

REM Verifica se o diretório existe
IF NOT EXIST "c:\Users\xxis4\Desktop\gerenciamento-ordens-b3\strategies\A" (
    echo O diretório c:\Users\xxis4\Desktop\gerenciamento-ordens-b3\strategies\A nao foi encontrado.
    exit /b 1
)

REM Navega para o diretório especificado
cd /d c:\Users\xxis4\Desktop\gerenciamento-ordens-b3\strategies\A

REM Executa o script Python
echo Iniciando estrategia A
echo Executando o script open.py...
python open.py

REM Verifica se a execução foi bem-sucedida
IF %ERRORLEVEL% NEQ 0 (
    echo Ocorreu um erro ao executar o script.
    exit /b %ERRORLEVEL%
)

echo Execucao concluida com sucesso.
