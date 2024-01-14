from telebot import types




#  INLINE BUTTON

theme_inline = types.InlineKeyboardMarkup()
theme_inline.row(types.InlineKeyboardButton(text="TMC", callback_data="tmc"),
                 types.InlineKeyboardButton(text="News", callback_data="news"),
                 types.InlineKeyboardButton(text="Opinion", callback_data="opinion"))
theme_inline.row(types.InlineKeyboardButton(text="Advise", callback_data="advise"),
                 types.InlineKeyboardButton(text="Complaint", callback_data="complaint"),
                 types.InlineKeyboardButton(text="Meme", callback_data="meme"))
theme_inline.row(types.InlineKeyboardButton(text="Exam", callback_data="exam"),
                 types.InlineKeyboardButton(text="Portal", callback_data="portal"),
                 types.InlineKeyboardButton(text="Turnitin", callback_data="turnitin"))





