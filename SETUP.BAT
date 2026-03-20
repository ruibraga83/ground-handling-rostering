---

### **For Windows (`setup.bat`):**

```batch
@echo off
REM Initialize git
git init
git config user.email "admin@rostering.local"
git config user.name "Admin User"

REM Create directories
mkdir backend\services\auth-service\src
mkdir backend\services\flight-service\src
mkdir backend\services\staff-service\src
mkdir backend\services\roster-service\src
mkdir backend\services\task-service\src
mkdir frontend\src
mkdir optimization-engine\src
mkdir docs
mkdir .github\workflows

REM Create files
(
echo # Ground Handling Rostering System
echo.
echo A production-ready SaaS platform.
) > README.md

(
echo node_modules/
echo __pycache__/
echo .env
echo dist/
) > .gitignore

(
echo PROPRIETARY LICENSE
) > LICENSE

(
echo version: '3.8'
echo services:
echo   postgres:
echo     image: postgres:15-alpine
echo     ports:
echo       - "5432:5432"
) > backend\docker-compose.yml

(
echo {"name": "auth-service"}
) > backend\services\auth-service\package.json

REM Git commands
git add .
git commit -m "Initial commit: Ground Handling Rostering System"
git branch -M main
git remote add origin https://github.com/ruibraga83/ground-handling-rostering.git
git push -u origin main

echo ✅ All files created and pushed to GitHub!
pause