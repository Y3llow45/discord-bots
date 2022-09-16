import discord
from keep_alive import keep_alive
import requests
import json
import random
from discord.ext import commands 
from datetime import date
from time import gmtime, strftime

hi_words = ["hi", "h1", "h1", "H1", "hey", "h3y", "H3y", "H3Y", "h3Y", "hyo", "hello", "h3ll0", "H3LL0", "H3ll0", "h3LLO", "YO", "Y0", "y0", "yo", "sup", "SUP", "SuP", "yoo", "heyo"]

hi_answer = ["heyo", "yoo", "SUP", "HI", "hello", "hi", "H3ll0", "hey"]

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
    if message.content.startswith('cat'):
        await message.channel.send(random.choice(cat))
    if message.content == "dt":
        await message.channel.send(strftime("%Y-%m-%d %H:%M:%S", gmtime()))


keep_alive()
bot.run('***********************************************************')
