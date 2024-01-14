import telebot
import sqlite3
import datetime
import time

import config
import inline_markups
import reply_markups
import forward


#  LIBRARY VARIABLES

db = sqlite3.connect("database.db", check_same_thread=False)
sql = db.cursor()

bot = telebot.TeleBot(config.token)

date_time = datetime.datetime.now().date()




#  CREATING DATABASE

sql.execute('CREATE TABLE IF NOT EXISTS user_access (id INTEGER, username TEXT, firstname TEXT, lastname TEXT, date TIMESTAMP)')
sql.execute('CREATE TABLE IF NOT EXISTS messages (id INTEGER, message TEXT, theme TEXT)')
db.commit()




#  START COMMAND  #

@bot.message_handler(commands = ["start"])
def start(message):

    sql.execute('SELECT id FROM user_access WHERE id = ?', (message.chat.id,))
    user_id = sql.fetchone()

    if user_id == None:

        sql.execute('INSERT INTO user_access (id, username, firstname, lastname, date) VALUES (?, ?, ?, ?, ?)',
        (message.chat.id, message.from_user.username, message.from_user.first_name, message.from_user.last_name, date_time))
        sql.execute('INSERT INTO messages (id, message, theme) VALUES (?, ?, ?)',
        (message.chat.id, "-", "-"))
        db.commit()

        bot.send_message(message.chat.id, "<b> Добро пожаловать ! </b>", parse_mode = "html", reply_markup = reply_markups.menu_button)

    else:

        bot.send_message(message.chat.id, "<b> Главное меню: </b>", parse_mode = "html", reply_markup = reply_markups.menu_button)



#  FORWARD COMMAND  #

@bot.message_handler(commands = ["forward"])
def forward(message):

    if message.chat.id == 284929331:
        forward.forward(message)





#  TEXT  #

@bot.message_handler(content_types = ["text"])
def text(message):

    #  ANONYM MESSAGE

    if message.text == "Отправить анонимное сообщение":
        user_message = bot.send_message(message.chat.id, "Введите ваше сообщение:", parse_mode = "html", reply_markup = reply_markups.cancel_button)
        bot.register_next_step_handler(user_message, save_data)

    #  CANCEL

    elif message.text == "Отменить":
        bot.send_message(message.chat.id, "Главное меню:", reply_markup=reply_markups.menu_button)



#  SAVE ID & MESSAGE

def save_data(message):

    #  CANCEL

    if message.text == "Отменить":

        bot.send_message(message.chat.id, "Отменено !", reply_markup=reply_markups.menu_button)

    else:

        sql.execute('UPDATE messages SET message = ? WHERE id = ?', (message.text, message.chat.id))
        db.commit()

        bot.send_message(message.chat.id, "Выберите тему сообщения:", reply_markup=inline_markups.theme_inline)



#  SEND MESSAGE TO ADMIN

def send_admin(call):

    #  SELECTING DATA

    sql.execute('SELECT * FROM messages WHERE id = ?', (call.message.chat.id,))
    data = sql.fetchone()

    #  BUTTONS

    admin_inline = telebot.types.InlineKeyboardMarkup(row_width=2)
    confirm = telebot.types.InlineKeyboardButton(text="✅", callback_data=f"confirm_{data[0]}")
    decline = telebot.types.InlineKeyboardButton(text="❌", callback_data=f"decline_{data[0]}")
    admin_inline.add(confirm, decline)

    #  SEND ADMIN

    bot.send_message(284929331, f"Новое сообщение от пользователя:  {data[0]}\n\nТема:  #{data[2]}\n\nСообщение:  {data[1]}", parse_mode="html", reply_markup=admin_inline)


#  CALLBACK

