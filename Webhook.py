import logging
from aiogram import Bot, Dispatcher, types, executor
import os
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher.webhook import SendMessage
from aiogram.utils.executor import start_webhook
from dotenv import load_dotenv
load_dotenv()
API_TOKEN = os.getenv('BOT_TOKEN')

# настройки вебхука
WEBHOOK_HOST = 'https://69fa-185-19-176-184.eu.ngrok.io'
WEBHOOK_PATH = ''
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

# настройки веб сервера
WEBAPP_HOST = '127.0.0.1' # или ip, 'localhost'
WEBAPP_PORT = 8000

logging.basicConfig(level = logging.DEBUG)

bot = Bot(token=API_TOKEN)
#Диспетчер
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

async def on_startup(dp: Dispatcher):
   await bot.set_webhook(WEBHOOK_URL)


async def on_shutdown(dp:Dispatcher):
   logging.warning('Shutting down..')
   await bot.delete_webhook()
   logging.warning('Bye!')


#/start
@dp.message_handler(commands=['start'])
async def echo(message: types.Message):
   return SendMessage(message.chat.id, message.text)

@dp.message_handler(commands=['help'])
async def echo(message: types.Message):
   return SendMessage(message.chat.id, 'Вы обратились к справке бота')



if __name__ == '__main__':
   start_webhook(
       dispatcher=dp,
       webhook_path=WEBHOOK_PATH,
       on_startup=on_startup,
       on_shutdown=on_shutdown,
       skip_updates=True,
       host=WEBAPP_HOST,
       port=WEBAPP_PORT,
   )

