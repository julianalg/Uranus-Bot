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
bootMessages = ["back from my nap", "oops back to make ur day awful"]
shouts = []

@bot.event
async def on_ready():
    print("poop bot is now online!")
    channel = bot.get_channel(872713496675110973)
    await channel.send(random.choice(bootMessages))


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

    if message.content == '?time machine youtube':
        await message.channel.send(embed=discord.Embed(title="YouTube 10 years ago today", description="[link](https://ten-years-ago.neal.fun/youtube.com/)"))

    if message.content == '?time machine espn':
        await message.channel.send(embed=discord.Embed(title="ESPN 10 years ago today"), description="[link](https://ten-years-ago.neal.fun/espn.go.com/)")

    if message.content == '?time machine apple':
        await message.channel.send(embed=discord.Embed(title="Apple.com 10 years ago today", description="[link](https://ten-years-ago.neal.fun/apple.com/)"))

    if message.content == '?time machine imdb':
        await message.channel.send(embed=discord.Embed(title="IMDb 10 years ago today"), description="[link](https://ten-years-ago.neal.fun/imdb.com/)")

    if message.content == '?time machine cnet':
        await message.channel.send(embed=discord.Embed(title="CNET 10 years ago today", description="[link](https://ten-years-ago.neal.fun/cnet.com/)"))

    if message.content == '?time machine ign':
        await message.channel.send(embed=discord.Embed(title="IGN 10 years ago today", description="[link](https://ten-years-ago.neal.fun/ign.com/)"))

    if message.content == '?tone':
      embedVar = discord.Embed(title="tone indicators:", description="usage: ?tone {tone indicator}", color=0x00ff00)
      await message.channel.send(embed=embedVar)

    if message.content == '?tone j':
      embedVar = discord.Embed(title="/j:", description="joking", color=0x00ff00)
      await message.channel.send(embed=embedVar)

    if message.content == '?tone hj':
      embedVar = discord.Embed(title="/hj:", description="half-joking", color=0x00ff00)
      await message.channel.send(embed=embedVar)

    if message.content == '?tone s':
      embedVar = discord.Embed(title="/s:", description="sarcastic", color=0x00ff00)
      await message.channel.send(embed=embedVar)

    if message.content == '?tone gen':
      embedVar = discord.Embed(title="/gen or /g:", description="genuine", color=0x00ff00)
      await message.channel.send(embed=embedVar)

    if message.content == '?tone g':
      embedVar = discord.Embed(title="/gen or /g:", description="geniune", color=0x00ff00)
      await message.channel.send(embed=embedVar)

    if message.content == '?tone srs':
      embedVar = discord.Embed(title="/srs:", description="serious", color=0x00ff00)
      await message.channel.send(embed=embedVar)

    if message.content == '?tone nsrs':
      embedVar = discord.Embed(title="/nsrs:", description="not serious", color=0x00ff00)
      await message.channel.send(embed=embedVar)

    if message.content == '?tone pos':
      embedVar = discord.Embed(title="/pos or /pc:", description="positive connotation", color=0x00ff00)
      await message.channel.send(embed=embedVar)

    if message.content == '?tone pc':
      embedVar = discord.Embed(title="/pos or /pc:", description="positive connotation", color=0x00ff00)
      await message.channel.send(embed=embedVar)

    if message.content == '?tone neu':
      embedVar = discord.Embed(title="/neu:", description="neutral connotation", color=0x00ff00)
      await message.channel.send(embed=embedVar)

    if message.content == '?tone neg':
      embedVar = discord.Embed(title="/neg or /nc:", description="negative connotation", color=0x00ff00)
      await message.channel.send(embed=embedVar)

    if message.content == '?tone nc':
      embedVar = discord.Embed(title="/neg or /nc:", description="negative connotation", color=0x00ff00)
      await message.channel.send(embed=embedVar)

    if message.content == '?tone p':
      embedVar = discord.Embed(title="/p:", description="platonic, (of love or friendship) intimate and affectionate but not sexual.", color=0x00ff00)
      await message.channel.send(embed=embedVar)

    if message.content == '?tone r':
      embedVar = discord.Embed(title="/r:", description="romantic", color=0x00ff00)
      await message.channel.send(embed=embedVar)

    if message.content == '?tone c':
      embedVar = discord.Embed(title="/c:", description="copypasta", color=0x00ff00)
      await message.channel.send(embed=embedVar)

    if message.content == '?tone l':
      embedVar = discord.Embed(title="/l or /ly:", description="lyrics", color=0x00ff00)
      await message.channel.send(embed=embedVar)

    if message.content == '?tone ly':
      embedVar = discord.Embed(title="/l or /ly:", description="lyrics", color=0x00ff00)
      await message.channel.send(embed=embedVar)

    if message.content == '?tone lh':
      embedVar = discord.Embed(title="/lh:", description="light-hearted", color=0x00ff00)
      await message.channel.send(embed=embedVar)

    if message.content == '?tone nm':
      embedVar = discord.Embed(title="/nm:", description="not mad", color=0x00ff00)
      await message.channel.send(embed=embedVar)

    if message.content == '?tone lu':
      embedVar = discord.Embed(title="/lu:", description="a little-upset", color=0x00ff00)
      await message.channel.send(embed=embedVar)

    if message.content == '?tone nbh':
      embedVar = discord.Embed(title="/nbh", description="for when you're vagueposting or venting, but it's directed at nobody here", color=0x00ff00)
      await message.channel.send(embed=embedVar)

    if message.content == '?tone sx':
      embedVar = discord.Embed(title="/sx or /x", description="sexual intent")
      await message.channel.send(embed=embedVar)
    
    if message.content == '?tone x':
      embedVar = discord.Embed(title="/sx or x", description="sexual intent")
      await message.channel.send(embed=embedVar)

    if message.content == '?tone nsx':
      embedVar = discord.Embed(title="/nsx or /nx", description="non-sexual intent")
      await message.channel.send(embed=embedVar)

    if message.content == '?tone nx':
      embedVar = discord.Embed(title="/nsx or /nx", description="non-sexual intent")
      await message.channel.send(embed=embedVar)

    if message.content == '?tone rh':
      embedVar = discord.Embed(title="/rh or /rt", description="rhetorical question")
      await message.channel.send(embed=embedVar)

    if message.content == '?tone rt':
      embedVar = discord.Embed(title="/rh or /rt", description="rhetorical question")
      await message.channel.send(embed=embedVar)

    if message.content == '?tone t':
      embedVar = discord.Embed(title="/t", description="teasing")
      await message.channel.send(embed=embedVar)
      
    if message.content == '?tone ij':
      embedVar = discord.Embed(title="/ij", description="inside joke")
      await message.channel.send(embed=embedVar)
      
    if message.content == '?tone m':
      embedVar = discord.Embed(title="/m", description="metaphorically")
      await message.channel.send(embed=embedVar)

    if message.content == '?tone li':
      embedVar = discord.Embed(title="/li", description="literally")
      await message.channel.send(embed=embedVar)

    if message.content == '?tone hyp':
      embedVar = discord.Embed(title="/hyperbole", description="hyperbole")
      await message.channel.send(embed=embedVar)

    if message.content == '?tone f':
      embedVar = discord.Embed(title="/f", description="fake")
      await message.channel.send(embed=embedVar)

    if message.content == '?tone th':
      embedVar = discord.Embed(title="/th", description="threat")
      await message.channel.send(embed=embedVar)

    if message.content == '?tone cb':
      embedVar = discord.Embed(title="/cb", description="clickbait")
      await message.channel.send(embed=embedVar)

    if message.content == '?tone explain':
      embedVar = discord.Embed(title="What are tone indicators?", description="Tone indicators are paralinguistic signifiers used at the ends of statements to help readers fill in the blanks.", url="https://tonetags.carrd.co/#intro")
      await message.channel.send(embed=embedVar)

    if message.content == '?tone credits':
      embedVar = discord.Embed(title="source & list of all tone indicators", url="https://toneindicators.carrd.co/")
      await message.channel.send(embed=embedVar)


async def on_message():
  print(message.content)

bot.run('ODcwNTA5OTAxNzU4MjAxODU3.YQNzhQ.OpIexUSJVQgsJjEVn6nVRP74VIc')
