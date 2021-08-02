# shit ton of modules i wanna die 
import os  # await commands
import discord # obvious
import time # time.sleep
import random # randoming lists
from dotenv import load_dotenv # other discord stuff
from discord.ext import commands # more discord stuff :zany_face:
# for the recommendation feature (importing from recommendationlists.py)
from recommedationlists import romanceMovies
from recommedationlists import dramaMovies
from recommedationlists import animatedMovies
from recommedationlists import romanceShows
from recommedationlists import narrativeGames
from recommedationlists import adventureGames
from recommedationlists import puzzleGames
from recommedationlists import rockMusic
from recommedationlists import popMusic
from recommedationlists import indieMusic

# lists, dictionaries, and variables for commands

# rate
rateResponses = ['me likey', 'me no likey']
# wallpapers
landscapeWallpaper = ['https://imgur.com/a/SsRbe8U', 'https://imgur.com/a/Qslcgi3', 'https://imgur.com/a/xD9luhv']
appleWallpaper = ['https://imgur.com/a/sDKkSPV', 'https://imgur.com/a/Lw4bc8T', 'https://imgur.com/a/LFBxJw3']
animeWallpaper = ['https://imgur.com/a/MEnmivv', 'https://imgur.com/a/L1fwQyh', 'https://imgur.com/a/ibNeh4']
# among us
amongUs = ['https://tenor.com/view/among-us-twerk-yellow-ass-thang-gif-18983570', 'https://imgur.com/a/VMmL45B', 'https://imgur.com/a/o1tlY0O', 'https://imgur.com/a/x58bHsf']
# useless net
uselessWebsites = ['https://www.hackertyper.com/', 'https://onefishstudio.net/ucg', 'https://pointerpointer.com/', 'https://www.boredbutton.com/', 'https://smashthewalls.com/']
# cute animal
cuteAnimal = ['https://imgur.com/t/aww/EsVNl3y', 'https://imgur.com/t/aww/OYSoXGx', 'https://imgur.com/t/aww/EKKWq5Q', 'https://imgur.com/t/aww/hBkTtOT']
# jokes
dadJokes = []
funnyJokes = []
cleverJokes = []
comedianQuotes = []
# playlists
# recommendations

# launching bot

load_dotenv()
token = os.getenv(token)

# prefix 
prefix = commands.Bot(command_prefix='poop')

client = discord.Client()

@client.event
async def on_ready():
	print(f'{client.user} has connected to discord!')
	
client.run(token) # leak if dumbass

# message commands trigged using a message

@client.event
async def on_message(message):
	if message.author == client.user:
		return
	
	# commands
	
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
		# i hate this shit
	
	if message.content == 'guess':
		ifCorrect = True
		numberGuess = random.randint(0, 100)
		await message.channel.send('ok, i guessed a number between 0 and 100. guess now: ')
		if ifCorrect:
			if message.content == numberGuess:
				await message.channel.send('great job! you guessed it')
				ifCorrect = False
			else:
				await message.channel.send('whoops, that wasnt it. try again')
				continue
	
	# features 
		
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
			
	if message.content == 'among us': # from dj
		randomAmogUs = random.choice(amongUs)
		await message.channel.send(randomAmogUs)
		
	if message.content == 'useless net':
		randomUseless = random.choice(uselessWebsites)
		await message.channel.send(randomUseless)
		
	if message.content == 'cute':
		randomAnimal = random.choice(cuteAnimal)
		await message.channel.send(randomAnimal)
		
	if message.content == 'jokes':
		
	if message.content == 'credits':
		await message.channel.send('here are all of the cool people who gave ideas to the bot: ',
					   'https://github.com/julianagar/Poop-Bot/blob/main/README.md')
	
