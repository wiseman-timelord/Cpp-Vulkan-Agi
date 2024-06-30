@echo off
title (Batch Launcher)
cd /d "%~dp0"

:: Display Code
color 80
mode con: cols=65 lines=25

:: Global Variables
set launcher_debug=off

:menu
cls
color 80
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
set /p choice=Select; Options = 1-2, Exit = X: 

if /i "%choice%"=="1" goto run_main_program
if /i "%choice%"=="2" goto run_installer_tool
if /i "%choice%"=="X" goto exit

echo Invalid choice, please try again.
goto menu

:run_main_program
cls
echo.
echo ====================( Launching Program )=======================
echo.
if "%launcher_debug%"=="on" (
    python main_script.py --debug
) else (
    python main_script.py
)
pause
goto menu

:run_installer_tool
cls
echo.
echo ===================( Launching Installer )======================
echo.
if "%launcher_debug%"=="on" (
    python main_install.py --debug
) else (
    python main_install.py
)
goto menu

:exit
exit
