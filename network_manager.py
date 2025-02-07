from socket import create_connection
import subprocess
import config_secrets 
from log_config import setup_logging
from time import sleep

logger = setup_logging()

def is_connection_active() -> bool:
    """
    Verifica se há uma conexão ativa com a Internet.

    Esta função tenta criar uma conexão de socket com o servidor DNS público do Google (8.8.8.8) na porta 53,
    que é a porta padrão para consultas DNS. Se a conexão for bem-sucedida dentro do tempo limite de 5 segundos, 
    a função retorna `True`, indicando que há uma conexão ativa com a Internet. Caso contrário, retorna `False`.

    :return: `True` se a conexão com a Internet estiver ativa, `False` caso contrário.
    """
    try:
        create_connection(("8.8.8.8", 53), timeout=5)
        return True
    except OSError:
        return False

def wifi_connect() -> None:
    """
    Conecta o computador à rede Wi-Fi especificada no arquivo de configuração.

    Esta função executa o comando `netsh wlan connect` no sistema Windows para estabelecer a conexão 
    com a rede Wi-Fi definida em `config_secrets.NETWORK_NAME`.

    Certifique-se de que o nome da rede no arquivo `config_secrets` esteja correto e que o computador 
    tenha permissão para executar o comando no ambiente.
    """
    subprocess.run(f'netsh wlan connect name="{config_secrets.NETWORK_NAME}"', 
                            shell=True)
    return None

def attempt_connection(max_retries=10, sleep_time=60):
    """
    Tenta conectar à internet até o número máximo de tentativas.
    
    :param max_retries: Número máximo de tentativas de conexão (default: 10)
    :param sleep_time: Tempo de espera entre as tentativas (default: 60 segundos)
    :return: True se a conexão for bem-sucedida, False caso contrário
    """
    for attempt in range(1, max_retries + 1):
        logger.info(f"Tentativa {attempt}/{max_retries} de conectar à internet...")

        if is_connection_active():
            logger.info("Internet conectada com sucesso.")
            return True  
        
        logger.error("Falha na conexão com a internet.")
        
        if attempt < max_retries:
            logger.info(f"Tentando reconectar em {sleep_time} segundos...")
            wifi_connect()  
            sleep(sleep_time)  
        else:
            logger.error("Número máximo de tentativas alcançado. Verifique sua conexão.")
            return False  # Falhou após o número máximo de tentativas

def network_manager() -> None:
    """
    Gerencia o processo de reconexão com a Internet.

    Esta função coordena o processo de tentativa de reconexão à Internet, 
    chamando a função `attempt_connection` e gerenciando as tentativas de 
    conexão até o número máximo configurado. Ela também registra o sucesso ou 
    falha de cada tentativa, e, em caso de erro inesperado, loga a exceção.

    O número máximo de tentativas e o tempo de espera entre elas são configurados 
    dentro da função. Se a conexão for bem-sucedida, uma mensagem de sucesso é registrada, 
    caso contrário, é registrado um erro informando a falha. Em caso de erro não tratado, 
    a exceção é capturada e registrada.
    """
    max_retries = 3  # Número máximo de tentativas
    sleep_time = 30  # Tempo de espera entre as tentativas

    try:
        # Tenta conectar à internet
        success = attempt_connection(max_retries, sleep_time)

        if success:
            logger.info("A conexão com a internet foi estabelecida com sucesso.")
        else:
            logger.error("Falha ao estabelecer conexão com a internet.")
    except Exception as e:
        logger.exception(f"Ocorreu um erro inesperado: {e}")

    return None


