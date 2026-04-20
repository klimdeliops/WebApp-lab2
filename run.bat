@echo off
cd /d "%~dp0app"
call venv\Scripts\activate.bat
python app.py
pause