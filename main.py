import os
import telebot
from telebot import types
import threading
from flask import Flask

TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

VIDEOS = {
    "fan_video": "8821827837:AAF8PpB1Dn6SMJV1"
}

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Button 1", callback_data="btn1"))
    markup.add(types.InlineKeyboardButton("Button 2", callback_data="btn2"))
    bot.send_message(message.chat.id, "👋 Welcome", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    bot.answer_callback_query(call.id, "Clicked!")

# --- Render Free ke liye Web Server ---
app = Flask(__name__)
@app.route('/')
def home():
    return "Bot is Running!"

def run_web():
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

threading.Thread(target=run_web).start()

# Bot start
bot.infinity_polling()
