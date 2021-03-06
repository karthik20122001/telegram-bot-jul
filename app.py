from Adafruit_IO import Client 
from telegram.ext import Updater, MessageHandler,Filters
import os

api_key = os.getenv('api_key')
aio = Client('B_KARTHIK',api_key)

def demo1(bot,update):
  chat_id = bot.message.chat_id
  path = 'https://image.shutterstock.com/image-vector/ok-hand-lettering-handmade-calligraphy-260nw-669965602.jpg'
  bot.message.reply_text('I am fine')
  update.bot.sendPhoto(chat_id=chat_id,photo=path)

def demo2(bot,update):
  bot.message.reply_text("My name is arrow's_bot")

def lightOn(bot,update):
  chat_id = bot.message.chat_id
  aio.send('light', 1)
  path = 'https://i.kinja-img.com/gawker-media/image/upload/c_fit,f_auto,g_center,pg_1,q_60,w_1600/wtzdfjeynfmmypoqsauy.jpg'
  update.bot.sendPhoto(chat_id=chat_id,photo=path)
  bot.message.reply_text("light is turned on")

def lightOff(bot,update):
  chat_id = bot.message.chat_id
  aio.send('light', 0)
  path = 'https://images.unsplash.com/photo-1546622519-4a467d28f75f?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1500&q=80'
  update.bot.sendPhoto(chat_id=chat_id,photo=path)
  bot.message.reply_text("light is turned off")

def fanOn(bot,update):
  chat_id = bot.message.chat_id
  aio.send('fan', 1)
  path = 'https://www.thespruce.com/thmb/tyVxBz0q2ToJOLZCGKUHj6vwId0=/1883x1412/smart/filters:no_upscale()/GettyImages-182436453-5c79e51cc9e77c0001e98e6c.jpg'
  update.bot.sendPhoto(chat_id=chat_id,photo=path)
  bot.message.reply_text("fan is turned on")

def fanOff(bot,update):
  chat_id = bot.message.chat_id
  aio.send('fan', 0)
  path = 'https://www.lifesavvy.com/p/uploads/2019/06/37df4c5d.jpg?height=200p&trim=2,2,2,2'
  update.bot.sendPhoto(chat_id=chat_id,photo=path)
  bot.message.reply_text("fan is turned off")

def main(bot,update):
  a = bot.message.text.lower()
  print(a)

  if a == "how are you?":
    demo1(bot,update)
  elif a =="what is your name?" or a=="name please":
    demo2(bot,update)
  elif a =="turn on the light" or a =="light on":
    lightOn(bot,update)
  elif a =="turn off the light" or a =="light off":
    lightOff(bot,update)
  elif a =="turn on the fan" or a =="fan on":
    fanOn(bot,update)
  elif a =="turn off the fan" or a =="fan off":
    fanOff(bot,update)
  else:
    bot.message.reply_text('Invalid Text')


BOT_TOKEN = os.getenv('BOT_TOKEN')
u = Updater(BOT_TOKEN,use_context=True)
dp = u.dispatcher
dp.add_handler(MessageHandler(Filters.text,main))
u.start_polling()
u.idle()
