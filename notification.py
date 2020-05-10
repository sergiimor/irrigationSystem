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
			print "is releStatus is true" + releStatus
		else:
			bot.sendMessage(chat_id, str("Abriendo "))
			GPIO.output(releCtrl, True)
			changeReleState (releStatus)
			print "is not releStatus is true" + releStatus
# Insert your telegram token below
bot = telepot.Bot('1075608346:AAGw8vhREx5WAMmV3aQpclk5yKjYWzn9qiI')
print (bot.getMe())
def relehandler(releStatus):
	releStatus != releStatus
	return releStatus
def changeReleState(releStatus):
	if releStatus == 0:
		releStatus = 1
	else:
		releStatus = 0
	return releStatus

# Start listening to the telegram bot and whenever a message is  received, the handle function will be called.
MessageLoop(bot, handle).run_as_thread()
print ('Listening....')

while 1:
    sleep(10)
