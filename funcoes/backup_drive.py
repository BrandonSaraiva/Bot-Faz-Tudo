#------------------------------IMPORTS------------------------------
import pyautogui
import time
import telebot
# ---------------BOT TELEGRAM-----------------
CHAVE_API = 'YOUR API KEY BOT HERE'

bot = telebot.TeleBot(CHAVE_API)
# ---------------FUNÇÃO-----------------
def drive_backup(mensagem):
    drive = 'YOUR HTTP PATH FOLDER TO BACKUP HERE'

    pyautogui.PAUSE = 0.5
    pyautogui.press('win')
    time.sleep(1)
    pyautogui.write('opera')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.write(drive)
    time.sleep(3)
    pyautogui.press('enter')
    pyautogui.hotkey('winleft','d')
    pyautogui.moveTo(1802,44)
    pyautogui.mouseDown()
    pyautogui.moveTo(1050,682)
    pyautogui.hotkey('alt','tab')
    time.sleep(3)
    pyautogui.mouseUp()
    pyautogui.moveTo(1104, 698)
    time.sleep(2)
    pyautogui.click()
    bot.send_message(mensagem.chat.id,f'Arquivo subido com sucesso, link: {drive}')
    pyautogui.moveTo(1753, 12)
    pyautogui.click()