import discord
from keep_alive import keep_alive
import requests
from discord.ext import commands 
import os
import pyautogui
import time

bot = commands.Bot(command_prefix = '$')  

@bot.command()
async def cmd(ctx, *arg):
    arg = ' '.join(arg)
    print(*arg)
    os.system(f'cmd /c "{arg}"');
    time.sleep(1)
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(r'0.png')
    await ctx.send(file=discord.File("{counter}.png"));
    os.remove(r"0.png") 

@bot.command()
async def say(ctx, *arg):
  arg = ' '.join(arg)
  await ctx.send(arg)
    
@bot.event
async def on_member_join(member):
  print(f'{member} has join the server')

@bot.event
async def on_member_remove(member):
  print(f'{member} has left the server')

@bot.event
async def on_ready():
  await bot.change_presence(status=discord.Status.online, activity=discord.Game('u dum dum'), )
  print(bot)
  print("started!")

keep_alive()
bot.run('token')   #<==== your token here!!!
