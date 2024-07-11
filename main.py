import telebot
import random
from keys import key
import gpt

bot = telebot.TeleBot(key)
message_text = None
user = None


@bot.message_handler(commands=["start"])
def start(message):
    user = message.from_user.first_name
    bot.send_message(message.chat.id, f"Olá {user}! Em que posso ajudar hoje?")


@bot.message_handler(commands=["d20"])
def d20r(message):
    d20 = random.randint(1, 20)
    bot.send_message(message.chat.id, d20)

@bot.message_handler(commands=["renjungatinho"])
def renjun(message):
    bot.send_message(message.chat.id, "Anna renjungatinho minha kpoper favorita hii")

def verify(message):
    global message_text
    user = message.from_user.first_name
    message_text = f'Responda ao {user}.' + message.text

    return True

@bot.message_handler(func=verify)
def send(message):
    texto = '''Escolha uma opção:
 /d20
 /renjungatinho
    '''
    gpt_response = gpt.generate_response(message_text)

    bot.reply_to(message, gpt_response)


bot.polling()
