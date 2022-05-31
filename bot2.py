import schedule
import telebot

API_TOKEN='5107764356:AAG_OM9tR9tucWPCehs6Wlw5ouYh-znS4eU'
//recibe api token para el metodo telebot
bot = telebot.TeleBot(API_TOKEN)
@bot.message_handler(commands=["help", "start"])

def enviar(message):
	bot.reply_to(message, "Hola, soy un bot!")

bot.polling() 
