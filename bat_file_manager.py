from os import startfile, remove
from os.path import exists, join, dirname, abspath
import subprocess

class BatFileManager:

    def __init__(self, strategie : str, file : str):
        
        if "." in file:
            raise ValueError("")
        self.file = file
        self.strategie = strategie
        self.path = join(dirname(abspath(__file__)), "strategies", strategie)
        self.bat_file_path = join(self.path, f"{file}.bat")

    def create_bat_file(self) -> None:
        if not exists(self.bat_file_path):
            with open(self.bat_file_path, 'w', encoding="utf-8") as f:
                content = f"""
@echo off

REM Verifica se o diretório existe
IF NOT EXIST "{self.path}" (
    echo O diretório {self.path} nao foi encontrado.
    exit /b 1
)

REM Navega para o diretório especificado
cd /d {self.path}

REM Executa o script Python
echo Iniciando estrategia {self.strategie}
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
            
            # Verifica se o arquivo existe antes de tentar abrir
            if not exists(self.bat_file_path):
                print(f"Erro: O arquivo {self.file}.bat não foi encontrado no diretório {self.path}.")
                return

            # Executa o arquivo .bat em uma nova janela do CMD
            print(f"Iniciando a execução do script {self.file}.bat...")
            subprocess.Popen(
                ["cmd.exe", "/c", self.bat_file_path],
                creationflags=subprocess.CREATE_NEW_CONSOLE 
            )

            print("Execução iniciada com sucesso!")

        except Exception as e:
            print(f"Erro ao executar o script: {e}")

    def run(self) -> None:
        self.create_bat_file()
        self.execute_bat_file()

  
         




