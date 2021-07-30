# shit ton of modules i wanna die 
import os 
import discord
import time
import random
from dotenv import load_dotenv
from discord.ext import commands

# lists, dictionaries, and variables for commands
rateResponses = ['me likey', 'me no likey']

load_dotenv()
token = os.getenv('ODcwNTA5OTAxNzU4MjAxODU3.YQNzhQ.tjsnPMOvj648GsnHAGMYG8HQINM')

# prefix 
prefix = commands.Bot(command_prefix='poop')

client = discord.Client()

@client.event
async def on_ready():
	print(f'{client.user} has connected to discord!')
	
client.run('ODcwNTA5OTAxNzU4MjAxODU3.YQNzhQ.tjsnPMOvj648GsnHAGMYG8HQINM')

# message commands trigged using a message
@client.event
async def on_message(message):
	if message.author == client.user:
		return
	
	if message.content == 'rate':
		likeResponseRandom = random.choice(deezDylan) # random choice
		await message.channel.send(likeResponseRandom) 
