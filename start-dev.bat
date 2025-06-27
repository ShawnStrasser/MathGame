@echo off
echo ========================================
echo    Math Game Development Servers
echo ========================================
echo.

echo Starting Flask Backend Server...
echo Backend will be available at: http://localhost:5000
echo.
start "Flask Backend" cmd /k "cd backend && python app.py"

echo Waiting 5 seconds for backend to start...
timeout /t 5 /nobreak > nul

echo.
echo Starting Vue.js Frontend Server...
echo Frontend will be available at: http://localhost:5173
echo.
start "Vue Frontend" cmd /k "cd frontend && npm run dev"

echo.
echo ========================================
echo Both servers are starting up!
echo.
echo Backend:  http://localhost:5000
echo Frontend: http://localhost:5173
echo.
echo The servers are running in separate windows.
echo Close those windows to stop the servers.
echo ========================================
echo.
pause 