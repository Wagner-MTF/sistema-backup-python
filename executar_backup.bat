@echo off
title Sistema de Backup Manual - Wagner MTF
cls

echo =======================================================
echo          SISTEMA DE BACKUP POR INTERVALO
echo =======================================================
echo.
echo Diretorio do Projeto: %~dp0
echo.

:: Navega ate a pasta onde o script esta
cd /d "%~dp0"

:: Executa o Python e permite que o usuario interaja com as perguntas
python main.py

echo.
echo =======================================================
echo    Processo Finalizado. Verifique a pasta de Destino.
echo =======================================================
echo.
pause