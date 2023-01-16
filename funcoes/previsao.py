# ---------------IMPORTS-----------------
import pyautogui
import time
import telebot

# ---------------BOT-----------------
CHAVE_API = 'YOUR API KEY BOT HERE'

bot = telebot.TeleBot(CHAVE_API)

# ---------------FUNÇÃO-----------------
def previsao_tempo(mensagem):
    pyautogui.PAUSE = 0.5
    pyautogui.press('win')
    time.sleep(1)
    pyautogui.write('opera')
    pyautogui.press('enter')
    time.sleep(4)
    pyautogui.moveTo(588, 52)
    pyautogui.write('https://www.climatempo.com.br/previsao-do-tempo/cidade/61/brasilia-df')
    bot.send_message(mensagem.chat.id, f'Abrindo site...')
    time.sleep(6)
    pyautogui.press('enter')
    time.sleep(6)
    pyautogui.moveTo(1289, 428)
    pyautogui.click()
    bot.send_message(mensagem.chat.id, f'Printando o resultado ')
    pyautogui.scroll(-600)
    pyautogui.hotkey('win', 'shift', 's')
    time.sleep(1)
    pyautogui.moveTo(363, 156)
    pyautogui.mouseDown()
    pyautogui.moveTo(1527, 963)
    time.sleep(1)
    pyautogui.mouseUp()
    bot.send_message(mensagem.chat.id, f'Abrindo telegram')
    pyautogui.moveTo(399, 49)
    pyautogui.click()
    pyautogui.write('HTTP DO SEU CHAT DO SEU TELEGRAM AQUI')
    pyautogui.press('enter')
    time.sleep(6)
    bot.send_message(mensagem.chat.id, f'Carregando foto...')
    pyautogui.moveTo(911, 1037)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)
    pyautogui.moveTo(891, 727)
    time.sleep(1)
    pyautogui.write('Previsao para o dia de hoje:')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.hotkey('alt', 'f4')
