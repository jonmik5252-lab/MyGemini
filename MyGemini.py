import telebot
from google import genai
from google.genai import types
import textwrap as txt

client = genai.Client(api_key = 'AQ.Ab8RN6Jwzne-nv7J9WRIXr921M8I93bC6O2D-nLfTXPaBQ--bA')


token = "7958532901:AAHtrppHHmZJEAgbT272lHYNl2bCeZRYUkE"

bot = telebot.TeleBot(token)

@bot.message_handler(commands = ['start'])
def start(mes):
    bot.send_message(mes.chat.id, 'Привет, чем могу помочь?')

@bot.message_handler(content_types = ["text"])
def ai(message):
    start_text = message.text
    response = client.models.generate_content( model='gemini-3.1-flash-lite', contents = start_text)
    f = response.text
    bot.send_message(message.chat.id, f)


print('бот запущен')

bot.polling(none_stop = True)

