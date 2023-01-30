import discord
from keep_alive import keep_alive
import requests
import json
import random
from discord.ext import commands 
from datetime import date
from time import gmtime, strftime

hi_words = ["hi", "hey", "hello", "Hello", "Hey", "Hyo", "hyo", "sup", "Hi", "yoo", "heyo", "Yoo", "Heyo"]

hi_answer = ["heyo", "yoo", "Hey", "Hi", "hello", "hi", "H3ll0", "hey"]


#From https://www.freecodecamp.org/news/create-a-discord-bot-with-python/
def get_qoute():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

bot = commands.Bot(command_prefix = '$')   

@bot.event
async def on_ready():
  print(bot)
  print("started!")

#@bot.command(aliases=['p', 'q'])
#async def ping (ctx, arg=None):
#  if arg == "pong":
#    await ctx.send("pong!")
#  else:
#    await ctx.send(f"Ping is: {round(bot.latency * 1000)}ms")
    
#@bot.event
#async def on_member_join(member):
#  print(f'{member} has join the server')

#@bot.event
#async def on_member_remove(member):
#  print(f'{member} has left the server')
#
#@bot.event
#async def on_ready():
#  await bot.change_presence(status=discord.Status.online, activity=discord.Game('$commands_help'), )
#  print(bot)
#  print("started!")
#
#keep_alive()
#bot.run('')
  
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
  
    msg = message.content

    if any(word in msg for word in hi_words):
        await message.channel.send(random.choice(hi_answer))
    if message.content.startswith('quote'):
        quote = get_qoute()
        await message.channel.send(quote)
    if message.content.startswith('bb'):
        await message.channel.send('bb') 
    if message.content == "dt":
        await message.channel.send(strftime("%Y-%m-%d %H:%M:%S", gmtime()))


keep_alive()
bot.run('***********************************************************')


