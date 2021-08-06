import os
import discord
import random
from discord.ext import commands

# rate responses
rateResponses = ['me likey', 'me no likey', 'muy bueno']
# wallpapers
landscapeWallpaper = ['https://imgur.com/a/SsRbe8U', 'https://imgur.com/a/Qslcgi3', 'https://imgur.com/a/xD9luhv', 'https://media.discordapp.net/attachments/872928261510934618/873010537976430612/5c3fd9952bbd0235c4911da8d9fdac5e.webp?width=299&height=532', 'https://media.discordapp.net/attachments/872928261510934618/873010564102750279/photo-1501786223405-6d024d7c3b8d.jpeg?width=355&height=532']
appleWallpaper = ['https://imgur.com/a/sDKkSPV', 'https://imgur.com/a/Lw4bc8T', 'https://imgur.com/a/LFBxJw3', 'https://media.discordapp.net/attachments/872928261510934618/873010512957423667/papers.co-sd03-classic-mac-space-apple-blur-34-iphone6-plus-wallpaper.jpg?width=299&height=532', 'https://media.discordapp.net/attachments/872928261510934618/873010538303619142/vng9P7.jpg?width=399&height=532']
animeWallpaper = ['https://imgur.com/a/MEnmivv', 'https://imgur.com/a/L1fwQyh', 'https://imgur.com/a/ibNeh4', 'https://media.discordapp.net/attachments/872928261510934618/873009365584605184/6a40c3cc24d76ff479e0026c4b95443d.jpg?width=299&height=532', 'https://media.discordapp.net/attachments/872928261510934618/873009367983747182/6338.jpg?width=299&height=532', 'https://media.discordapp.net/attachments/872928261510934618/873009366666706994/anime-scenery-sunset-uhdpaper.com-4K-112.jpg?width=299&height=532', 'https://media.discordapp.net/attachments/872928261510934618/873009367937581126/wp4805654.jpg?width=246&height=532']
cityWallpper = ['https://imgur.com/a/LBUviZT', 'https://imgur.com/a/hxcjPjO', 'https://imgur.com/a/16t7AYu', 'https://media.discordapp.net/attachments/872928261510934618/873009360899543060/photo-1496871455396-14e56815f1f4.jpeg?width=338&height=533']
spaceWallpaper = ['https://imgur.com/a/eujV4dv', 'https://imgur.com/a/0yxdPlp', 'https://imgur.com/a/KxmsLhM']
colorWallpaper = ['https://imgur.com/a/dEYjCyT', 'https://imgur.com/a/M5eqvsj', 'https://imgur.com/a/LE96HIs', 'https://media.discordapp.net/attachments/872928261510934618/873009115197231104/Gradient-Background-Wallpaper-001-300x585.jpg?width=225&height=439', 'https://media.discordapp.net/attachments/872928261510934618/873009114761035886/wp4464892.jpg?width=299&height=532']
prideWallpaper = ['https://imgur.com/a/LyQtx5f', 'https://imgur.com/a/yKy3uP8', 'https://imgur.com/a/YAbmrGV', 'https://media.discordapp.net/attachments/872928261510934618/873009355522461706/pride-month-flag-pattern-gocase.jpg?width=259&height=533', ]
illustrationWallpaper = ['https://imgur.com/a/2TWHDkz', 'https://imgur.com/a/wRSe6oR', 'https://imgur.com/a/wRSe6oR', 'https://media.discordapp.net/attachments/872928261510934618/873009108419244112/2847850.jpg?width=246&height=533', 'https://cdn.discordapp.com/attachments/872928261510934618/873009110197628928/6e525c1189a9733d7614ba7c4b554ed2.jpg', 'https://media.discordapp.net/attachments/872928261510934618/873009109891440720/wp5098525.jpg?width=299&height=532', 'https://media.discordapp.net/attachments/872928261510934618/873009112286392370/1172024.jpg?width=266&height=533', ]
# playlist
playlists = ['https://open.spotify.com/playlist/283WZvKuACszj3K0xyId4V?si=pqjTqhj4R6iqzlPFWvyo7A&dl_branch=1', 'https://open.spotify.com/playlist/0dVAtxbrA56wsgxuP7XKMe?si=Guq-iHRiTLWGtckMUxXtfg&dl_branch=1', 'https://open.spotify.com/playlist/6pwwwIa0kX1nooQBn5InpB?si=0e9553d7807d4677', 'https://open.spotify.com/playlist/3nBRaDPtYtWJI6TfL8MEoS?si=gpf_bq6VQWCdcnFnQ4uzBA']
# among us
amongUs = ['https://tenor.com/view/among-us-twerk-yellow-ass-thang-gif-18983570', 'https://imgur.com/a/VMmL45B', 'https://imgur.com/a/o1tlY0O', 'https://imgur.com/a/x58bHsf', 'https://media.discordapp.net/attachments/872928261510934618/873011151527637032/JermaSus.webp?width=270&height=338', 'https://media.discordapp.net/attachments/872928261510934618/873011163506544691/Among-Us-memes.jpg?width=705&height=353', 'https://cdn.discordapp.com/attachments/872928261510934618/873011174860541982/gpue7yepssp51.jpg', 'https://cdn.discordapp.com/attachments/872928261510934618/873011187065970728/maxresdefault.jpg', 'https://cdn.discordapp.com/attachments/872928261510934618/873011199783096410/4jlqsm.jpg', 'https://cdn.discordapp.com/attachments/872928261510934618/873011263196766238/a6077ef30ba8d41d914549906e3b5533.jpg']
# useless net
uselessWebsites = ['https://www.hackertyper.com/', 'https://onefishstudio.net/ucg', 'https://pointerpointer.com/', 'https://www.boredbutton.com/', 'https://smashthewalls.com/', 'https://mondrianandme.com', 'https://thatsthefinger.com', 'https://puginarug.com', 'https://cant-not-tweet-this.com', 'https://alwaysjudgeabookbyitscover.com',  'https://www.mapcrunch.com/', 'https://www.window-swap.com/Window', 'https://screamintothevoid.com/', 'https://archive.org/details/msdos_Oregon_Trail_The_1990']
# cute animal
cuteAnimal = ['https://imgur.com/t/aww/EsVNl3y', 'https://imgur.com/t/aww/OYSoXGx', 'https://imgur.com/t/aww/EKKWq5Q', 'https://imgur.com/t/aww/hBkTtOT', 'https://imgur.com/t/aww/GWvmwBy', 'https://imgur.com/t/aww/cYOAzQG', 'https://imgur.com/t/aww/PYO3jHw', 'https://imgur.com/t/aww/onaQY4K', 'https://imgur.com/t/aww/9JqesLH', 'https://www.reddit.com/r/aww/comments/oyoksi/the_determined_doggo', 'https://www.reddit.com/r/aww/comments/oyjgtp/thats_too_cute_i_will_die_from_cuteness/']
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
jokes = ['look in the mirrror', 'what did the fridge say to the toaster? ||nothing at all, they cant talk lmfao||', 'how do you put an elephant in the fridge? || you open the door, put the elephant in, and close the door||']
# cs asking
csResponseQuestions = ['ask L instead', 'therapy is always an option', 'maybe if you stanned nct you’d find the answer', 'ask @CarlSuburbs on twitter', 'yes, 100%, i can’t stress this enough, absolutely, for sure, no doubt', 'stop. baby don’t stop.', 'There is no such thing as a coincidence. The fact that you have asked me this means that we are energetically and spiritually aligned.']
# tasks
tasks = ['clean bedroom', 'clear out email inbox', 're-do phone home screen', 'change your wallpapers (tip: ?wallpaper)', 'go on a walk or stretch', 'say good morning/afternoon/evening/night or check up on a friend', "sort and sell things you don't need", "contribute ideas to the bot (?submit)"]

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

    if message.content.startswith('?rate'): # from L
        likeResponseRandom = random.choice(rateResponses) # random choice
        await message.channel.send(likeResponseRandom) 
      
    if message.content == '?dance':
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
        
    if message.content.startswith('?ask carl'):
          randomCarl = random.choice(csResponseQuestions)
          await message.channel.send(randomCarl)
        
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
  
    if message.content == '?jokes':
      randomJoke = random.choice(jokes)
      await message.channel.send(randomJoke)
      
    if message.content == '?task':
      randomTasks = random.choice(tasks)
      await message.channel.send(randomTasks)


    # wallpaper
    
    
    if message.content == '?wallpaper': # from adam
        await message.channel.send('all of these wallpapers are intended for phones. support for desktop wallpapers are on their way') 
        await message.channel.send('avaliable categories: anime, apple, landscape, cityscape, space, color, pride or illustration?')
        await message.channel.send('do "?wp (then the catergory you want)"')
        
    if message.content == '?wp': # from adam
        await message.channel.send('all of these wallpapers are intended for phones. support for desktop wallpapers are on their way') 
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
      
      
    # bot info and other stuff
    
        
    if message.content == '?submit':
      await message.channel.send('submit stuff here: https://forms.gle/jz4bemZKgjj4d1oWA')
          
    if message.content == '?credits':
      await message.channel.send('here are all of the cool people who gave ideas to the bot: https://github.com/julianagar/Poop-Bot/blob/main/README.md')

    if message.content == '?website':
      await message.channel.send('https://julianagar.carrd.co/#poop-bot')

    if message.content == '?server':
      await message.channel.send('https://discord.gg/bq6ZuHVaHV')
      
    if message.content == '?changelog':
      await message.channel.send('view the changelog here: https://github.com/julianagar/Poop-Bot/blob/main/changelog.md')
        
# more bot running stuff 
      
@bot.event
async def on_message():
    print(message.content)
			
bot.run(token)
