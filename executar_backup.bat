@echo off
title Sistema de Automacao de Backup - Wagner MTF
echo Iniciando o processo de backup...
echo ---------------------------------------

:: Navega ate a pasta do projeto
cd /d "C:\Projetos\AutomacaoBackup"

:: Executa o script Python
python main.py

echo ---------------------------------------
echo Processo concluido! Verifique os logs.
pause