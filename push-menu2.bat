@echo off
cd /d "%~dp0"
del /q push-visa3.bat push-menu.bat 2>nul
git add about.html airport-transfer-how-to-book.html airport-transfer-vehicles.html airport-transfer-why-choose-us.html catalogue.html contact.html cruise-enquiry.html cruises.html expedite-vietnam-evisa.html fix-vietnam-evisa.html index.html noi-bai-airport-fast-track.html plan.html private-car.html services.html style.css tan-son-nhat-airport-fast-track.html tour-enquiry.html tour-guide.html tour-ha-long.html tours.html urgent-vietnam-visa.html vietnam-airport-fast-track.html vietnam-arrival-fast-track.html vietnam-departure-fast-track.html vietnam-domestic-fast-track.html vietnam-evisa-for-chinese-citizens.html vietnam-evisa-special-nationalities.html vietnam-evisa.html vietnam-visa-approval-letter.html vietnam-visa-weekend-holiday.html visa-enquiry.html visa.html 
git commit -m "Vietnam Visa menu: eVisa submenu, rename items"
git push
echo.
echo === Done. Press any key to close ===
pause >nul
(goto) 2>nul & del "%~f0"
