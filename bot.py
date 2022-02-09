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
        await message.channel.send('test message! \nlatency: ' + str(round(bot.latency, 1)))

    if message.content.startswith('?void shout'):
        shouts.append(message.content[12:])
        await message.channel.send('done. you shouted: ' + '**' + message.content[12:] + '**')
        print(shouts)
        print('total: ' + str(len(shouts)))
     
    if message.content == '?void pull':
        await message.channel.send('pulled this: ' + random.choice(shouts))
        if randint(1,5) == 1:
            await message.channel.send('*tip: you can shout a message by saying: ?void shout [message]*')

    if message.content.startswith("?google"):
        query = message.content[2-6:]
        await message.channel.send('https://lmgtfy.app/?q=' + query + '&iie=1')
    
    if message.content == '?tone':
        await message.channel.send(embed=discord.Embed(title="tone indicators", description="tone indicators are ways to indicate tones in text. \n learn more: https://toneindicators.carrd.co \n usage: ?tone {tone indicator}"))
        
    if message.content == '?figurative language':
        await message.channel.send(embed=discord.Embed(title="figurative language", description="a way of expressing a story/thoughts using words that do not use its strict meaning. \n usage: ?fig lan {type of figurative language}"))
        
    if message.content == '?about':
        await message.channel.send(embed=discord.Embed(title="Uranus Bot", description="[a discord bot that was made bcuz i was bored](https://julianagar.github.io/uranusbot-website/) \n version 2.0 (wip) \n get uptime info using ?about"))
        
    if message.content == '?time machine': 
        await message.channel.send(embed=discord.Embed(title="ten years ago (via neal.fun)", description="websites as they were 10 years ago today. \nvia [neal.fun](https://neal.fun) \nusage: ?time machine [cnn, reddit, nyt, bbc, fox, amazon]"))
        
    if message.content == '?time machine cnn':
        await message.channel.send(embed=discord.Embed(title="CNN 10 years ago today", description="[link](https://ten-years-ago.neal.fun/cnn.com/)"))
        
    if message.content == '?time machine reddit':
        await message.channel.send(embed=discord.Embed(title="Reddit 10 years ago today", description="[link](https://ten-years-ago.neal.fun/reddit.com/)"))

    if message.content == '?time machine nyt':
       await message.channel.send(embed=discord.Embed(title="New York Times 10 years ago today", description="[link](https://ten-years-ago.neal.fun/nytimes.com/)"))

    if message.content == '?time machine bbc':
        await message.channel.send(embed=discord.Embed(title="BBC 10 years ago today", description="[link](https://ten-years-ago.neal.fun/bbc.com/)"))
    
    if message.content == '?time machine fox':
        await message.channel.send(embed=discord.Embed(title="Fox News 10 years ago today", description="[link](https://ten-years-ago.neal.fun/foxnews.com/)"))

    if message.content == '?time machine amazon':
        await message.channel.send(embed=discord.Embed(title="Amazon 10 years ago today", description="[link](https://ten-years-ago.neal.fun/amazon.com/)"))



async def on_message():
  print(message.content)

bot.run('token')
