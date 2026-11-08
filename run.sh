#!/usr/bin/env bash
set -e

echo "=== Telegram Bot (uzluksiz / doimiy) ==="

# Virtual muhit
if [ ! -d ".venv" ]; then
    echo "Virtual muhit yaratilmoqda..."
    python3 -m venv .venv
fi

# Aktivlashtirish
# shellcheck source=/dev/null
source .venv/bin/activate

# Kutubxonalarni o'rnatish
echo "Kutubxonalarni o'rnatish..."
pip install -r requirements.txt

# .env fayli
if [ ! -f ".env" ]; then
    echo "OGOHLANTIRISH: .env fayli topilmadi, .env.example dan nusxalandi."
    cp .env.example .env
fi

echo "Botni ishga tushirish..."
python bot.py
