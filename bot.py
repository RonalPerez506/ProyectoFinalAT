from telegram.ext import Updater, Filters, CommandHandler, MessageHandler
import cv2
from tensorflow.keras.applications.resnet50 import ResNet50
import numpy as np
from labels import lbl

TOKEN = "5107764356:AAG_OM9tR9tucWPCehs6Wlw5ouYh-znS4eU"

model = ResNet50()

def start(updater, context): 
	updater.message.reply_text("Bienvenido, envía tu imagen!")

def help_(updater, context): 
	updater.message.reply_text("Solo imagenes para clasificar.")

def message(updater, context):
	msg = updater.message.text
	print(msg)
	updater.message.reply_text(msg)

def image(updater, context):
	photo = updater.message.photo[-1].get_file()
	photo.download("img.jpg")

	img = cv2.imread("img.jpg")

	img = cv2.resize(img, (224,224))
	img = np.reshape(img, (1,224,224,3))

	pred = np.argmax(model.predict(img))

	pred = lbl[pred]

	print(pred)

	updater.message.reply_text(pred)





updater = Updater(TOKEN)
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("help", help_))

dispatcher.add_handler(MessageHandler(Filters.text, message))

dispatcher.add_handler(MessageHandler(Filters.photo, image))


updater.start_polling()
updater.idle()