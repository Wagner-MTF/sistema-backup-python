TASKKILL /F /IM HUB_Server.exe
TASKKILL /F /IM HUB_Sort.exe
TASKKILL /F /IM HUB_Remove.exe
TASKKILL /F /IM HUB_Upload.exe
TASKKILL /F /IM HUB_Send.exe
@echo OFF
timeout /T 3 /NOBREAK
@echo ON
sc start ONRAD_Hub_Server
@echo OFF
timeout /T 3 /NOBREAK
@echo ON
sc start ONRAD_Hub_Sort
@echo OFF
timeout /T 3 /NOBREAK
@echo ON
sc start ONRAD_Hub_Send
@echo OFF
timeout /T 3 /NOBREAK
@echo ON
sc start ONRAD_Hub_Upload
@echo OFF
timeout /T 3 /NOBREAK
@echo ON
sc start ONRAD_Hub_Remove
