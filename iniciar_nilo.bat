@echo off
chcp 65001 >nul
cd /d "%~dp0"
where py >nul 2>nul
if %errorlevel% equ 0 (
  py -3 servidor_nilo.py
) else (
  python servidor_nilo.py
)
if errorlevel 1 (
  echo.
  echo Nao foi possivel iniciar Nilo. Confira se Python 3 esta instalado.
  pause
)
