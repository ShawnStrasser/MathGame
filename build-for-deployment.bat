@echo off
echo Building frontend for deployment...
cd frontend
call npm run build
cd ..
echo Frontend build complete!
echo.
echo Files ready for deployment:
echo - backend/app.py (updated to serve static files)
echo - backend/wsgi.py (WSGI file for PythonAnywhere)
echo - backend/requirements.txt (updated dependencies)
echo - frontend/dist/ (built static files)
echo.
echo Next steps:
echo 1. Upload the backend folder to PythonAnywhere
echo 2. Upload the frontend/dist folder contents to PythonAnywhere
echo 3. Follow the PythonAnywhere deployment instructions
pause 