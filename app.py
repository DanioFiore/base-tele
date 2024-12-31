import telebot
from telebot.types import Message
import os
from dotenv import load_dotenv

load_dotenv()
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# initialize the bot
bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

# handler for command /start
@bot.message_handler(commands=['start'])
def send_welcome(message: Message):
  bot.reply_to(message, "Hello! I'm a Telegram Bot ready to help. 🦾")

# handler for messages
@bot.message_handler(func=lambda message: True)
def echo_all(message: Message):
  bot.reply_to(message, f"You have said: {message.text}")

# start the bot
if __name__ == "__main__":
  print("Bot started!")
  bot.polling()
