@echo off
chcp 65001 >nul
echo Python virtual muhitini tekshirish...
if not exist venv\Scripts\activate.bat (
    echo Virtual muhit topilmadi, yaratilmoqda...
    python -m venv venv
)
call venv\Scripts\activate.bat
echo Kutubxonalarni o'rnatish...
pip install -r requirements.txt
echo Botni ishga tushirish...
if exist .env (
    echo .env fayli topildi.
) else (
    echo OGOHLANTIRISH: .env fayli topilmadi! .env.example dan nusxalang va BOT_TOKEN ni kiriting.
    copy .env.example .env >nul
)
python bot.py
pause
