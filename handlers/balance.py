# -*- coding: utf-8 -*-
from aiogram.types import Message

from loader import dp
from sql.sql_commands import getting_balance


@dp.message_handler(commands=['balance'])
async def return_balance(message: Message):
   chat_id = message.from_user.id
   balance = getting_balance(chat_id=chat_id)

   await message.answer(f'Ваш баланс - {balance}')