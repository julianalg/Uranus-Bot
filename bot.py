# bot.py
import os
import time
import discord
from random import randint
from random import seed
import random
from discord.ext import commands, tasks
from discord.ext.commands import CommandNotFound

bot = commands.Bot(command_prefix='ur')

shouts = []

@bot.event
async def on_ready():
    print("poop bot is now online!")

@bot.listen()
async def on_message(message):
    if message.author == bot.user:
        return
    if message.author.bot: return

    if message.content == '?test':
        await message.channel.send('test message!')

    if message.content.startswith('?void shout'):
        shouts.append(message.content)
        await message.channel.send('done. you shouted: ' + '**' + message.content + '**')
        #print(shouts)
        #print('total: ' + len(shouts))
     
    if message.content == '?void pull':
        await message.channel.send('pulled this: ' + random.choice(shouts))
        if randint(1,5) == 1:
            await message.channel.send('*tip: you can shout a message by saying: ?void shout [message]*')

    if message.content.startswith("?google"):
        query = message.content[2-6:]
        await message.channel.send('https://lmgtfy.app/?q=' + query + '&iie=1')
    

    

async def on_message():
  print(message.content)

bot.run('token')
