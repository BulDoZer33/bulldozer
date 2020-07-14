# -*- coding: utf-8 -*-
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext
from random import randint

from keyboards.inline.bets_transport_keyboard import transport_button
from sql.sql_commands import change_of_balance, getting_balance
from loader import dp
from states.states_for_bets import *


def input_check(func):
   async def check(message: Message, state: FSMContext):
      if len(message.text.split()) != 2:
         await message.answer('Тут точно 2 числа? Попробуй отправить еще раз')
         return

      elif not message.text.split()[0].isdigit() or not message.text.split()[1].isdigit():
         await message.answer('Неуверен что тут все числа. Попробуй отправить еще раз')
         return

      elif int(message.text.split()[0]) < 50:
         await message.answer('Ставка должна быть больше 50.')
         return

      elif int(message.text.split()[1]) < 2 or int(message.text.split()[1]) > 10:
         await message.answer('Ставка должна быть не меньше 2 и не больше 10')
         return

      await func(message, state)
   return check

@dp.message_handler(commands=['bets'])
async def bets(message: Message):
   await message.answer('Правила по комманде: /betting_rules\nВведите [ставку] [колличество техники]\nПример: 250 4')
   await S.amount_of_transport.set()


@dp.message_handler(commands=['betting_rules'], state=S.amount_of_transport)
async def betting_rules(message: Message):
   await message.answer('Ставка - это та сумма которую вы потеряете при поражении или умножите при победе\n\n'
                        'Колличество техники - это то число, которое влияет на процент победы (1/n) и на которе умножится ставка\n\n'
                        'Введите [ставку] [колличество техники]\nПример: 250 4')


@dp.message_handler(content_types=['text'], state=S.amount_of_transport)
@input_check
async def start_bets(message: Message, state: FSMContext):
   mes = message.text.split()

   transport = list(set(['🚌 Автобус', '🚜 Трактор', '🚋 Трамвай', '🚆 Поезд', '🚗 Автомабиль', '🚤 Катер', '🚲 Велосипед', '🚚 Грузовик', '🚁 Вертолет', '🚂 Паровоз']))
   buttons_name = [transport[i] for i in range(int(mes[1]))]

   # Save data
   await state.update_data(bet=int(mes[0]), x=int(mes[1]))

   await message.answer(f'Ставка - {mes[0]}\nВыберите транспорт',  reply_markup=transport_button(buttons_name=buttons_name))
   await S.getting_callback.set()


@dp.callback_query_handler(state=S.getting_callback)
async def handling_callback_win(call: CallbackQuery, state: FSMContext):
   await call.answer(cache_time=6)

   chat_id = call.from_user.id

   data = await state.get_data() # getting data
   bet = data.get('bet') # getting bet
   x = data.get('x') # getting x

   if 'win' in str(call.data):
      change_of_balance(chat_id=chat_id, sum=bet)
      await call.message.answer(text=f'Поздравляю ты выиграл - {bet * x}\nБаланс - {getting_balance(chat_id)}')
   else:
      change_of_balance(chat_id=chat_id, sum=bet*-1)
      await call.message.answer(text=f'К сожалению ты проиграл - {bet}\nБаланс - {getting_balance(chat_id)}')

   await call.message.answer('Введите [ставку] [колличество техники]\nПример: 250 4')
   await S.amount_of_transport.set()
