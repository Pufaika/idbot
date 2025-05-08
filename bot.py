from aiogram import Bot, Dispatcher, executor, types
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")  # 🔧 Set this in Railway variables

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# This handler returns the chat ID of any group where the bot receives a message
@dp.message_handler()
async def get_chat_id(message: types.Message):
    await message.reply(f"🔎 Group Chat ID: {message.chat.id}")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
