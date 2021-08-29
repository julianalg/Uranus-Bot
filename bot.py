import os
import time
import discord
from random import randint
from random import seed
import random
from discord.ext import commands
from discord.ext.commands import CommandNotFound

# list dependencies
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
uselessWebsites = ['https://www.hackertyper.com/', 'https://onefishstudio.net/ucg', 'https://pointerpointer.com/', 'https://www.boredbutton.com/', 'https://smashthewalls.com/', 'https://mondrianandme.com', 'https://thatsthefinger.com', 'https://puginarug.com', 'https://cant-not-tweet-this.com', 'https://alwaysjudgeabookbyitscover.com',  'https://www.mapcrunch.com/', 'https://www.window-swap.com/Window', 'https://screamintothevoid.com/', 'https://archive.org/details/msdos_Oregon_Trail_The_1990', 'https://www.thesolaropposites.com/lessonalyzer/', 'https://nestflix.fun']
# cute animal
cuteAnimal = ['https://imgur.com/t/aww/EsVNl3y', 'https://imgur.com/t/aww/OYSoXGx', 'https://imgur.com/t/aww/EKKWq5Q', 'https://imgur.com/t/aww/hBkTtOT', 'https://imgur.com/t/aww/GWvmwBy', 'https://imgur.com/t/aww/cYOAzQG', 'https://imgur.com/t/aww/PYO3jHw', 'https://imgur.com/t/aww/onaQY4K', 'https://imgur.com/t/aww/9JqesLH', 'https://www.reddit.com/r/aww/comments/oyoksi/the_determined_doggo', 'https://www.reddit.com/r/aww/comments/oyjgtp/thats_too_cute_i_will_die_from_cuteness/', 'https://imgur.com/t/petshow2021/oVbdYj9', 'https://imgur.com/t/petshow2021/0ii4FJ5', 'https://imgur.com/t/petshow2021/NmBuPAe', 'https://imgur.com/t/petshow2021/GLKbglZ']
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
rnbAlbums = ['Ctrl: https://bit.ly/3fGqPan', "When It's All Said And Done... Take Time: https://bit.ly/3zX5il6", 'After Hours: https://open.spotify.com/album/4yP0hdKOZPNshxUOjY0cZj?autoplay=true', 'Blond: https://open.spotify.com/album/3mH6qwIy9crq0I9YQbOuDf?autoplay=true']
kpopAlbums = ['Regular-Irregular: https://bit.ly/3Arl6Nl', 'THE OTHER SIDE OF THE MOON: https://bit.ly/3fQkitx', 'She Is: https://bit.ly/2U4adS6', 'The Perfect Red Velvet: https://bit.ly/3xxvm4H', 'Feel Special: https://bit.ly/3lIyPvc', 'Remember Us: Youth Part 2: https://bit.ly/37sfCFP', 'FEVER: https://bit.ly/3jHujdE', 'Zero: Fever Part.1: https://music.youtube.com/playlist?list=OLAK5uy_mk8hALS6QQbsjFhXANAoT85cAP9wdMJfE&feature=gws_kp_album&feature=gws_kp_artist', "Don't Call Me: https://music.youtube.com/playlist?list=OLAK5uy_kPiZ5ftT-ifzoFmoYroH_WffozSAFm_eU&feature=gws_kp_album&feature=gws_kp_artist", 'BORDER: CARNIVAL: https://music.youtube.com/playlist?list=OLAK5uy_nxPYOoHgmm1iR-bs39vZNJa3rxr-zhCx8&feature=gws_kp_album&feature=gws_kp_artist', 'Teen, Age: https://music.youtube.com/playlist?list=OLAK5uy_k3LRlcnKy4EcWk1Joc5lKOSlP2-WYbrwY&feature=gws_kp_album&feature=gws_kp_artist', 'NCT-RESONACE,Pt.2 (The 2nd Album): https://music.youtube.com/playlist?list=OLAK5uy_kbSg7V8UK4ZDzPaGRfVJI7rsDP2LQR7Zg&feature=gws_kp_album&feature=gws_kp_artist', "Ex'Act: https://music.youtube.com/playlist?list=OLAK5uy_n0yuTw9cb1INJlnZ9ydDV-zRvbPi_iH4w&feature=gws_kp_album&feature=gws_kp_artist", 'Hello Future: https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwivoPPCmaXyAhUSDzQIHTS0AKQQyCkwAHoECAIQAw&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DQPUjV7epJqE&usg=AOvVaw3t4kqPEwDm6PSpGbjC_t6y', 'instinct:  https://music.youtube.com/watch?v=aOuK3WUffXc&feature=gws_kp_track', 'QUERENCIA: https://music.youtube.com/playlist?list=OLAK5uy_lt7o5tYOgtUF8098LlJxwWoMaHRqwxfDg&feature=gws_kp_album&feature=gws_kp_artist', '130 mood: TRBL: https://music.youtube.com/playlist?list=OLAK5uy_nF3pW60THeSSuC-IdFfQh2wautFpKWRSo&feature=gws_kp_album&feature=gws_kp_artist', 'IS ANYBODY OUT THERE?: https://music.youtube.com/playlist?list=OLAK5uy_nY9vJNOiFsuUe4vsinqpgy3lnk8ykB7lE&feature=gws_kp_album&feature=gws_kp_artist']
comedyAlbums = ['Bo Burnham: Inside (The Songs): https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjgmMmx9KbyAhUS3p4KHY8ZBO0QFnoECAMQAQ&url=https%3A%2F%2Fopen.spotify.com%2Falbum%2F1e5OlE0EY5fucq6GIU1xi3&usg=AOvVaw3BqZQ22RGQIRg1cWtonehq3v', 'New In Town: https://open.spotify.com/album/3ZvULmHESu5iaRNSAIewQ0?autoplay=true']
# jokes 
jokes = ['look in the mirrror', 'what did the fridge say to the toaster? ||nothing at all, they cant talk lmfao||', 'how do you put an elephant in the fridge? || you open the door, put the elephant in, and close the door||']
# cs asking
csResponseQuestions = ['ask L instead', 'therapy is always an option', 'maybe if you stanned nct you’d find the answer', 'ask @CarlSuburbs on twitter', 'yes, 100%, i can’t stress this enough, absolutely, for sure, no doubt', 'stop. baby don’t stop.', 'There is no such thing as a coincidence. The fact that you have asked me this means that we are energetically and spiritually aligned.']
# tasks
tasks = ['clean bedroom', 'clear out email inbox', 're-do phone home screen', 'change your wallpapers (tip: ?wallpaper)', 'go on a walk or stretch', 'say good morning/afternoon/evening/night or check up on a friend', "sort and sell things you don't need", "contribute ideas to the bot (?submit)"]
# tips
tips = ['?rate: have the bot rate anything', '?cock: :zany_face:', '?dance: dancing cat', '?ask carl: ask carl suburbs something', '?wp: wallpaper', '?recommendations: recommendations', '? void shout: shout random messages into the void', '?void pull: pull random messages out of the void', '?cute: cute animals', '?among us: im sorry', "?useless: useless website", "?task: a productive task todo"]
# boot messages
bootMessages = ['im back bitches', 'sorry i shit myself im back now', 'jaymes took me down again sorry', "my downtime was literally everyone's but julian's fault."]

