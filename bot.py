"""
Telegram bot — doimiy (uzluksiz) ishlaydigan versiya.
run_polling() allaqachon qayta ulanishni qayta urinishi orqali doimiy ishlaydi,
keyinroq quyidagi supervisor loop esa bot xatolik sababli to'xtaganida qayta ishga tushiradi.
"""

import logging
import os
import sys
import time
import signal

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
)

# .env faylidan o'zgaruvchilarni yuklaymiz
load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

# Log sozlamalari
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

# ------ Bot buyruqlar va handlerlar ------

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """/start buyrug'i"""
    user = update.effective_user
    await update.message.reply_text(
        f"Salom, {user.first_name if user else 'dost'}!\n"
        "Men doimiy (uzluksiz) ishlaydigan Telegram botman.\n"
        "Yordam uchun /help yozing."
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """/help buyrug'i"""
    await update.message.reply_text(
        "Mavjud buyruqlar:\n"
        "/start - Botni ishga tushirish\n"
        "/help - Bu yordam xabari\n"
        "/ping - Botning ishlashini tekshirish\n\n"
        "Istagan xabaringizni yuboring, men uni sizga qaytaraman."
    )


async def ping(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """/ping buyrug'i — bot hali ham ishlayotganini tekshirish"""
    await update.message.reply_text("Pong! Men uzluksiz ishlayapman. ✅")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Foydalanuvchi yuborgan matn xabarini qaytarish"""
    text = update.message.text or ""
    await update.message.reply_text(f"Siz yozdingiz: {text}")


async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE):
    """Xatoliklarni qayd etish"""
    logger.error("Xatolik yuz berdi: %s", context.error, exc_info=context.error)


def build_application() -> Application:
    """Bot application-ni qurish"""
    app = (
        Application.builder()
        .token(TOKEN)
        .build()
    )

    # Handlerlar ro'yxati
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("ping", ping))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Xatolik handler
    app.add_error_handler(error_handler)

    return app


def main():
    """Botni ishga tushirish"""
    if not TOKEN:
        logger.error(
            "BOT_TOKEN o'rnatilmagan! Iltimos, .env fayl yarating va BOT_TOKEN ni kiriting."
        )
        sys.exit(1)

    app = build_application()

    logger.info("Bot ishga tushmoqda ... (uzluksiz / doimiy rejim)")

    # run_polling — Telegram API'dan yangilanishlarni doimiy soraydi,
    # tarmoq muammolari yuz berganda avtomatik qayta ulanadi.
    app.run_polling(
        allowed_updates=Update.ALL_TYPES,
        drop_pending_updates=True,
        close_loop=False,
    )


if __name__ == "__main__":
    # Supervisor loop: bot xatolik sababli to'xtaganida 5 sonikdan keyin qayta ishga tushadi.
    # Ctrl+C (KeyboardInterrupt) bosilganda to'xtaydi.
    while True:
        try:
            main()
        except KeyboardInterrupt:
            logger.info("Bot foydalanuvchi tomonidan to'xtatildi.")
            break
        except Exception as exc:  # noqa: BLE001
            logger.exception(
                "Bot to'xtadi, 5 sonikdan keyin qayta ishga tushirilmoqda: %s", exc
            )
            time.sleep(5)
