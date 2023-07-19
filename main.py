import json

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo

bot = Bot('6334709070:AAE03Mabp71A1a7Ljf20S8-BIMSmLkolR58')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markap = types.ReplyKeyboardMarkup()
    markap.add(types.KeyboardButton('Открыть веб страницу', web_app=WebAppInfo(url='https://petya20578.github.io/')))
    await message.answer('Привет мой друг!', reply_markup=markap)


@dp.message_handler(content_types=['web_app_data'])
async def web_app(message: types.Message):
    res = json.loads(message.web_app_data.data)
    await message.answer(f'Имя: {res["name"]}\nEmail: {res["email"]}\nТелефон: {res["phone"]}')


executor.start_polling(dp)
