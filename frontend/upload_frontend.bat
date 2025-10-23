@echo off
echo Subiendo FRONTEND a shanghai-front...
echo.

echo 1. Verificando estado del repositorio frontend...
git status
echo.

echo 2. Agregando todos los archivos del frontend...
git add .
echo.

echo 3. Haciendo commit del frontend...
git commit -m "Frontend React - Shanghai project"
echo.

echo 4. Subiendo al repositorio shanghai-front...
git push -u origin main
echo.

echo ¡Frontend subido correctamente!
echo Tu frontend React está disponible en: https://github.com/iancamps90/shanghai-front
pause
