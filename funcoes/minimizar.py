# ---------------IMPORTS-----------------
import pyautogui
import time
import telebot
# ---------------BOT-----------------
CHAVE_API = 'YOUR API KEY BOT HERE'

bot = telebot.TeleBot(CHAVE_API)

# ---------------FUNÇÃO-----------------
def minimizar_all(mensagem):
    pyautogui.PAUSE = 0.5
    pyautogui.hotkey('win', 'd')
    bot.send_message(mensagem.chat.id,"All minimized")