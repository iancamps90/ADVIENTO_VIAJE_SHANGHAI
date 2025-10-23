@echo off
echo Subiendo proyecto a GitHub...
echo.

echo 1. Verificando estado del repositorio...
git status
echo.

echo 2. Agregando todos los archivos...
git add .
echo.

echo 3. Haciendo commit...
git commit -m "Initial commit - Shanghai project"
echo.

echo 4. Subiendo al repositorio shanghai-front...
git push -u origin main
echo.

echo ¡Proceso completado!
echo Tu proyecto ahora está disponible en: https://github.com/iancamps90/shanghai-front
pause
