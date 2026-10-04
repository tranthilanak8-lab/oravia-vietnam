@echo off
cd /d "%~dp0"
if exist "C:\Program Files\nodejs\node.exe" set "PATH=C:\Program Files\nodejs;%PATH%"
echo ============================================== > deploy-log.txt
echo  Deploying oravia-vietnam to Cloudflare >> deploy-log.txt
echo ============================================== >> deploy-log.txt
call npx wrangler deploy >> deploy-log.txt 2>&1
echo. >> deploy-log.txt
echo === DEPLOY SCRIPT FINISHED === >> deploy-log.txt
exit
