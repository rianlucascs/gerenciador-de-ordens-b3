#!/bin/bash

# Definir o diretório do repositório
REPO_DIR="C:\Users\xxis4\Desktop\gerenciamento-ordens-b3"

# Verificar se o diretório existe
if [ ! -d "$REPO_DIR" ]; then
    echo "Erro: O diretório '$REPO_DIR' não existe!"
    exit 1
fi

# Navegar até o diretório do repositório
cd "$REPO_DIR" || { echo "Falha ao acessar o diretório!"; exit 1; }

# Verificar se o Git está instalado
if ! command -v git &> /dev/null; then
    echo "Erro: Git não encontrado. Por favor, instale o Git."
    exit 1
fi

# Adicionar alterações
git add .

# Verificar se há alterações antes de fazer o commit
if git diff-index --quiet HEAD --; then
    echo "Nenhuma alteração para commit."
else
    # Comitar as mudanças com uma mensagem de data
    COMMIT_MSG="Commit automático - $(date '+%Y-%m-%d %H:%M:%S')"
    git commit -m "$COMMIT_MSG"
    
    # Verificar se o commit foi bem-sucedido
    if [ $? -eq 0 ]; then
        echo "Commit bem-sucedido com a mensagem: $COMMIT_MSG"
    else
        echo "Erro ao realizar o commit."
        exit 1
    fi
    
    # Push para o repositório remoto
    git push origin master
    
    # Verificar se o push foi bem-sucedido
    if [ $? -eq 0 ]; then
        echo "Push bem-sucedido!"
    else
        echo "Erro ao fazer push para o repositório remoto."
        exit 1
    fi
fi
