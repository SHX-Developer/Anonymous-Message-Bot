import telebot
import sqlite3

import config





#  LIBRARY VARIABLES  #

bot = telebot.TeleBot(config.token)

db = sqlite3.connect("bot.db", check_same_thread=False)
sql = db.cursor()





#  FUNCTION  #

def function(message):
    pass