from os import startfile, remove
from os.path import exists, join, dirname, abspath
import subprocess
import shlex

class BatFileManager:

    def __init__(self, strategie : str, file : str):
        
        if "." in file:
            raise ValueError("")
        self.file = file
        self.path = join(dirname(abspath(__file__)), "strategies", strategie)

    def create_bat_file(self) -> None:
        if not exists(join(self.path, f"{self.file}.bat")):
            with open(join(self.path, f"{self.file}.bat"), 'w', encoding="utf-8") as f:
                content = f"""@echo off
REM Verifica se o diretório existe
IF NOT EXIST "{self.path}" (
    echo O diretório {self.path} nao foi encontrado.
    exit /b 1
)

REM Navega para o diretório especificado
cd /d {self.path}

REM Executa o script Python
echo Executando o script {self.file}.py...
python {self.file}.py

REM Verifica se a execução foi bem-sucedida
IF %ERRORLEVEL% NEQ 0 (
    echo Ocorreu um erro ao executar o script.
    exit /b %ERRORLEVEL%
)

echo Execucao concluida com sucesso.
"""
                f.write(content)
    
    def execute_bat_file(self) -> None:
        try:
            bat_file_path = join(self.path, f"{self.file}.bat")
            
            # Verifica se o arquivo existe antes de tentar abrir
            if not exists(bat_file_path):
                print(f"Erro: O arquivo {self.file}.bat não foi encontrado no diretório {self.path}.")
                return

            # Executa o arquivo .bat em uma nova janela do CMD
            print(f"Iniciando a execução do script {self.file}.bat...")
            subprocess.Popen(
                ["cmd.exe", "/c", bat_file_path],
                creationflags=subprocess.CREATE_NEW_CONSOLE  # Abre uma nova janela do terminal
            )

            print("Execução iniciada com sucesso!")

        except Exception as e:
            print(f"Erro ao executar o script: {e}")

BatFileManager("A", "open").execute_bat_file()
BatFileManager("B", "open").execute_bat_file()       
         




