@echo off
title Warehouse App Test Runner
setlocal enabledelayedexpansion

echo.
echo  =============================================
echo   WAREHOUSE APP TEST SUITE
echo  =============================================
echo.

python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo   [ERROR] Python is not installed or not in PATH.
    pause
    exit /b 1
)

echo   [INFO]  Ensuring pytest...
pip install --upgrade pytest >nul 2>&1

echo   [INFO]  Starting tests...
echo.
pytest tests -v --tb=short --color=yes
set EXIT_CODE=%errorlevel%

echo.
if %EXIT_CODE% equ 0 (
    echo   [SUCCESS]  All tests passed.
) else (
    echo   [FAILURE]  Some tests failed.
)
echo.
pause