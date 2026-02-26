@echo off
echo Iniciando atualizacao do Portfolio...
git add .
git commit -m "Automacao: Atualizacao do Projeto Hospitalar 03 %date% %time%"
git push origin main
echo.
echo Tudo certo! Seu projeto ja esta no GitHub.
pause