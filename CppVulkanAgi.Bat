@echo off

:: Initialization
title Batch Launcher
cd /d "%~dp0"
color 80
mode con: cols=65 lines=25

:: Check for Python installation
where python >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed or not added to the PATH.
    pause
    exit /b 1
)

:menu
cls
echo.
echo ========================( Batch Launcher )=======================
echo.
echo.
echo.
echo.
echo.
echo.
echo.
echo.
echo                       1. Run Main Program
echo.
echo                      2. Run Installer Tool
echo.
echo.
echo.
echo.
echo.
echo.
echo.
echo.
echo ----------------------------------------------------------------
set /p choice=Select; Launch Options = 1-2, Exit Launcher = X: 

if /i "%choice%"=="1" goto check_main_program
if /i "%choice%"=="2" goto check_main_installer
if /i "%choice%"=="X" goto exit

echo Invalid choice, please try again.
timeout /t 3 /nobreak >nul
goto menu

:check_main_program
if exist main_program.py (
    goto run_program
) else (
    echo.
    echo Error: main_program.py not found.
    timeout /t 3 /nobreak >nul
    goto menu
)

:check_main_installer
if exist main_installer.py (
    goto run_installer
) else (
    echo.
    echo Error: main_installer.py not found.
    timeout /t 3 /nobreak >nul
    goto menu
)

:run_program
cls
echo.
echo ====================( Launching Program )=======================
echo.
timeout /t 2 /nobreak >nul
@echo on
python main_program.py
@echo off
timeout /t 5 /nobreak >nul
color 80
mode con: cols=65 lines=25
goto menu

:run_installer
cls
echo.
echo ===================( Launching Installer )======================
echo.
timeout /t 2 /nobreak >nul
@echo on
python main_installer.py
@echo off
timeout /t 5 /nobreak >nul
color 80
mode con: cols=65 lines=25
goto menu

:exit
exit
