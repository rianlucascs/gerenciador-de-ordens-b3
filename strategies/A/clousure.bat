
@echo off

REM Verifica se o diretório especificado existe
IF NOT EXIST "C:\Users\xxis4\Desktop\gerenciamento-ordens-b3\strategies\A" (
    echo O diretório C:\Users\xxis4\Desktop\gerenciamento-ordens-b3\strategies\A nao foi encontrado.
    exit /b 1
)

REM Navega para o diretório especificado
cd /d C:\Users\xxis4\Desktop\gerenciamento-ordens-b3\strategies\A

REM Executa o script Python
echo Iniciando a estratégia: A
echo Executando o script clousure.py...
python clousure.py

REM Verifica se a execução foi bem-sucedida
IF %ERRORLEVEL% NEQ 0 (
    echo Ocorreu um erro ao executar o script.
    exit /b %ERRORLEVEL%
)

echo Execução concluída com sucesso.
