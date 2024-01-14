from telebot import types




#  REPLY BUTTON  #

menu_button = types.ReplyKeyboardMarkup(True)
menu_button.row("Отправить анонимное сообщение")

cancel_button = types.ReplyKeyboardMarkup(True)
cancel_button.row("Отменить")