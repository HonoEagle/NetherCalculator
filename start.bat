@echo off
setlocal
cd /d "%~dp0"

where pyw >nul 2>&1
if %errorlevel%==0 (
    start "" pyw nether-calc.py
    goto :end
)

where pythonw >nul 2>&1
if %errorlevel%==0 (
    start "" pythonw nether-calc.py
    goto :end
)

where py >nul 2>&1
if %errorlevel%==0 (
    py nether-calc.py
    goto :end
)

where python >nul 2>&1
if %errorlevel%==0 (
    python nether-calc.py
    goto :end
)

echo Python n'est pas installe ou n'est pas dans le PATH.
echo Installe Python 3 puis reessaie.
pause

:end
endlocal
