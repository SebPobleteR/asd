import os
import telegram
from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler

def handle_start(update, context):

    update.message.reply_text(
        text=(
            'This bot has been migrated to a new one: @ForwarderGeniusBot.'
            '\nGo there and run /start to continue'
        ),
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Go to the bot', url='https://t.me/ForwarderGeniusBot')]
        ])
    )



def process_message(update, context):

    text = update.message.text

    if str(text).__contains__('#channel'):
        context.bot.send_message(
            chat_id='YOUR_CHANNEL_ID',
            text=str(text).replace('#channel', '')
        )


if __name__ == '__main__':

    updater = Updater(token=os.environ['TOKEN'], use_context=True)
    bot = telegram.Bot(token=token)

    dp = updater.dispatcher
    dp.add_handler(MessageHandler(filters=Filters.text, callback=process_message))
    updater.start_polling()

    print('Bot is polling')
    
    print(f'running at @{bot.username}')

    updater.idle()
