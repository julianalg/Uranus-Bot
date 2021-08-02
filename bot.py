# shit ton of modules i wanna die 
import os  # await commands
import discord # obvious
import time # time.sleep
import random # randoming lists
from dotenv import load_dotenv # other discord stuff
from discord.ext import commands # more discord stuff :zany_face:
# for the recommendation feature (importing from recommendationlists.py)
from recommedationlists import romanceMovies
from recommedationlists import animatedMovies
from recommedationlists import comedyShows
from recommedationlists import cartoonShows
from recommedationlists import rockMusic
from recommedationlists import alternativeMuic
from recommedationlists import popAlbums
from recommedationlists import indieAlbums
from recommedationlists import rnbAlbums

# lists, dictionaries, and variables for commands

# rate
rateResponses = ['me likey', 'me no likey']
# wallpapers
landscapeWallpaper = ['https://imgur.com/a/SsRbe8U', 'https://imgur.com/a/Qslcgi3', 'https://imgur.com/a/xD9luhv']
appleWallpaper = ['https://imgur.com/a/sDKkSPV', 'https://imgur.com/a/Lw4bc8T', 'https://imgur.com/a/LFBxJw3']
animeWallpaper = ['https://imgur.com/a/MEnmivv', 'https://imgur.com/a/L1fwQyh', 'https://imgur.com/a/ibNeh4']
cityWallpper = ['https://imgur.com/a/LBUviZT', 'https://imgur.com/a/hxcjPjO', 'https://imgur.com/a/16t7AYu']
spaceWallpaper = ['https://imgur.com/a/eujV4dv', 'https://imgur.com/a/0yxdPlp', 'https://imgur.com/a/KxmsLhM']
colorWallpaper = ['https://imgur.com/a/dEYjCyT', 'https://imgur.com/a/M5eqvsj', 'https://imgur.com/a/LE96HIs']
prideWallpaper = ['https://imgur.com/a/LyQtx5f', 'https://imgur.com/a/yKy3uP8', 'https://imgur.com/a/YAbmrGV']
illustrationWallpaper = ['https://imgur.com/a/2TWHDkz', 'https://imgur.com/a/wRSe6oR', 'https://imgur.com/a/wRSe6oR']
# among us
amongUs = ['https://tenor.com/view/among-us-twerk-yellow-ass-thang-gif-18983570', 'https://imgur.com/a/VMmL45B', 'https://imgur.com/a/o1tlY0O', 'https://imgur.com/a/x58bHsf']
# useless net
uselessWebsites = ['https://www.hackertyper.com/', 'https://onefishstudio.net/ucg', 'https://pointerpointer.com/', 'https://www.boredbutton.com/', 'https://smashthewalls.com/']
# cute animal
cuteAnimal = ['https://imgur.com/t/aww/EsVNl3y', 'https://imgur.com/t/aww/OYSoXGx', 'https://imgur.com/t/aww/EKKWq5Q', 'https://imgur.com/t/aww/hBkTtOT']
# playlists
playlists = ['https://open.spotify.com/playlist/283WZvKuACszj3K0xyId4V?si=pqjTqhj4R6iqzlPFWvyo7A&dl_branch=1', 'https://open.spotify.com/playlist/0dVAtxbrA56wsgxuP7XKMe?si=Guq-iHRiTLWGtckMUxXtfg&dl_branch=1', 'https://open.spotify.com/playlist/6pwwwIa0kX1nooQBn5InpB?si=0e9553d7807d4677']
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
		while ifCorrect:
			if message.content == numberGuess:
				await message.channel.send('great job! you guessed it')
				ifCorrect = False
			else:
				await message.channel.send('whoops, that wasnt it. try again')
				continue
	
	# features 
		
	if message.content == 'wallpaper': # from adam
		await message.channel.send('all of these wallpapers are intented for phones. support for desktop wallpapers are on their way', 
			'avaliable categories: anime, apple, landscape, cityscape, space, color, pride or illustration?')
		if message.content == 'landscape':
			randomLandscape = random.choice(landscapeWallpaper)
			await message.channel.send(randomLandscape)
		if message.content == 'apple':
			randomApple = random.choice(appleWallpaper)
			await message.channel.send(randomApple)
		if message.content == 'anime':
			randomAnime = random.choice(animeWallpaper)
			await message.channel.send(randomAnime)
		if message.content == 'cityscape':
			randomCityscape = random.choice(cityWallpper)
			await message.channel.send(randomCityscape)
		if message.content == 'space':
			randomSpace = random.choice(spaceWallpaper)
			await message.channel.send(randomSpace)
		if message.content == 'color':
			randomColor = random.choice(colorWallpaper)
			await message.channel.send(randomColor)
		if message.content == 'pride':
			randomPride = random.choice(prideWallpaper)
			await message.channel.send(randomPride)
		if message.content == ' illustration':
			randomllustration = random.choie(illustrationWallpaper)
			await message.channel.send(randomllustration)
			
	if message.content == 'among us': # from dj
		randomAmogUs = random.choice(amongUs)
		await message.channel.send(randomAmogUs)
		
	if message.content == 'useless net':
		randomUseless = random.choice(uselessWebsites)
		await message.channel.send(randomUseless)
		
	if message.content == 'cute':
		randomAnimal = random.choice(cuteAnimal)
		await message.channel.send(randomAnimal)

	if message.content == 'recommendations':
		await message.channel.send('what would you like: a movie, tv show, video game, or music artist?')
		if message.content == 'movie':
			await message.channel.send('which would you like: romance, drama, or animated')
			if message.content == 'romance':
				randomRomance = random.choice(romanceMovies)
				await message.channel.send(randomRomance)
			if message.content == 'animated':
				randomAnimated = random.choice(animatedMovies)
				await message.channel.send(randomAnimated)
		if message.content == 'tv show':
			await message.channel.send('which would you like: romance, comedy, drama')
			if message.content == 'comedy':
				randomComedyTV = random.choice(comedyShows)
				await message.channel.send(randomComedyTV)
			if message.content == 'cartoon':
				randomCartoon = random.choice(cartoonShows)
				await message.channel.send(randomCartoon)
		if message.content == 'artist':
			await message.channel.send('which would you like: rock, pop, or indie?')
			if message.content == 'rock':
				randomRock = random.choice(rockMusic)
				await message.channel.send(randomRock)
			if message.content == 'alternative':
				randomAlt = random.choice(alternativeMuic)
				await message.channel.send(randomAlt)
		if message.content == 'album':
			await message.channel.send('which would you like: pop, indie, or R&B?')
			if message.content == 'pop':
				randomPop = random.choice(popAlbums)
				await message.channel.send(randomPop)
			if message.content == 'indie':
				randomIndie = random.choice(indieAlbums)
				await message.channel.send(randomIndie)
			if message.content == 'R&B':
				randomRNB = random.choice(rnbAlbums)
				await message.channel.send(randomRNB)

	if message.content == 'playlist':
		randomPlaylist = random.choice(playlists)
		await message.channel.send(randomPlaylist)

	if message.content == 'submit':
		await message.channel.send('submit stuff here: https://forms.gle/jz4bemZKgjj4d1oWA')
		
	if message.content == 'credits':
		await message.channel.send('here are all of the cool people who gave ideas to the bot: ',
					   'https://github.com/julianagar/Poop-Bot/blob/main/README.md')