recommendationAna = 0
wallpaperAna = 0
toneIntAna = 0
webAna = 0

def analytics():
  print('recommendations called: ' + recommendationAna)
  print('wallpapers called: ' + wallpaperAna)
  print('tone indicators called: ' + toneIntAna)
  print('bot info called: ' + webAna)

# shouts 
shouts = []

# bot running stuff 

bot = commands.Bot(command_prefix='?')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        return
    raise error


@bot.event
async def on_ready():
  print("poop bot is now online")
  channel = bot.get_channel(872713496675110973)
  await channel.send(random.choice(bootMessages))

# commands 
@bot.listen()
async def on_message(message):
    if message.author == bot.user:
        return
    if message.author.bot: return # so the bot doesnt reply to itself 
  
    if message.content == '?test':
      await message.channel.send('test message!')

    if message.content.startswith('?rate'): 
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
      await message.channel.send(random.choice(csResponseQuestions))
        
    if message.content == '?playlist':
      await message.channel.send(random.choice(playlists))
  
    if message.content == '?among us': 
      await message.channel.send(random.choice(amongUs))
    
    if message.content == '?useless':
      await message.channel.send(random.choice(uselessWebsites))
  
    if message.content == '?cute':
      await message.channel.send(random.choice(cuteAnimal))
  
    if message.content == '?jokes':
      await message.channel.send(random.choice(jokes))
      
    if message.content == '?task':
      await message.channel.send(random.choice(tasks))
     
    if message.content.startswith("?number rate"):
      if message.content == "?number rate adam":
        await message.channel.send('101/100')
      else:
        await message.channel.send(str(randint(0,100)) + '/100')

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
    
    if message.content == '?wallpaper': 
      await message.channel.send('all of these wallpapers are intended for phones. support for desktop wallpapers are on their way') 
      await message.channel.send('avaliable categories: anime, apple, landscape, cityscape, space, color, pride or illustration?')
      await message.channel.send('do "?wp (then the catergory you want)"')
      wallpaperAna = wallpaperAna + 1
        
    if message.content == '?wp': # same thing but different trigger, i dont know if or commands works with discord.py
      await message.channel.send('all of these wallpapers are intended for phones. support for desktop wallpapers are on their way') 
      await message.channel.send('avaliable categories: anime, apple, landscape, cityscape, space, color, pride or illustration?')
      await message.channel.send('do "?wp (then the catergory you want)"')
      wallpaperAna = wallpaperAna + 1
        
    if message.content == '?wp landscape':
      await message.channel.send(random.choice(landscapeWallpaper))
      wallpaperAna = wallpaperAna + 1

    if message.content == '?wp apple': 
      await message.channel.send(random.choice(appleWallpaper))
      wallpaperAna = wallpaperAna + 1

    if message.content == '?wp anime':
      await message.channel.send(random.choice(animeWallpaper))
      wallpaperAna = wallpaperAna + 1

    if message.content == '?wp cityscape':
      await message.channel.send(random.choice(cityWallpper))
      wallpaperAna = wallpaperAna + 1

    if message.content == '?wp space':
      await message.channel.send(random.choice(spaceWallpaper))
      wallpaperAna = wallpaperAna + 1

    if message.content == '?wp color':
      await message.channel.send(random.choice(colorWallpaper))
      wallpaperAna = wallpaperAna + 1

    if message.content == '?wp pride':
      await message.channel.send(random.choice(prideWallpaper))
      wallpaperAna = wallpaperAna + 1
        
    if message.content == '?wp illustration':
      await message.channel.send(random.choice(illustrationWallpaper))
      wallpaperAna = wallpaperAna + 1
        
    # recommendation cluster fuck
    
    if message.content == '?recommendations':
      await message.channel.send('what would you like: a movie, tv show, video game, or music artist?')
      await message.channel.send('do ?(catergory)')
      recommendationAna = recommendationAna + 1
        
    if message.content == '?movie':
      await message.channel.send('which would you like: romance, drama, or animated?')
      await message.channel.send('do ?movie (catergory)')
      recommendationAna = recommendationAna + 1
            
    if message.content == '?movie romance':
      await message.channel.send(random.choice(romanceMovies))
      recommendationAna = recommendationAna + 1
        
    if message.content == '?movie animated':
      await message.channel.send(random.choice(animatedMovies))
      recommendationAna = recommendationAna + 1
              
    if message.content == '?tv show':
      await message.channel.send('which would you like: romance, comedy, drama, anime')
      await message.channel.send('do ?tv (catergory)')
      recommendationAna = recommendationAna + 1
          
    if message.content == '?tv comedy':
      await message.channel.send(random.choice(comedyShows))
      recommendationAna = recommendationAna + 1
            
    if message.content == '?tv cartoon': 
        await message.channel.send(random.choice(cartoonShows))
        recommendationAna = recommendationAna + 1

    if message.content == '?tv anime':
      await message.channel.send(random.choice(animeShows))
      recommendationAna = recommendationAna + 1

    if message.content == '?tv drama':
      await message.channel.send(random.choice(dramaShows))
      recommendationAna = recommendationAna + 1

    if message.content == '?artist':
      await message.channel.send('which would you like: rock or pop?')
      await message.channel.send('do ?artist (catergory)')
      recommendationAna = recommendationAna + 1

    if message.content == '?artist rock':
      await message.channel.send(random.choice(rockMusic))
      recommendationAna = recommendationAna + 1
        
    if message.content == '?artist alternative':
      await message.channel.send(random.choice(alternativeMuic))
      recommendationAna = recommendationAna + 1
          
    if message.content == '?album':
      await message.channel.send('which would you like: pop, indie, kpop, comedy, or R&B?')
      await message.channel.send('do ?album (catergory)')
      recommendationAna = recommendationAna + 1
        
    if message.content == '?album pop':
      await message.channel.send(random.choice(popAlbums))
      recommendationAna = recommendationAna + 1
          
    if message.content == '?album indie':
      await message.channel.send(random.choice(indieAlbums))
      recommendationAna = recommendationAna + 1
    
    if message.content == '?album kpop':
      await message.channel.send(random.choice(kpopAlbums))
      recommendationAna = recommendationAna + 1
    
    if message.content == '?album comedy':
      await message.channel.send(random.choice(comedyAlbums))
      recommendationAna = recommendationAna + 1
      
    if message.content == '?album R&B':
      await message.channel.send(random.choice(rnbAlbums))
      recommendationAna = recommendationAna + 1

    # tone indicators

    if message.content == '?tone':
      embedVar = discord.Embed(title="tone indicators:", description="usage: ?tone {tone indicator}", color=0x00ff00)
      await message.channel.send(embed=embedVar)
      toneIntAna = toneIntAna + 1

    if message.content == '?tone j':
      embedVar = discord.Embed(title="/j:", description="joking", color=0x00ff00)
      await message.channel.send(embed=embedVar)
      toneIntAna = toneIntAna + 1

    if message.content == '?tone hj':
      embedVar = discord.Embed(title="/hj:", description="half-joking", color=0x00ff00)
      await message.channel.send(embed=embedVar)
      toneIntAna = toneIntAna + 1

    if message.content == '?tone s':
      embedVar = discord.Embed(title="/s:", description="sarcastic", color=0x00ff00)
      await message.channel.send(embed=embedVar)
      toneIntAna = toneIntAna + 1

    if message.content == '?tone gen':
      embedVar = discord.Embed(title="/gen or /g:", description="genuine", color=0x00ff00)
      await message.channel.send(embed=embedVar)
      toneIntAna = toneIntAna + 1

    if message.content == '?tone g':
      embedVar = discord.Embed(title="/gen or /g:", description="geniune", color=0x00ff00)
      await message.channel.send(embed=embedVar)
      toneIntAna = toneIntAna + 1

    if message.content == '?tone srs':
      embedVar = discord.Embed(title="/srs:", description="serious", color=0x00ff00)
      await message.channel.send(embed=embedVar)
      toneIntAna = toneIntAna + 1

    if message.content == '?tone nsrs':
      embedVar = discord.Embed(title="/nsrs:", description="not serious", color=0x00ff00)
      await message.channel.send(embed=embedVar)
      toneIntAna = toneIntAna + 1

    if message.content == '?tone pos':
      embedVar = discord.Embed(title="/pos or /pc:", description="positive connotation", color=0x00ff00)
      await message.channel.send(embed=embedVar)
      toneIntAna = toneIntAna + 1

    if message.content == '?tone pc':
      embedVar = discord.Embed(title="/pos or /pc:", description="positive connotation", color=0x00ff00)
      await message.channel.send(embed=embedVar)
      toneIntAna = toneIntAna + 1

    if message.content == '?tone neu':
      embedVar = discord.Embed(title="/neu:", description="neutral connotation", color=0x00ff00)
      await message.channel.send(embed=embedVar)
      toneIntAna = toneIntAna + 1

    if message.content == '?tone neg':
      embedVar = discord.Embed(title="/neg or /nc:", description="negative connotation", color=0x00ff00)
      await message.channel.send(embed=embedVar)
      toneIntAna = toneIntAna + 1

    if message.content == '?tone nc':
      embedVar = discord.Embed(title="/neg or /nc:", description="negative connotation", color=0x00ff00)
      await message.channel.send(embed=embedVar)
      toneIntAna = toneIntAna + 1

    if message.content == '?tone p':
      embedVar = discord.Embed(title="/p:", description="platonic", color=0x00ff00)
      await message.channel.send(embed=embedVar)
      toneIntAna = toneIntAna + 1

    if message.content == '?tone r':
      embedVar = discord.Embed(title="/r:", description="romantic", color=0x00ff00)
      await message.channel.send(embed=embedVar)
      toneIntAna = toneIntAna + 1

    if message.content == '?tone c':
      embedVar = discord.Embed(title="/c:", description="copypasta", color=0x00ff00)
      await message.channel.send(embed=embedVar)
      toneIntAna = toneIntAna + 1

    if message.content == '?tone l':
      embedVar = discord.Embed(title="/l or /ly:", description="lyrics", color=0x00ff00)
      await message.channel.send(embed=embedVar)
      toneIntAna = toneIntAna + 1

    if message.content == '?tone ly':
      embedVar = discord.Embed(title="/l or /ly:", description="lyrics", color=0x00ff00)
      await message.channel.send(embed=embedVar)
      toneIntAna = toneIntAna + 1

    if message.content == '?tone lh':
      embedVar = discord.Embed(title="/lh:", description="light-hearted", color=0x00ff00)
      await message.channel.send(embed=embedVar)
      toneIntAna = toneIntAna + 1

    if message.content == '?tone nm':
      embedVar = discord.Embed(title="/nm:", description="not mad", color=0x00ff00)
      await message.channel.send(embed=embedVar)
      toneIntAna = toneIntAna + 1

    if message.content == '?tone lu':
      embedVar = discord.Embed(title="/lu:", description="a little-upset", color=0x00ff00)
      await message.channel.send(embed=embedVar)
      toneIntAna = toneIntAna + 1

    if message.content == '?tone nbh':
      embedVar = discord.Embed(title="/nbh", description="for when you're vagueposting or venting, but it's directed at nobody here", color=0x00ff00)
      await message.channel.send(embed=embedVar)
      toneIntAna = toneIntAna + 1

    if message.content == '?tone nbh':
      embedVar = discord.Embed(title="/nbh", description="for when you're vagueposting or venting, but it's directed at nobody here", color=0x00ff00)
      await message.channel.send(embed=embedVar)
      toneIntAna = toneIntAna + 1

    if message.content == '?tone sx':
      embedVar = discord.Embed(title="/sx or /x", description="sexual intent")
      await message.channel.send(embed=embedVar)
      toneIntAna = toneIntAna + 1
    
    if message.content == '?tone x':
      embedVar = discord.Embed(title="/sx or x", description="sexual intent")
      await message.channel.send(embed=embedVar)
      toneIntAna = toneIntAna + 1

    if message.content == '?tone nsx':
      embedVar = discord.Embed(title="/nsx or /nx", description="non-sexual intent")
      await message.channel.send(embed=embedVar)
      toneIntAna = toneIntAna + 1

    if message.content == '?tone nx':
      embedVar = discord.Embed(title="/nsx or /nx", description="non-sexual intent")
      await message.channel.send(embed=embedVar)
      toneIntAna = toneIntAna + 1

    if message.content == '?tone rh':
      embedVar = discord.Embed(title="/rh or /rt", description="rhetorical question")
      await message.channel.send(embed=embedVar)
      toneIntAna = toneIntAna + 1

    if message.content == '?tone rt':
      embedVar = discord.Embed(title="/rh or /rt", description="rhetorical question")
      await message.channel.send(embed=embedVar)
      toneIntAna = toneIntAna + 1

    if message.content == '?tone t':
      embedVar = discord.Embed(title="/t", description="teasing")
      await message.channel.send(embed=embedVar)
      toneIntAna = toneIntAna + 1
      
    if message.content == '?tone ij':
      embedVar = discord.Embed(title="/ij", description="inside joke")
      await message.channel.send(embed=embedVar)
      toneIntAna = toneIntAna + 1

    if message.content == '?tone m':
      embedVar = discord.Embed(title="/m", description="metaphorically")
      await message.channel.send(embed=embedVar)
      toneIntAna = toneIntAna + 1

    if message.content == '?tone li':
      embedVar = discord.Embed(title="/li", description="literally")
      await message.channel.send(embed=embedVar)
      toneIntAna = toneIntAna + 1

    if message.content == '?tone hyp':
      embedVar = discord.Embed(title="/hyperbole", description="hyperbole")
      await message.channel.send(embed=embedVar)
      toneIntAna = toneIntAna + 1

    if message.content == '?tone f':
      embedVar = discord.Embed(title="/f", description="fake")
      await message.channel.send(embed=embedVar)
      toneIntAna = toneIntAna + 1

    if message.content == '?tone th':
      embedVar = discord.Embed(title="/th", description="threat")
      await message.channel.send(embed=embedVar)
      toneIntAna = toneIntAna + 1

    if message.content == '?tone /cb':
      embedVar = discord.Embed(title="/cb", description="clickbait")
      await message.channel.send(embed=embedVar)
      toneIntAna = toneIntAna + 1

    # bot info and other stuff

    if message.content == '?credits':
      await message.channel.send('here are all of the cool people who gave ideas to the bot: https://github.com/julianagar/Poop-Bot/blob/main/README.md')
      webAna = webAna + 1

    if message.content == '?website':
      await message.channel.send('https://julianagar.carrd.co/#poop-bot')
      webAna = webAna + 1

    if message.content == '?server':
      await message.channel.send('https://discord.gg/bq6ZuHVaHV')
      webAna = webAna + 1

    if message.content == '?changelog':
      await message.channel.send('view the changelog here: https://github.com/julianagar/Poop-Bot/blob/main/changelog.md')
      webAna = webAna + 1
      
    if message.content == '?tip':
      await message.channel.send(random.choice(tips))
      webAna = webAna + 1

# analytics

time.sleep(1800)
analytics()

# bot running stuff
  
async def on_message():
    print(message.content)
			
bot.run('token')
