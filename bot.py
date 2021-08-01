# shit ton of modules i wanna die 
import os 
import discord
import time
import random
from dotenv import load_dotenv
from discord.ext import commands

# lists, dictionaries, and variables for commands
rateResponses = ['me likey', 'me no likey']
landscapeWallpaper = ['https://imgur.com/a/SsRbe8U', 'https://imgur.com/a/Qslcgi3', 'https://imgur.com/a/xD9luhv']
appleWallpaper = ['https://imgur.com/a/sDKkSPV', 'https://imgur.com/a/Lw4bc8T', 'https://imgur.com/a/LFBxJw3']
animeWallpaper = ['https://imgur.com/a/MEnmivv', 'https://imgur.com/a/L1fwQyh', 'https://imgur.com/a/ibNeh4']

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
	
	if message.content == 'rate': # from L
		likeResponseRandom = random.choice(rateResponses) # random choice
		await message.channel.send(likeResponseRandom) 

	if message.content == 'dance': # from jericho (i will cry if this code does not work probably)
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
		
	if message.content == 'wallpaper': # from adam
		await message.channel.send('all of these wallpapers are intented for phones. support for desktop wallpapers are on their way')
		await message.channel.send('avaliable categories: anime, apple, and landscape')
		if message.content == 'landscape':
			randomLandscape = random.choice(landscapeWallpaper)
			await message.channel.send(randomLandscape)
		if message.content == 'apple':
			randomApple = random.choice(appleWallpaper)
			await message.channel.send(randomApple)
		if message.content == 'anime':
			randomAnime = random.choice(animeWallpaper)
			await message.channel.send(randomAnime)
			
	if message.content == 'credits':
		await message.channel.send('here are all of the cool people who gave ideas to the bot: ',
					   'https://github.com/julianagar/Poop-Bot/blob/main/bot.py')
	
