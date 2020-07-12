from aiogram.types import Message

from loader import dp


@dp.message_handler(commands=['commands'])
async def all_commands(message: Message):
   await message.reply()