@bot.callback_query_handler(func = lambda call: True)
def callback(call):

    if call.data == "tmc":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, "Ваше сообщение отправлено на проверку администраторам, ожидайте уведомления !", reply_markup=reply_markups.menu_button)

        sql.execute('UPDATE messages SET theme = ? WHERE id = ?', ("tmc", call.message.chat.id))
        db.commit()
        send_admin(call)

    elif call.data == "news":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, "Ваше сообщение отправлено на проверку администраторам, ожидайте уведомления !", reply_markup=reply_markups.menu_button)

        sql.execute('UPDATE messages SET theme = ? WHERE id = ?', ("news", call.message.chat.id))
        db.commit()
        send_admin(call)
    
    elif call.data == "opinion":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, "Ваше сообщение отправлено на проверку администраторам, ожидайте уведомления !", reply_markup=reply_markups.menu_button)

        sql.execute('UPDATE messages SET theme = ? WHERE id = ?', ("opinion", call.message.chat.id))
        db.commit()
        send_admin(call)
    
    elif call.data == "advise":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, "Ваше сообщение отправлено на проверку администраторам, ожидайте уведомления !", reply_markup=reply_markups.menu_button)

        sql.execute('UPDATE messages SET theme = ? WHERE id = ?', ("advise", call.message.chat.id))
        db.commit()
        send_admin(call)
    
    elif call.data == "complaint":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, "Ваше сообщение отправлено на проверку администраторам, ожидайте уведомления !", reply_markup=reply_markups.menu_button)

        sql.execute('UPDATE messages SET theme = ? WHERE id = ?', ("complaint", call.message.chat.id))
        db.commit()
        send_admin(call)
    
    elif call.data == "meme":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, "Ваше сообщение отправлено на проверку администраторам, ожидайте уведомления !", reply_markup=reply_markups.menu_button)

        sql.execute('UPDATE messages SET theme = ? WHERE id = ?', ("meme", call.message.chat.id))
        db.commit()
        send_admin(call)
    
    elif call.data == "exam":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, "Ваше сообщение отправлено на проверку администраторам, ожидайте уведомления !", reply_markup=reply_markups.menu_button)

        sql.execute('UPDATE messages SET theme = ? WHERE id = ?', ("exam", call.message.chat.id))
        db.commit()
        send_admin(call)
    
    elif call.data == "portal":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, "Ваше сообщение отправлено на проверку администраторам, ожидайте уведомления !", reply_markup=reply_markups.menu_button)

        sql.execute('UPDATE messages SET theme = ? WHERE id = ?', ("portal", call.message.chat.id))
        db.commit()
        send_admin(call)
    
    elif call.data == "turnitin":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, "Ваше сообщение отправлено на проверку администраторам, ожидайте уведомления !", reply_markup=reply_markups.menu_button)

        sql.execute('UPDATE messages SET theme = ? WHERE id = ?', ("turnitin", call.message.chat.id))
        db.commit()
        send_admin(call)






#  ADMIN CHOOSE

    #  CONFIRM

    elif call.data.startswith("confirm_"):
        user_id = call.data.split("_")[1]
        bot.delete_message(call.message.chat.id, call.message.message_id)

        #  SELECT USER MESSAGE

        sql.execute('SELECT * FROM messages WHERE id = ?', (user_id,))
        data = sql.fetchone()
        message = data[1]
        theme = data[2]

        #  SEND TO CHANNEL

        bot.send_message('@qiutg21p908', f'#{theme}\n\n"{message}"')

        #  SEND MESSAGES TO USERS

        bot.send_message(284929331, f"✅  Сообщение отправлено на канал !")
        bot.send_message(user_id, f"✅  Ваше сообщение отправлено на канал !")

        #  UPDATE DATA

        sql.execute('UPDATE messages SET message = ? WHERE id = ?', ("-", user_id))
        sql.execute('UPDATE messages SET theme = ? WHERE id = ?', ("-", user_id))
        db.commit()
        


    #  DECLINE

    elif call.data.startswith("decline_"):
        user_id = call.data.split("_")[1]
        bot.delete_message(call.message.chat.id, call.message.message_id)

        #  SEND MESSAGES TO USERS

        bot.send_message(284929331, f"❌  Сообщение отменено !")
        bot.send_message(user_id, f"❌  Ваше сообщение было отменено !")

        #  UPDATE DATA

        sql.execute('UPDATE messages SET message = ? WHERE id = ?', ("-", user_id))
        sql.execute('UPDATE messages SET theme = ? WHERE id = ?', ("-", user_id))
        db.commit()














    #  EDIT INLINE TEXT

    if call.data == "edit_inline":
        bot.edit_message_text(call.message.chat.id, call.message.message_id, text = "<b> ТЕКСТ </b>", parse_mode = "html", reply_markup = None)

    #  EDIT INLINE PHOTO

    if call.data == "edit_photo":
        with open("photo/photo.jpg", "rb") as photo:
            bot.edit_message_media( media = telebot.types.InputMedia(
                                    type = 'photo',
                                    media = photo,
                                    chat_id = call.message.chat.id,
                                    message_id = call.message.message_id,
                                    caption = "ТЕКСТ",
                                    parse_mode ="html"),
                                    reply_markup = None)

    #  DELETE INLINE  #

    if call.data == "delete_inline":
        bot.delete_message(call.message.chat.id, call.message.message_id)





#  LAUNCH THE BOT  #

if __name__=='__main__':

    while True:

        try:

            bot.polling(non_stop=True, interval=0)

        except Exception as e:

            print(e)
            
            time.sleep(5)
            
            continue