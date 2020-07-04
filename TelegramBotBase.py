import telebot

f = open("token.txt", "r")
lines = f.readlines()
token = lines[0].strip()

bot = telebot.TeleBot(str(token))

@bot.message_handler(commands=['Hello'])
def StartCamera(message):
    SetCameraValue(True)

@bot.message_handler(func=lambda message: True)
def EchoAll(message):
    bot.reply_to(message, "I onlny react on \"Hello\" ;) ")

bot.polling()
