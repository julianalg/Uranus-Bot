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

@bot.event
async def on_ready():
    print("poop bot is now online!")

async def on_message(message):
    if message.author == bot.user:
        return
    if message.author.bot: return 

async def on_message():
  print(message.content)

bot.run('token')
