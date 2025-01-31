#!/bin/bash
# Commit automático diário, por exemplo

git add .
git commit -m "Commit automático - $(date)"
git push origin main
