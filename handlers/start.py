# -*- coding: utf-8  -*-
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from sql.sql_commands import user_add_for_db

@dp.message_handler(CommandStart())
async def start(message: types.Message):
   await message.answer(f'Привет, {message.from_user.full_name}.\nЭто бот в котором ты можешь купить и прокачать свой собственный бульдозер и соревноваться его мощьностями с другими игроками\nВсе комманды: /commands')
   user_add_for_db(chat_id=message.from_user.id)
