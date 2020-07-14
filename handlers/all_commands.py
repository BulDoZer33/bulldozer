# -*- coding: utf-8 -*-
from aiogram.types import Message

from loader import dp


@dp.message_handler(commands=['commands'])
async def all_commands(message: Message):
   await message.answer('Комманды:\n'
                        '/balance - ваш баланс,\n'
                        '/bets - ставки на технику(неплохой способ зароботка)\n'
                        '/upgrade_bulldozer - улучшение бульдозера')
