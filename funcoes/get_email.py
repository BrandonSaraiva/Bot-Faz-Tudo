# ---------------IMPORTS-----------------
import pyautogui
import time
import telebot
#--------------------------BOT--------------------------------
CHAVE_API = 'YOUR API KEY BOT HERE'

bot = telebot.TeleBot(CHAVE_API)
#--------------------------FUNÇÃO--------------------------------

def print_mail(mensagem):
    pyautogui.PAUSE = 0.5
    pyautogui.press('win')
    time.sleep(1)
    pyautogui.write('opera')
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.moveTo(211, 85)
    pyautogui.click()
    pyautogui.click()
    time.sleep(6)
    bot.send_message(mensagem.chat.id, f'Abrindo email...')
    pyautogui.hotkey('win', 'shift', 's')
    time.sleep(1)
    pyautogui.moveTo(299, 273)
    pyautogui.mouseDown()
    pyautogui.moveTo(1783, 465)
    time.sleep(1)
    bot.send_message(mensagem.chat.id, f'Tirando print...')
    pyautogui.mouseUp()
    pyautogui.moveTo(399, 49)
    pyautogui.click()
    pyautogui.write('HTTP DO SEU CHAT DO TELEGRAM OU WTS AQUI')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(6)
    bot.send_message(mensagem.chat.id, f'Carregando foto...')
    pyautogui.moveTo(911, 1037)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)
    pyautogui.moveTo(891, 727)
    time.sleep(1)
    pyautogui.write('Ultimos 5 emails de sua caixa😘')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.hotkey('alt', 'f4')


