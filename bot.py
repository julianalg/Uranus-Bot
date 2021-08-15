import os
import discord
from random import randint
from random import seed
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
popAlbums = ['Happier than Ever: https://bit.ly/3yjMdJv', 'Planet Her: https://bit.ly/3jeaA5h', 'Hot Pink: https://music.youtube.com/playlist?list=OLAK5uy_nN6ToczJSrgaKwaWT3jyvNgedNcs2D94Y&feature=gws_kp_album&feature=gws_kp_artist', 'SOUR: https://music.youtube.com/playlist?list=OLAK5uy_mRc9HLtU_4lp_-MKQNApIRiLwY0M6xoCA&feature=gws_kp_album&feature=gws_kp_artist', 'Blood Harmony: https://music.youtube.com/playlist?list=OLAK5uy_mb0tj-3a2sG_iILVI1LC1jejNJDkTbDeg&feature=gws_kp_album&feature=gws_kp_artist']
indieAlbums = ['Sling: https://bit.ly/3iksXpM', 'Jubilee: https://bit.ly/3jl9F34', 'Apricot Princess: https://music.youtube.com/playlist?list=OLAK5uy_n7pYtvKITUmxl51Y5Sv7IbU0mdxmskDw8&feature=gws_kp_album&feature=gws_kp_artist', 'Harmony House: https://music.youtube.com/playlist?list=OLAK5uy_nC-k8nCXlXiw_46lVDh5MpKEFs4E7ED_Q&feature=gws_kp_album&feature=gws_kp_artist']
rnbAlbums = ['Ctrl: https://bit.ly/3fGqPan', "When It's All Said And Done... Take Time: https://bit.ly/3zX5il6"]
kpopAlbums = ['Regular-Irregular: https://bit.ly/3Arl6Nl', 'THE OTHER SIDE OF THE MOON: https://bit.ly/3fQkitx', 'She Is: https://bit.ly/2U4adS6', 'The Perfect Red Velvet: https://bit.ly/3xxvm4H', 'Feel Special: https://bit.ly/3lIyPvc', 'Remember Us: Youth Part 2: https://bit.ly/37sfCFP', 'FEVER: https://bit.ly/3jHujdE', 'Zero: Fever Part.1: https://music.youtube.com/playlist?list=OLAK5uy_mk8hALS6QQbsjFhXANAoT85cAP9wdMJfE&feature=gws_kp_album&feature=gws_kp_artist', "Don't Call Me: https://music.youtube.com/playlist?list=OLAK5uy_kPiZ5ftT-ifzoFmoYroH_WffozSAFm_eU&feature=gws_kp_album&feature=gws_kp_artist", 'BORDER: CARNIVAL: https://music.youtube.com/playlist?list=OLAK5uy_nxPYOoHgmm1iR-bs39vZNJa3rxr-zhCx8&feature=gws_kp_album&feature=gws_kp_artist', 'Teen, Age: https://music.youtube.com/playlist?list=OLAK5uy_k3LRlcnKy4EcWk1Joc5lKOSlP2-WYbrwY&feature=gws_kp_album&feature=gws_kp_artist', 'NCT-RESONACE,Pt.2 (The 2nd Album): https://music.youtube.com/playlist?list=OLAK5uy_kbSg7V8UK4ZDzPaGRfVJI7rsDP2LQR7Zg&feature=gws_kp_album&feature=gws_kp_artist', "Ex'Act: https://music.youtube.com/playlist?list=OLAK5uy_n0yuTw9cb1INJlnZ9ydDV-zRvbPi_iH4w&feature=gws_kp_album&feature=gws_kp_artist", 'Hello Future: https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwivoPPCmaXyAhUSDzQIHTS0AKQQyCkwAHoECAIQAw&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DQPUjV7epJqE&usg=AOvVaw3t4kqPEwDm6PSpGbjC_t6y', 'instinct:  https://music.youtube.com/watch?v=aOuK3WUffXc&feature=gws_kp_track', 'QUERENCIA: https://music.youtube.com/playlist?list=OLAK5uy_lt7o5tYOgtUF8098LlJxwWoMaHRqwxfDg&feature=gws_kp_album&feature=gws_kp_artist', '130 mood: TRBL: https://music.youtube.com/playlist?list=OLAK5uy_nF3pW60THeSSuC-IdFfQh2wautFpKWRSo&feature=gws_kp_album&feature=gws_kp_artist', 'IS ANYBODY OUT THERE?: https://music.youtube.com/playlist?list=OLAK5uy_nY9vJNOiFsuUe4vsinqpgy3lnk8ykB7lE&feature=gws_kp_album&feature=gws_kp_artist']
comedyAlbums = ['Bo Burnham: Inside (The Songs): https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjgmMmx9KbyAhUS3p4KHY8ZBO0QFnoECAMQAQ&url=https%3A%2F%2Fopen.spotify.com%2Falbum%2F1e5OlE0EY5fucq6GIU1xi3&usg=AOvVaw3BqZQ22RGQIRg1cWTdhq3v', 'New In Town: https://open.spotify.com/album/3ZvULmHESu5iaRNSAIewQ0?autoplay=true']
# jokes 
jokes = ['look in the mirrror', 'what did the fridge say to the toaster? ||nothing at all, they cant talk lmfao||', 'how do you put an elephant in the fridge? || you open the door, put the elephant in, and close the door||']
# cs asking
csResponseQuestions = ['ask L instead', 'therapy is always an option', 'maybe if you stanned nct you’d find the answer', 'ask @CarlSuburbs on twitter', 'yes, 100%, i can’t stress this enough, absolutely, for sure, no doubt', 'stop. baby don’t stop.', 'There is no such thing as a coincidence. The fact that you have asked me this means that we are energetically and spiritually aligned.']
# tasks
tasks = ['clean bedroom', 'clear out email inbox', 're-do phone home screen', 'change your wallpapers (tip: ?wallpaper)', 'go on a walk or stretch', 'say good morning/afternoon/evening/night or check up on a friend', "sort and sell things you don't need", "contribute ideas to the bot (?submit)"]
# tips
tips = ['?rate: have the bot rate anything', '?cock: :zany_face:', '?dance: dancing cat', '?ask carl: ask carl suburbs something', '?wp: wallpaper', '?recommendations: recommendations']
# random number
cuzRandintDoesntWorkIHateThis = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100]


