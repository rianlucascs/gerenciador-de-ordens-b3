import socket
import subprocess
import config_secrets 
from log_config import setup_logging
from time import sleep

logger = setup_logging()

def is_connection_active() -> bool:
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=5)
        return True
    except OSError:
        return False

def wifi_connect() -> None:
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
    Gerencia a reconexão com a internet.
    """
    max_retries = 5  # Número máximo de tentativas
    sleep_time = 60  # Tempo de espera entre as tentativas

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
