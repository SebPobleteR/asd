import os
import telegram
from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler

def process_message(update, context):
    text=update.message.text
    if str(text).__contains__('#channel') == None:
        context.bot.send_message(
            chat_id='YOUR_CHANNEL_ID',
            text=str(text).replace('#channel', '')
        )
        
if __name__ == '__main__':
    updater = Updater(token=os.environ['TOKEN'], use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(filters=Filters.text, callback=process_message))
    updater.start_polling()
    print('Bot is polling')
    updater.idle()
