from bs4 import BeautifulSoup
import requests
from csv import writer
from datetime import datetime
import time
import pytz

from telegram import update
from telegram.ext import *
import tester as t

keys = '5026688528:AAEL4kIDJ922BuC40X2ggwI9SMBCSuXJsso'


def start_command(update, context):
    update.message.reply_text("""
    Добро пожаловать в программу тестирования
    """)

def help_command(update, context):
    update.message.reply_text("Выберите нужный тест из списка")

def exit_command(update, context):
    quit()
    

def handle_message(update, context):
    text = str(update.message.text).lower()
    response = t.sample_responses(text)
    if (response == '1' or response == '2' or response == '3' or response == '4'):
        t.test(update,response)
    else:
        update.message.reply_text(response)

def error(update, context):
    print(f"Update {update} caused error {context.error}")

def main():
    updater = Updater(keys, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start",start_command))
    dp.add_handler(CommandHandler("help",help_command))
    dp.add_handler(CommandHandler("exit",exit_command))

    dp.add_handler(MessageHandler(Filters.text,handle_message))

    dp.add_error_handler(error)

    updater.start_polling(5)
    updater.idle()

    

main()