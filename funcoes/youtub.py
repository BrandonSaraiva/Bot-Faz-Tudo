# ---------------IMPORTS-----------------
import pyautogui
import time
import telebot

# ---------------BOT-----------------
CHAVE_API = 'YOUR API KEY BOT HERE'

bot = telebot.TeleBot(CHAVE_API)

# ---------------FUNÇÃO-----------------
def carregar_video(mensagem):
    url = mensagem.text
    pyautogui.PAUSE = 0.5
    pyautogui.press('win')
    time.sleep(1)
    pyautogui.write('opera')
    pyautogui.press('enter')
    time.sleep(4)
    pyautogui.moveTo(588, 52)
    pyautogui.write(url)
    bot.send_message(mensagem.chat.id, f'Abrindo vídeo...')
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(6)
    pyautogui.moveTo(859, 558)
    pyautogui.click()
    pyautogui.press('f')
    time.sleep(2)
    bot.send_message(mensagem.chat.id, f'Vídeo pronto🫡')

