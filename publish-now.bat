@echo off
cd /d "%~dp0"
if exist "C:\Program Files\nodejs\node.exe" set "PATH=C:\Program Files\nodejs;%PATH%"
if exist "C:\Program Files\Git\cmd\git.exe" set "PATH=C:\Program Files\Git\cmd;%PATH%"
echo ===== GIT ===== > publish-log.txt
git add -A >> publish-log.txt 2>&1
git commit -m "Add Cao Bang section, Hanoi-Ha Long-Sapa 5D4N tour and contact-only North Vietnam combo tours" >> publish-log.txt 2>&1
git push >> publish-log.txt 2>&1
echo ===== DEPLOY ===== >> publish-log.txt
call npx --yes wrangler deploy >> publish-log.txt 2>&1
echo === PUBLISH FINISHED === >> publish-log.txt
exit
