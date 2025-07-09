import random
import os
from dotenv import load_dotenv  # 🆕 добавили dotenv

from telegram import Update, ReplyKeyboardRemove
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# 📥 Загружаем переменные из .env
load_dotenv()

# ✅ Получаем токен из переменной окружения
TOKEN = os.getenv("TOKEN")

# Цифры в синем кружке (emoji)
DICE_NUMS = {
    1: "1️⃣",
    2: "2️⃣",
    3: "3️⃣",
    4: "4️⃣",
    5: "5️⃣",
    6: "6️⃣"
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎯 Напиши /roll чтобы бросить 2 кости!",
        reply_markup=ReplyKeyboardRemove()
    )

async def roll(update: Update, context: ContextTypes.DEFAULT_TYPE):
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    total = d1 + d2

    text = (
        f"🎯 *Кидаем кости!*\n\n"
        f"🟢 Первая: {DICE_NUMS[d1]}\n"
        f"🔵 Вторая: {DICE_NUMS[d2]}\n\n"
        f"🎉 *Результат: {total}* 🎉"
    )
    await update.message.reply_text(text, parse_mode="Markdown")

# 🔄 Запуск
if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("roll", roll))
    print("✅ Бот запущен.")
    app.run_polling()
