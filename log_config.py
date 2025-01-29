import logging
from logging.handlers import RotatingFileHandler

def setup_logging():
    # Criando o logger
    logger = logging.getLogger(__name__)

    # Configuração básica do log (para o console)
    logging.basicConfig(
        level=logging.DEBUG,  # Define o nível mínimo de log (pode ser DEBUG, INFO, WARNING, ERROR, CRITICAL)
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # Formato da saída
        handlers=[
            logging.StreamHandler()  # Exibe no console
        ]
    )

    # Configuração de log com rotação (escreve em arquivo com rotação)
    handler = RotatingFileHandler('logs.log', maxBytes=10**6, backupCount=3, encoding='utf-8')  # 1MB por arquivo, 3 arquivos de backup
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    # Adicionando o handler de rotação ao logger
    logger.addHandler(handler)

    return logger
