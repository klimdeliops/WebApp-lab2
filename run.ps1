# run.ps1
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location "$scriptDir"

Write-Host "Активация виртуального окружения..." -ForegroundColor Green
& .\venv\Scripts\Activate.ps1

Write-Host "Запуск приложения..." -ForegroundColor Green
python app.py