import os
import discord
import random
from discord.ext import commands
# rate responses
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
# playlist
playlists = ['https://open.spotify.com/playlist/283WZvKuACszj3K0xyId4V?si=pqjTqhj4R6iqzlPFWvyo7A&dl_branch=1', 'https://open.spotify.com/playlist/0dVAtxbrA56wsgxuP7XKMe?si=Guq-iHRiTLWGtckMUxXtfg&dl_branch=1', 'https://open.spotify.com/playlist/6pwwwIa0kX1nooQBn5InpB?si=0e9553d7807d4677']
# among us
amongUs = ['https://tenor.com/view/among-us-twerk-yellow-ass-thang-gif-18983570', 'https://imgur.com/a/VMmL45B', 'https://imgur.com/a/o1tlY0O', 'https://imgur.com/a/x58bHsf']
# useless net
uselessWebsites = ['https://www.hackertyper.com/', 'https://onefishstudio.net/ucg', 'https://pointerpointer.com/', 'https://www.boredbutton.com/', 'https://smashthewalls.com/']
# cute animal
cuteAnimal = ['https://imgur.com/t/aww/EsVNl3y', 'https://imgur.com/t/aww/OYSoXGx', 'https://imgur.com/t/aww/EKKWq5Q', 'https://imgur.com/t/aww/hBkTtOT']
# recommendations kept here and not in bot.py so it doesnt fill up the whole thing
romanceMovies = ['Crounching Tiger, Hidden Dragon: https://bit.ly/3inx1Wx', 'Call Me by Your Name: https://imdb.to/3xjfsL6']
animatedMovies = ['Luca: https://bit.ly/3yk6y1f', "Howl's Moving Castle: https://imdb.to/3jgHWQY", 'Your Name.: https://imdb.to/37khqk1', 'The Emoji Movie: https://imdb.to/3iqvOgW']
comedyMovies = ['John Mulaney: Kid Gorgeous: https://imdb.to/2TVtSDR', 'Bo Burnham: Inside: https://imdb.to/3CqZJh8']
# shows 
cartoonShows = ['The Amazing World of Gumball: https://imdb.to/3iiK5w7', 'Lazor Wulf: https://imdb.to/3fnNmZd', 'Tuca & Bertie: https://imdb.to/3ydQ8HT']
comedyShows = ['Shrill: https://imdb.to/3fyjFoq', 'Schmigadoon: https://imdb.to/3lns2a3']
animeShows = ['One Piece: https://imdb.to/3imsmUr', 'Rascal Does Not Dream of Bunny Girl Senpai: https://imdb.to/3A25i3w']
dramaShows = ['Money Heist: https://imdb.to/3lxwK59', 'The Morning Show: https://imdb.to/3xpL7L8']
# music genres 
rockMusic = ['day6: https://bit.ly/3ig3cH6']
alternativeMuic = ['Joji: https://bit.ly/3A0Op9b', 'Rex Orange County: https://bit.ly/2Vi61Pl']
# albums
popAlbums = ['Happier than Ever: https://bit.ly/3yjMdJv', 'Planet Her: https://bit.ly/3jeaA5h']
indieAlbums = ['Sling: https://bit.ly/3iksXpM', 'Jubilee: https://bit.ly/3jl9F34']
rnbAlbums = ['Ctrl: https://bit.ly/3fGqPan', "When It's All Said And Done... Take Time: https://bit.ly/3zX5il6"]
# jokes 
jokes = ['look in the mirrror', 'what did the fridge say to the toaster? ||nothing at all, they cant talk lmfao||', 'how do you put an elephant in the fridge? || you open the door, put the elephant in, and close the door||"]

# bot running stuff 

bot = commands.Bot(command_prefix='?')

@bot.event
async def on_ready():
    print('running now')

# commands 
@bot.listen()
async def on_message(message):
    if message.author == bot.user:
        return
    if message.author.bot: return
    
    if message.content == '?test':
        await message.channel.send('test message!')

    if message.content == '?rate': # from L
        likeResponseRandom = random.choice(rateResponses) # random choice
        await message.channel.send(likeResponseRandom) 

    if message.content == '?dance': # from jericho (i will cry if this code does not work probably)
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

   
    if message.content == '?wallpaper': # from adam
        await message.channel.send('all of these wallpapers are intented for phones. support for desktop wallpapers are on their way') 
        await message.channel.send('avaliable categories: anime, apple, landscape, cityscape, space, color, pride or illustration?')
        await message.channel.send('do "?wp (then the catergory you want)"')
        
    if message.content == '?wp landscape':
        randomLandscape = random.choice(landscapeWallpaper)
        await message.channel.send(randomLandscape)

    if message.content == '?wp apple':
        randomApple = random.choice(appleWallpaper)
        await message.channel.send(randomApple)

    if message.content == '?wp anime':
        randomAnime = random.choice(animeWallpaper)
        await message.channel.send(randomAnime)

    if message.content == '?wp cityscape':
        randomCityscape = random.choice(cityWallpper)
        await message.channel.send(randomCityscape)

    if message.content == '?wp space':
        randomSpace = random.choice(spaceWallpaper)
        await message.channel.send(randomSpace)

    if message.content == '?wp color':
        randomColor = random.choice(colorWallpaper)
        await message.channel.send(randomColor)

    if message.content == '?wp pride':
        randomPride = random.choice(prideWallpaper)
        await message.channel.send(randomPride)
        
    if message.content == '?wp illustration':
        randomllustration = random.choice(illustrationWallpaper)
        await message.channel.send(randomllustration)

    if message.content == '?playlist':
        randomPlaylist = random.choice(playlists)
        await message.channel.send(randomPlaylist)

    if message.content == '?among us': # from dj
        randomAmogUs = random.choice(amongUs)
        await message.channel.send(randomAmogUs)
		
    if message.content == '?useless':
        randomUseless = random.choice(uselessWebsites)
        await message.channel.send(randomUseless)

    if message.content == '?cute':
        randomCute = random.choice(cuteAnimal)
        await message.channel.send(randomCute)
        
    # recommendation cluster fuck
        
    if message.content == '?recommendations':
        await message.channel.send('what would you like: a movie, tv show, video game, or music artist?')
	await message.channel.send('do ?(catergory)')
        
    if message.content == '?movie':
        await message.channel.send('which would you like: romance, drama, or animated?')
        await message.channel.send('do ?movie (catergory)')
            
    if message.content == '?movie romance':
        randomRomance = random.choice(romanceMovies)
        await message.channel.send(randomRomance)
        
    if message.content == '?movie animated':
        randomAnimated = random.choice(animatedMovies)
        await message.channel.send(randomAnimated)
              
    if message.content == '?tv show':
        await message.channel.send('which would you like: romance, comedy, drama, anime')
	await message.channel.send('do ?tv (catergory)')
          
    if message.content == '?tv comedy':
        randomComedyTV = random.choice(comedyShows)
        await message.channel.send(randomComedyTV)
            
    if message.content == '?tv cartoon':
        randomCartoon = random.choice(cartoonShows)
        await message.channel.send(randomCartoon)

	if message.content == '?tv anime':
		randomAnime = random.choice(animeShows)
        await message.channel.send(randomAnime)
	
	if message.content == '?tv drama':
		randomDrama = random.choice(dramaShows)
		await message.channel.send(randomDrama)

    if message.content == '?artist':
        await message.channel.send('which would you like: rock, pop, or indie?')
		await message.channel.send('do ?artist (catergory)')
				  
    if message.content == '?art rock':
        randomRock = random.choice(rockMusic)
        await message.channel.send(randomRock)
        
    if message.content == '?art alternative':
        randomAlt = random.choice(alternativeMuic)
        await message.channel.send(randomAlt)
          
    if message.content == '?album':
        await message.channel.send('which would you like: pop, indie, or R&B?')
		await message.channel.send('do ?album (catergory)')
        
    if message.content == '?album pop':
        randomPop = random.choice(popAlbums)
        await message.channel.send(randomPop)
          
    if message.content == '?album indie':
        randomIndie = random.choice(indieAlbums)
        await message.channel.send(randomIndie)
          
    if message.content == '?album R&B':
        randomRNB = random.choice(rnbAlbums)
        await message.channel.send(randomRNB)
        
    if message.content == '?submit':
        await message.channel.send('submit stuff here: https://forms.gle/jz4bemZKgjj4d1oWA')
          
    if message.content == '?credits':
        await message.channel.send('here are all of the cool people who gave ideas to the bot: https://github.com/julianagar/Poop-Bot/blob/main/README.md')

    if message.content == '?website':
        await message.channel.send('https://julianagar.carrd.co/#poop-bot')

    if message.content == '?server':
        await message.channel.send('https://discord.gg/bq6ZuHVaHV')
        
        
# more bot running stuff 
      
@bot.event
async def on_message():
    print(message.content)
			
bot.run('token')
