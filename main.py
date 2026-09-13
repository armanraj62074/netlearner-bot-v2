import os
import telebot
from telebot import types

TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

VIDEOS = {
    "fan_video": "8821827837:AAF8PpBlDn6SMJVl77qj58gGzmdSEuD7Fvc"
}

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("🎬 Demo Video Dekho", callback_data="play_fan"))
    markup.add(types.InlineKeyboardButton("📚 Mere Courses", url="https://t.me/+SmdhmPxglIRmZWVl"))
    bot.send_message(message.chat.id, "👋 Welcome to NetLearner! Apna course choose karo.", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data == "play_fan":
        bot.send_video(call.message.chat.id, VIDEOS["fan_video"])

bot.infinity_polling()
