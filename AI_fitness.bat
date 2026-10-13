@echo off
title AI Fitness Launcher
setlocal

cd /d "%~dp0"

set "PYTHON=%~dp0venv\Scripts\python.exe"

echo =====================================
echo       AI FITNESS LAUNCHER
echo =====================================
echo.

if not exist "%PYTHON%" (
    echo ERROR: Virtual environment not found!
    echo Expected: %PYTHON%
    pause
    exit /b 1
)

echo Starting AI Fitness Backend...
start "AI Fitness Backend" cmd /k ""%PYTHON%" main.py"

timeout /t 3 /nobreak >nul

echo Starting AI Fitness Frontend...
start "AI Fitness Frontend" cmd /k ""%PYTHON%" -m streamlit run app.py --server.port 8501"

timeout /t 5 /nobreak >nul

echo Opening AI Fitness Website...
start "" "http://localhost:8501"

echo.
echo Backend and frontend launch commands executed.
echo Keep both server windows open while using the website.
pause