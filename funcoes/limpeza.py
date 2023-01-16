# ---------------IMPORTS-----------------
import pyautogui
import time
import telebot
# ---------------BOT TELEGRAM-----------------
CHAVE_API = 'YOUR API KEY BOT HERE'

bot = telebot.TeleBot(CHAVE_API)
# ---------------FUNÇÃO-----------------

def fechar_all(mensagem):
    pyautogui.press('f')
    pyautogui.PAUSE = 0.5
    pyautogui.moveTo(1890, 242)
    pyautogui.rightClick()
    time.sleep(1)
    pyautogui.moveTo(1709, 699)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(1002, 590)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(1034, 155)
    pyautogui.click()
    bot.send_message(mensagem.chat.id, "Tudo limpo 😅")