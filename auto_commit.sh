#!/bin/bash
# Commit automático diário, por exemplo

cd C:\Users\xxis4\Desktop\gerenciamento-ordens-b3

git add .
git commit -m "Commit automático - $(date)"
git push origin main
