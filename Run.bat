@echo off
title Warehouse App Checker
setlocal enabledelayedexpansion

set "PKGS=PyQt5 openpyxl pytest"

set "MISSING="
for %%P in (%PKGS%) do (
    python -c "import %%P" 2>nul
    if !errorlevel! neq 0 (
        set "MISSING=!MISSING! %%P"
    )
)

if not "!MISSING!"=="" (
    echo ========================================
    echo  Modules missing:
    echo !MISSING!
    echo.
    echo  Use:
    echo  pip install!MISSING!
    echo ========================================
    pause
    exit /b 1
)

echo All modules installed! Launching programm...
python main.py