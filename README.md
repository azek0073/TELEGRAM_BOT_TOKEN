# Telegram Bot — Doimiy (uzluksiz) ishlaydigan versiya

Ushbu bot **python-telegram-bot** kutubxonasidan foydalanib yozilgan va **doimiy (uzluksiz)** ishlaydi:

- `run_polling()` Telegram API'dan yangilanishlarni doimiy soraydi.
- Tarmoq muammo yoki xatolik yuz berganda avtomatik qayta ulanadi / qayta ishga tushadi.
- `while True` supervisori bot to'xtaganidan so'ng 5 sonikdan keyin qayta ishga tushiradi.

## O'rnatish (Windows)

1. Repo'ni clone qiling:

```bash
git clone https://github.com/azek0073/TELEGRAM_BOT_TOKEN.git
cd TELEGRAM_BOT_TOKEN
```

2. `.env.example` nusxasini oling va tokenni kiriting:

```bash
copy .env.example .env
```

`.env` ichida `BOT_TOKEN=123456:ABC-DEF...` ni @BotFather dan olgan tokeningiz bilan almashtiring.

3. Botni ishga tushiring:

```bash
run.bat
```

Yoki quyidagini bajaring:

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python bot.py
```

## O'rnatish (Linux / macOS)

```bash
git clone https://github.com/azek0073/TELEGRAM_BOT_TOKEN.git
cd TELEGRAM_BOT_TOKEN
cp .env.example .env
# .env ichiga BOT_TOKEN ni yozing
chmod +x run.sh
./run.sh
```

## Bot tokenini olish

1. Telegram'da [@BotFather](https://t.me/botfather) ga murojaat qiling.
2. `/newbuy` buyrug'i yuboring yoki `/newbot` orqali bot yarating.
3. Olgan `BOT_TOKEN` ni `.env` fayliga yozing.

## Bot buyruqlari

| Buyruq | Ma'nos |
|--------|--------|
| `/start` | Botni ishga tushirish |
| `/help` | Yordam xabari |
| `/ping` | Bot ishlayotganini tekshirish |
| (matn xabar) | Yuborgan xabaringizni qaytaradi |

## Doimiy ishlashni ta'minlash (serverda)

Agar serverda doimiy (fon) rejimda turmoqchi bo'lsangiz, `systemd` yoki `screen`/`tmux` dan foydalaning.

**systemd misoli (`/etc/systemd/system/telegrambot.service`):**

```ini
[Unit]
Description=Telegram Bot (doimiy)
After=network.target

[Service]
Type=simple
User=youruser
WorkingDirectory=/path/to/TELEGRAM_BOT_TOKEN
EnvironmentFile=/path/to/TELEGRAM_BOT_TOKEN/.env
ExecStart=/path/to/TELEGRAM_BOT_TOKEN/.venv/bin/python bot.py
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
```

So'ng:

```bash
sudo systemctl daemon-reload
sudo systemctl enable --now telegrambot
```

## Kutubxonalar

- `python-telegram-bot==21.4`
- `python-dotenv==1.0.1`

Barcha bog'liqliklar `requirements.txt` da ko'rsatilgan.

## Xavfsizlik

- `.env` faylini hech kimga bermang va git'ga qo'shming (`.gitignore`da allaqachon chiqarilgan).
- Tokenni kod ichida to'g'ridan-to'g'ri yozmang.
