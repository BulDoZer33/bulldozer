from aiogram.dispatcher.filters.state import State, StatesGroup


class S(StatesGroup):
   amount_of_transport = State()
   getting_callback = State()