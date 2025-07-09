


from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import asyncio
import random
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = "7716257236:AAHUSNHr2YZhydBRjN5AGFovoQVlTTnE_48"

bot = Bot(token=TOKEN)
dp = Dispatcher()

DICE_NUMS = {
    1: "1️⃣",
    2: "2️⃣",
    3: "3️⃣",
    4: "4️⃣",
    5: "5️⃣",
    6: "6️⃣"
}

inline_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🎲 Бросить кости", callback_data="roll")]
])

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Жми кнопку ниже, чтобы бросить кости!", reply_markup=inline_kb)

@dp.callback_query(F.data == "roll")
async def roll_callback(callback: types.CallbackQuery):
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    total = d1 + d2

    if d1 == d2:
        score = (d1 + d2) * 2  # удвоение очков
        text = (
            f"🎯 <b>Кидаем кости!</b>\n\n"
            f"🔥 Выпал <b>КУШ</b>! Дубль: {DICE_NUMS[d1]} + {DICE_NUMS[d2]}\n"
            f"🟢 Очки удваиваются!\n"
            f"🎉 <b>Результат: {score}</b> 🎉"
        )
    else:
        score = total
        text = (
            f"🎯 <b>Кидаем кости!</b>\n\n"
            f"🟢 Первая: {DICE_NUMS[d1]}\n"
            f"🔵 Вторая: {DICE_NUMS[d2]}\n\n"
            f"🎉 <b>Результат: {score}</b> 🎉"
        )
    await callback.message.answer(text, reply_markup=inline_kb, parse_mode="HTML")
    await callback.answer()

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
