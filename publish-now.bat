@echo off
cd /d "%~dp0"
if exist "C:\Program Files\nodejs\node.exe" set "PATH=C:\Program Files\nodejs;%PATH%"
if exist "C:\Program Files\Git\cmd\git.exe" set "PATH=C:\Program Files\Git\cmd;%PATH%"
echo ===== GIT ===== > publish-log.txt
git add -A >> publish-log.txt 2>&1
git commit -m "Split Tours menu into Daily Tours and Multi-day Tours with one page per category" >> publish-log.txt 2>&1
git push >> publish-log.txt 2>&1
echo ===== DEPLOY ===== >> publish-log.txt
call npx wrangler deploy >> publish-log.txt 2>&1
echo === PUBLISH FINISHED === >> publish-log.txt
exit
