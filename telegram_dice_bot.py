import os
import random
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardRemove
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

# Эмодзи для кубиков
DICE_NUMS = {
    1: "1️⃣",
    2: "2️⃣",
    3: "3️⃣",
    4: "4️⃣",
    5: "5️⃣",
    6: "6️⃣"
}

# Новый способ — через DefaultBotProperties!
bot = Bot(
    token=TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN)
)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        "🎯 Напиши /roll чтобы бросить 2 кости!",
        reply_markup=ReplyKeyboardRemove()
    )

@dp.message(Command("roll"))
async def cmd_roll(message: types.Message):
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    total = d1 + d2

    text = (
        f"🎲 *Кидаем кости!*\n\n"
        f"🟢 Первая: {DICE_NUMS[d1]}\n"
        f"🔵 Вторая: {DICE_NUMS[d2]}\n\n"
        f"🎉 *Результат: {total}* 🎉"
    )
    await message.answer(text, reply_markup=ReplyKeyboardRemove())

if __name__ == "__main__":
    import asyncio
    asyncio.run(dp.start_polling(bot))
