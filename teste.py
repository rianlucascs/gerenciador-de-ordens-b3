import socket

def verificar_conexao():
    try:
        # Tenta conectar ao servidor de DNS do Google (8.8.8.8), porta 53 (comum para DNS)
        socket.create_connection(("8.8.8.8", 53), timeout=5)
        return True
    except OSError:
        return False

# Exemplo de uso
if verificar_conexao():
    print("Conectado à internet")
else:
    print("Não há conexão com a internet")
