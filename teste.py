
# Para agendar a tarefa às 9 da manhã:

# schtasks /create /tn "Tarefa das 9 AM" /tr "C:\Caminho\Para\Seu\Programa.exe" /sc daily /st 09:00


# Para agendar a tarefa às 4 da tarde:

# schtasks /create /tn "Tarefa das 4 PM" /tr "C:\Caminho\Para\Seu\Programa.exe" /sc daily /st 16:00

# Explicando cada parte:
# /sc daily: Define que a tarefa será executada diariamente.
# /st HH:mm: Define o horário de execução (9:00 AM para a primeira e 16:00 PM para a segunda).