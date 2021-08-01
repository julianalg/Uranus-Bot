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
token = os.getenv('')

# prefix 
prefix = commands.Bot(command_prefix='poop')

client = discord.Client()

@client.event
async def on_ready():
	print(f'{client.user} has connected to discord!')
	
client.run('')

# message commands trigged using a message
@client.event
async def on_message(message):
	if message.author == client.user:
		return
	
	if message.content == 'rate':
		likeResponseRandom = random.choice(rateResponses) # random choice
		await message.channel.send(likeResponseRandom) 

	if message.content == 'dance':
		await message.channel.send('(_＼ヽ')
		await message.channel.send('　 ＼＼ .Λ＿Λ.')
		await message.channel.send('　　 ＼(　ˇωˇ)')
		await message.channel.send('　　　 >　⌒ヽ')
		await message.channel.send('　　　/ 　 へ＼')
		await message.channel.send('　　 /　　/　＼＼')
		await message.channel.send('　　 ﾚ　ノ　　 ヽ_つ')
		await message.channel.send('　　/　/')
		await message.channel.send('　 /　/|')
		await message.channel.send('　(　(ヽ')
		await message.channel.send('　|　|、＼')
		await message.channel.send('　| 丿 ＼ ⌒)')
		await message.channel.send('　| |　　) /')
		await message.channel.send('`ノ ) 　 Lﾉ')
		await message.channel.send('(_／')
		# i hate this shit

	
