import datetime  # Importing the datetime library
import telepot   # Importing the telepot library
from telepot.loop import MessageLoop    # Library function to communicate with telegram bot
import RPi.GPIO as GPIO     # Importing the GPIO library to use the GPIO pins of Raspberry pi
from time import sleep      # Importing the time library to provide the delays in program
import main as pr

releCtrl = 21

#Rele OFF state
releStatus = 0 
now = datetime.datetime.now() # Getting date and time

GPIO.setmode(GPIO.BCM)      # Use Board pin numbering
GPIO.setup(releCtrl, GPIO.OUT) # Declaring the GPIO 21 as output pin
bot = telepot.Bot('1075608346:AAGw8vhREx5WAMmV3aQpclk5yKjYWzn9qiI')

print (bot.getMe())

def handle(msg):
    chat_id = msg['chat']['id'] # Receiving the message from telegram
    command = msg['text']   # Getting text from the message

    print ('Received:')
    print(command)

    # Comparing the incoming message to send a reply according to it
    if command == '/hi':
        bot.sendMessage (chat_id, str("Hi! MakerPro"))
    elif command == '/time':
        bot.sendMessage(chat_id, str("Time: ") + str(now.hour) + str(":") + str(now.minute) + str(":") + str(now.second))
    elif command == '/date':
        bot.sendMessage(chat_id, str("Date: ") + str(now.day) + str("/") + str(now.month) + str("/") + str(now.year))
    elif command == '/temperature':
		sensor_tm=str(pr.Temperatura("Temperatura"))
		a,temperatura=sensor_tm.split(":")
		bot.sendMessage(chat_id, str(a) + str (": ") + str(humitat))
    elif command == '/humitat':
		sensor_hm=str(pr.Humidity("Humitat"))
		a,humitat=sensor_hm.split(":")
	    bot.sendMessage(chat_id, str(a) + str (": ") + str(humitat))
    elif command == '/rele':
		if releStatus == 1:
			bot.sendMessage(chat_id, str("Cerrando "))
			GPIO.output(releCtrl, True)
			changeReleState (releStatus)
			print "is releSatatus is true" + releStatus
		else:
			bot.sendMessage(chat_id, str("Abriendo "))
			GPIO.output(releCtrl, True)
			changeReleState (releStatus)
			print "is not releStatus is true" + releStatus
# Insert your telegram token below

def relehandler(releStatus):
	releStatus != releStatus
	return releStatus
def changeReleState(releStatus):
	if releStatus == 0:
		releStatus = 1
	else:
		releStatus = 0
	return releStatus
	
def start(update, context):
    keyboard = [[InlineKeyboardButton("Option 1", callback_data='1'),
                 InlineKeyboardButton("Option 2", callback_data='2')],

                [InlineKeyboardButton("Option 3", callback_data='3')]]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Please choose:', reply_markup=reply_markup)


def button(update, context):
    query = update.callback_query

    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    query.answer()

    query.edit_message_text(text="Selected option: {}".format(query.data))


def help(update, context):
    update.message.reply_text("Use /start to test this bot.")


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)
# Start listening to the telegram bot and whenever a message is  received, the handle function will be called.
MessageLoop(bot, handle).run_as_thread()
print ('Listening....')

def main():
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("TOKEN", use_context=True)

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    updater.dispatcher.add_handler(CommandHandler('help', help))
    updater.dispatcher.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()


if __name__ == '__main__':
    main()