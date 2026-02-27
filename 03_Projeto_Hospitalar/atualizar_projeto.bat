@echo off
echo Iniciando atualizacao do Portfolio...
git add .
git commit -m "Automacao: Adicao da view VW_PERCENTUAL_VARIACAO_FATURAMENTO no Projeto Hospitalar 03 %date% %time%"
git push origin main
echo.
echo Tudo certo! Seu projeto ja esta no GitHub.
pause