
@echo off

REM Verifica se o diretório existe
IF NOT EXIST "c:\Users\xxis4\Desktop\gerenciamento-ordens-b3\strategies\B" (
    echo O diretório c:\Users\xxis4\Desktop\gerenciamento-ordens-b3\strategies\B nao foi encontrado.
    exit /b 1
)

REM Navega para o diretório especificado
cd /d c:\Users\xxis4\Desktop\gerenciamento-ordens-b3\strategies\B

REM Executa o script Python
echo Iniciando estrategia B
echo Executando o script open.py...
python open.py

REM Verifica se a execução foi bem-sucedida
IF %ERRORLEVEL% NEQ 0 (
    echo Ocorreu um erro ao executar o script.
    exit /b %ERRORLEVEL%
)

echo Execucao concluida com sucesso.