shouts = []

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
      await message.channel.send(random.choice(rateResponses))

    if message.content == '?fart':
      await message.channel.send('https://cdn.discordapp.com/attachments/872928261510934618/874451466394431488/wet-fart-meme-sound-effect-hd.mp4')

    if message.content.startswith('?cock'):
        await message.channel.send(':zany_face:')
      
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

     
    if message.content.startswith('?number rate'):
        if message.content == '?number rate adam':
          await message.channel.send('101/100')
        if message.content == "?number rate rina's love for jaymes":
          await message.channel.send('-1/100')
        else:
          rateNumber = randint(0, 100)
          await message.channel.send(str(rateNumber) + '/100')

    # void and repeating messages

    if message.content.startswith('?void shout'):
      shouts.append(message.content)
      await message.channel.send('done!')
      print(shouts)

    if message.content == '?void pull':
      await message.channel.send(random.choice(shouts))

    if message.content.startswith('?repeat after me'):
      await message.channel.send(message.content)

    # wallpaper
    
    
    if message.content == '?wallpaper': # from adam
        await message.channel.send('all of these wallpapers are intended for phones. support for desktop wallpapers are on their way') 
        await message.channel.send('avaliable categories: anime, apple, landscape, cityscape, space, color, pride or illustration?')
        await message.channel.send('do "?wp (then the catergory you want)"')
        
    if message.content == '?wp': # same thing but different trigger, i dont know if or commands works with discord.py
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
      await message.channel.send('which would you like: rock or pop?')
      await message.channel.send('do ?artist (catergory)')

    if message.content == '?artist rock':
      randomRock = random.choice(rockMusic)
      await message.channel.send(randomRock)
        
    if message.content == '?artist alternative':
      randomAlt = random.choice(alternativeMuic)
      await message.channel.send(randomAlt)
          
    if message.content == '?album':
      await message.channel.send('which would you like: pop, indie, kpop, comedy, or R&B?')
      await message.channel.send('do ?album (catergory)')
        
    if message.content == '?album pop':
      randomPop = random.choice(popAlbums)
      await message.channel.send(randomPop)
          
    if message.content == '?album indie':
      randomIndie = random.choice(indieAlbums)
      await message.channel.send(randomIndie)
    
    if message.content == '?album kpop':
      randomkPop = random.choice(kpopAlbums)
      await message.channel.send(randomkPop)
    
    if message.content == '?album comedy':
      await message.channel.send(random.choice(comedyAlbums))
      
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
      
    if message.content == '?tip':
      randomTip = random.choice(tips)
      await message.channel.send(randomTip)

# more bot running stuff 
      
@bot.event
async def on_message():
    print(message.content)
			
bot.run('ODcwNTA5OTAxNzU4MjAxODU3.YQNzhQ.LFhjeuCKIcqkV6UzXfoT8rLyZtI')
