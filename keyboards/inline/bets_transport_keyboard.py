# -*- coding: utf-8 -*-
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from random import randint


def transport_button(buttons_name):
   r = randint(0, len(buttons_name))
   buttons = []
   for i in range(len(buttons_name)):
      if i == r:
         i = buttons_name[i]
         buttons.append([InlineKeyboardButton(text=i, callback_data=i + ' win')])
      else:
         i = buttons_name[i]
         buttons.append([InlineKeyboardButton(text=i, callback_data=i)])

   keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)

   return keyboard