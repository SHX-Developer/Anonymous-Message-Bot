import telebot
import sqlite3
import datetime

import config

import inline_markups
import reply_markups



#  LIBRARY VARIABLES  #

bot = telebot.TeleBot(config.token)

db = sqlite3.connect("database.db", check_same_thread=False)
sql = db.cursor()

date_time = datetime.datetime.now().date()





#  FORWARD

def forward(message):

    bot.send_message(message.chat.id, "<b> Рассылка началась  ✅ </b>", parse_mode="html")

    sql.execute("SELECT id FROM user_access")
    data = sql.fetchall()

    sql.execute("""SELECT COUNT(id) FROM user_access""")
    all_users = sql.fetchone()[0]

    total = 0

    for users in data:

        try:

            bot.send_message(users[0], "ТЕКСТ",parse_mode="html", reply_markup=reply_markups.menu_button)

            total += 1

            print(f"[{users[0]}]: получил сообщение  ✅")

        except Exception as e:

            print(e)

            print(f"[{users[0]}]: заблокировал бота  ❌")

    else:

        blocked_users = all_users - total

        bot.send_message(message.chat.id, f"<b>✅  Ваше сообщение успешно отправлено:  {total}  пользователям из:  {all_users}   </b>", parse_mode="html", reply_markup=None)
        bot.send_message(message.chat.id, f"<b>❌  Заблокировавшие пользователи:  {blocked_users} </b>", parse_mode="html", reply_markup=None)