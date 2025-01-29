from os.path import exists, join, dirname, abspath
import subprocess
from log_config import setup_logging

class BatFileManager:

    def __init__(self, strategie : str, file : str):
        """
        Inicializa a instância da classe BatFileManager com os dados fornecidos.

        Esta classe gerencia a criação e execução de arquivos .bat que automatizam a execução
        de scripts Python específicos em diretórios de estratégia definidos. O arquivo .bat gerado
        verifica se o diretório da estratégia existe, navega até o diretório e executa o script Python
        correspondente. Caso o arquivo .bat não exista, ele será criado.

        Attributes:
            file (str): Nome do arquivo .bat (sem a extensão). Este arquivo executará o script Python.
            strategie (str): Nome da estratégia, usado para determinar o diretório onde o script Python será executado.
            path (str): Caminho completo do diretório onde o arquivo .bat e o script Python estarão localizados.
            bat_file_path (str): Caminho completo do arquivo .bat que será criado e executado.

        Methods:
            ``create_bat_file() -> None``:
                Cria o arquivo .bat, caso ainda não exista, contendo os comandos necessários para a execução do script Python.

            ``_generate_bat_content() -> str``:
                Gera o conteúdo do arquivo .bat com os comandos específicos para verificar o diretório e executar o script.

            ``execute_bat_file() -> None``:
                Executa o arquivo .bat em uma nova janela do CMD, iniciando a execução do script Python.

            ``run() -> None``:
                Cria o arquivo .bat e executa-o em sequência, iniciando o processo completo.
        """
        if "." in file:
            raise ValueError(f"O nome do arquivo não pode conter pontos ('.'). O arquivo fornecido: {file}")
        self.file = file
        self.strategie = strategie
        self.path = join(dirname(abspath(__file__)), "strategies", strategie)
        self.bat_file_path = join(self.path, f"{file}.bat")

        self.logger = setup_logging()


    def create_bat_file(self) -> None:
        """
        Cria o arquivo .bat caso ele não exista.

        Este método verifica se o arquivo .bat já foi criado. Caso contrário, ele gera o conteúdo do arquivo 
        .bat e o grava no diretório especificado. O arquivo .bat contém os comandos para verificar se o diretório 
        da estratégia existe, navegar até ele e executar o script Python.

        Raises:
            OSError: Se ocorrer um erro ao tentar criar ou escrever no arquivo .bat.
        """
        if not exists(self.bat_file_path):
            try:
                with open(self.bat_file_path, 'w', encoding="utf-8") as f:
                    bat_content  = self._generate_bat_content()
                    f.write(bat_content)
                self.logger.info(f"Arquivo .bat criado com sucesso: {self.bat_file_path}")
            except OSError as e:
                self.logger.error(f"Erro ao criar o arquivo .bat: {e}")
                raise

    def _generate_bat_content(self) -> str:
        """
        Gera o conteúdo do arquivo .bat.

        Este método gera o conteúdo que será escrito no arquivo .bat, incluindo os comandos para:
        - Verificar se o diretório da estratégia existe.
        - Navegar até o diretório da estratégia.
        - Executar o script Python correspondente.
        - Verificar se a execução foi bem-sucedida.

        Returns:
            str: O conteúdo completo do arquivo .bat com os comandos necessários.
        """
        return f"""
@echo off

REM Verifica se o diretório especificado existe
IF NOT EXIST "{self.path}" (
    echo O diretório {self.path} nao foi encontrado.
    exit /b 1
)

REM Navega para o diretório especificado
cd /d {self.path}

REM Executa o script Python
echo Iniciando a estratégia: {self.strategie}
echo Executando o script {self.file}.py...
python {self.file}.py

REM Verifica se a execução foi bem-sucedida
IF %ERRORLEVEL% NEQ 0 (
    echo Ocorreu um erro ao executar o script.
    exit /b %ERRORLEVEL%
)

echo Execução concluída com sucesso.
"""
    
    def execute_bat_file(self) -> None:
        """
        Executa o arquivo .bat em uma nova janela do CMD.

        Este método verifica se o arquivo .bat existe no caminho especificado e, caso exista, 
        executa o arquivo .bat em uma nova janela de terminal (CMD), iniciando a execução do script Python.

        Raises:
            Exception: Se ocorrer um erro ao tentar executar o arquivo .bat ou se o arquivo não for encontrado.
        """
        try:
            if not exists(self.bat_file_path):
                self.logger.error(f"Erro: O arquivo {self.file}.bat não foi encontrado no diretório {self.path}.")
                return
            self.logger.info(f"Iniciando a execução do script {self.file}.bat da estratégia {self.strategie}.")
            subprocess.Popen(
                ["cmd.exe", "/c", self.bat_file_path],
                creationflags=subprocess.CREATE_NEW_CONSOLE 
            )
            self.logger.info(f"Execução do script {self.file} da estratégia {self.strategie} iniciada com sucesso!")
        except Exception as e:
            self.logger.error(f"Erro ao executar o script {self.file} da estratégia {self.strategie}: {e}")

    def run(self) -> None:
        self.create_bat_file()
        self.execute_bat_file()

if __name__ == "__main__":
    bat_file_manager = BatFileManager("A", "open")
    bat_file_manager.run()




