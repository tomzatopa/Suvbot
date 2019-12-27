###############################
############IMPORTY############
###############################
import os
import os.path
import subprocess
import random
import discord
import asyncio
import requests
import json
import urllib.parse
from os import path
from dotenv import load_dotenv
from discord.ext import commands
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

###############################
###SETTINGS + IMPORT PROMENNYCH
###############################
bot = commands.Bot(command_prefix='!')
bot.remove_command('help')
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
MAINTAINER = [
    int(os.getenv('MAINTAINER1')),
    int(os.getenv('MAINTAINER2'))
    ]

###############################
###########EXTENSIONS##########
###############################
bot.load_extension('gamble')

###############################
##########BOT EVENTS###########
###############################
#nastaveni statusu
@bot.event
async def on_ready():
    akt=random.randrange(1,5)
    if akt==1:
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching,name='tvojí nahou mámu'))
    elif akt==2:
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching,name='porno s tvojí mámou'))
    elif akt==3:
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening,name='tvojí mámu sténat'))
    else:
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing,name='si s tvojí mámou'))

@bot.event
async def on_reaction_add(reaction, user):
    channel=reaction.message.channel
    for e in reaction.message.embeds:
        if e.footer.text=='Vyber jednu možnost.':
            if user!=bot.user:
                for r in reaction.message.reactions:
                    if r!=reaction:
                        await r.remove(user)

@bot.event
async def on_message(message):
    if (message.channel.id == 634683421616111616) and (message.author.id != 291891867703050240):
        print("test podminky")
        finalmsg = message.content
        print(finalmsg)
        message.channel = 634689737910648832
        print(message.channel)
        await message.send(finalmsg)
        print("poslano")
    else:
        await bot.process_commands(message)

###############################
########OBECNE FUNKCE##########
###############################
#vyber random radku z filu - Ehrendil
def rand_line(soubor):
    x = random.choice(list(open(soubor,encoding='utf-8')))
    return x
#sklonovani slov do 5. padu (osloveni)
def sklon_5p(text):
    sklon=text
    if text.startswith('<@') and text.endswith('>') : #pokud nekdo pouzije @ mention, tak se nesklonuje
        return sklon
    if text.endswith('a') or text.endswith('u'):
        sklon=text[:-1]+'o'
    elif text.endswith('ec'):
        sklon=text[:-2]+'če'
    elif text.endswith('c'):
        sklon=text[:-1]+'če'
    elif text.endswith('ek'):
        sklon=text[:-2]+'ku'
    elif text.endswith('ph'):
        sklon+='e'
    elif text.endswith('s') or text.endswith('š') or text.endswith('x') or text.endswith('j')  or text.endswith('č') or text.endswith('ř'):
        sklon+='i'
    elif text.endswith('g') or text.endswith('h') or text.endswith('k') or text.endswith('q'):
        sklon+='u'
    elif text.endswith('i') or text.endswith('í') or text.endswith('e') or text.endswith('é') or text.endswith('o') or text.endswith('y') or text.endswith('á'):
        sklon=text
    else:
        sklon+='e'
    return sklon

#sklonovani do slovenskeho osloveni
def sklon_slovak(text):
    sklon=text
    if text.endswith('a') or text.endswith('u') or text.endswith('c') or text.endswith('e'):
        sklon=text[:-1]+'ko'
    elif text.endswith('i') or text.endswith('í') or text.endswith('y') or text.endswith('ý'):
        sklon+='nko'
    elif text.endswith('ek'):
        sklon=text[:-2]+'ko'
    elif text.endswith('k'):
        sklon+='o'
    elif text.endswith('ko'):
        sklon=text
    else:
        sklon+='ko'
    return sklon

#removne extensions
def strip_extensions(seznam):
    soubory = []
    for soubor in seznam:
        soubor = os.path.splitext(soubor)[0]
        soubory.append(soubor)
    souboryfinal='\n'.join(soubory)
    return(souboryfinal)

###############################
#########BOT COMMANDS##########
###############################
####HELP COMMAND - IMPORTANTE
@bot.command(name='help')
async def help(ctx, *args):
    user = ctx.author
    helpmsg = discord.Embed(colour = discord.Colour.blue())
    helpmsg.set_author(name='SUVBOT HELPIK')
    helpmsg.add_field(name='__**!leaveguld osoba1 osoba2**__', value='Generátor souvětí, které se Vám může hodit při opouštění guildy s uražením dvou osob které Vás štvaly nejvíc.', inline=True)
    helpmsg.add_field(name='__**!insult osoba**__', value='Urazí osobu, funguje mention. ', inline=True)
    helpmsg.add_field(name='__**!iaosound vybrany-zvuk**__', value='Přehraje ve voice kanále vybraný zvuk. Pro list dostupných zvuků zadejte: !help iaosound', inline=True)
    helpmsg.add_field(name='__**!iaoimage vybrany-img**__', value='Pošle do kanálu vyberaný image. Pro list dostupných zvuků zadejte: !help iaoimage', inline=True)
    helpmsg.add_field(name='__**!iaomeme**__', value='Pošle do kanálu random meme!', inline=True)
    helpmsg.add_field(name='__**!slovak osoba**__', value='Pro naše bratry, nebojte se užít mention a jednoho z nich označit! ', inline=True)
    helpmsg.add_field(name='__**!slabikar**__', value='Bův ví co to je... :shrug:', inline=True)
    helpmsg.add_field(name='__**!gondorhelp kdo-neprisel-na-pomoc**__', value='Gondor help.... mluví za vše', inline=True)
    helpmsg.add_field(name='__**!inspire**__', value='Zobrazí náhodnou \"inspirational quote\"', inline=True)
    helpmsg.add_field(name='__**!recipe neco**__', value='Vyhledá recept', inline=True)

    helpmsg.add_field(name='__**!joke**__', value='Zobrazí náhodný dad joke', inline=True)
    helpmsg.add_field(name='__**!wolfram**__', value='Zobrazí odpověď na wolframalpha dotaz', inline=True)
    helpmsg.add_field(name='__**!office**__', value='Zobrazí náhodnou hlášku Michaela Scotta z The Office', inline=True)
    helpmsg.add_field(name='__**!cat**__', value='Zobrazí náhodný cat pic', inline=True)
    helpmsg.add_field(name='__**!poll typ otázka odpoved1 odpoved2 atd**__', value='Vytvoří hlasování. Pro více info: !help poll', inline=True)

    if args:
        helpmsg.clear_fields()
        if "iaoimage" in args:
            helpmsg.set_author(name='SUVBOT HELPIK')
            imagelist=os.listdir('./images')
            argumenty=strip_extensions(imagelist)
            helpmsg.add_field(name='__**!iaoimage vybrany-img**__', value='Pošle do kanálu vybraný image', inline=True)
            helpmsg.add_field(name='mozne image:', value=''+argumenty+'', inline=False)
            await user.send(embed=helpmsg)
        elif "iaosound" in args:
            helpmsg.set_author(name='SUVBOT HELPIK')
            soundlist=os.listdir('./sounds')
            argumenty=strip_extensions(soundlist)
            helpmsg.add_field(name='!__**iaosound vybrany-sound**__', value='Přehraje do kanálu vybraný zvuk', inline=True)
            helpmsg.add_field(name='mozne zvuky:', value=''+argumenty+'', inline=False)
            await user.send(embed=helpmsg)
        elif "poll" in args:
            helpmsg.set_author(name='SUVBOT HELPIK')
            helpmsg.add_field(name='!__**!poll typ otázka odpoved1 odpoved2 atd**__', value='Vytvoří hlasování.', inline=True)
            helpmsg.add_field(name='typ:', value='sc nebo mc:\nsc=single choice - dovolí každému zvolit pouze jednu odpověď\nmc=multiple choice - dovolí vybrat více odpovědí najednou', inline=False)
            helpmsg.add_field(name='otázka/odpovědi:', value='musí být v uvozovkách pokud mají být víceslovné', inline=False)
            helpmsg.add_field(name='odpovědi:', value='max 10\npokud se nenapíšou žádné možnosti, jsou odpovědi automaticky ANO/NE.', inline=False)
            await user.send(embed=helpmsg)
    else:
        await user.send("Help, který by pochopil snad každý!")
        await user.send(embed=helpmsg)

#################################
#leaveguld command
@bot.command(name='leaveguld')
async def leaveguld(ctx, arg1, arg2):
    osoba1 = str(arg1).capitalize()
    osoba2 = sklon_5p(str(arg2)).capitalize()
    os1 = str(rand_line('osoba1.txt')).rstrip()
    os2 = str(rand_line('osoba2.txt')).rstrip()
    misto = str(rand_line('misto.txt')).rstrip()
    guilda = str(rand_line('guilda.txt')).rstrip()
    nadS = str(rand_line('nadavkyS.txt')).rstrip()

    if random.randrange(1,5)==1:
        nadFirst = str(rand_line('nadavkyF.txt')).rstrip()
    else:
        nadFirst = str(rand_line('nadavky.txt')).rstrip()

    if random.randrange(1,5)==1:
        pridJm1 = str(rand_line('pridJmF.txt')).rstrip()
        nadSecond = str(rand_line('nadavkyF.txt')).rstrip()
        while nadFirst==nadSecond:
            nadSecond = str(rand_line('nadavkyF.txt')).rstrip()
    else:
        pridJm1 = str(rand_line('pridJm.txt')).rstrip()
        nadSecond = str(rand_line('nadavky.txt')).rstrip()
        while nadFirst==nadSecond:
            nadSecond = str(rand_line('nadavky.txt')).rstrip()

    if random.randrange(1,5)==1:
        nadTy = sklon_5p(str(rand_line('nadavkyF.txt')).rstrip())
        pridJm2 = str(rand_line('pridJmF.txt')).rstrip()
        while pridJm1==pridJm2:
            pridJm2 = str(rand_line('pridJmF.txt')).rstrip()
    else:
        nadTy = sklon_5p(str(rand_line('nadavky.txt')).rstrip())
        pridJm2 = str(rand_line('pridJm.txt')).rstrip()
        while pridJm1==pridJm2:
            pridJm2 = str(rand_line('pridJm.txt')).rstrip()

    if random.randrange(1,5)==1:
        nadLast = sklon_5p(str(rand_line('nadavkyF.txt')).rstrip())
        while nadTy==nadLast:
            nadLast = sklon_5p(str(rand_line('nadavkyF.txt')).rstrip())
    else:
        nadLast = sklon_5p(str(rand_line('nadavky.txt')).rstrip())
        while nadTy==nadLast:
            nadLast = sklon_5p(str(rand_line('nadavky.txt')).rstrip())

    leave='Ahoj, rozhodl jsem se leavnout guildu, protože '+osoba1+' je ' + nadFirst \
        + ' a ' + pridJm1 \
        + ' ' + nadSecond \
        + ', který ' + os1 \
        + '. Hraju to už '+str(random.randrange(5,51)) \
        +' let a prošel jsem už '+str(random.randrange(5,21)) \
        +' guild a s takovým ' + nadS \
        + ' jako je '+osoba1+' jsem se ještě nesetkal. Doufám, že v příštím tieru ' + guilda \
        + '. Strčte si vaší guildu ' + misto \
        + ', jdu mít '+str(random.randrange(1,51)) \
        +' parsy jinam! A '+osoba2+' ty ' + pridJm2 \
        + ' ' + nadTy \
        + ' se taky můžeš ' + os2 \
        + ' ty ' + nadLast+ '!'

    await ctx.send(leave)

@leaveguld.error
async def info_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Je potřeba zadat jména lidí: !leaveguld osoba1 osoba2')

#insult command
@bot.command(name='insult')
async def insult(ctx,arg1):
    nekdo = sklon_5p(str(arg1)).capitalize()
    print(nekdo)
    if (nekdo == "<@!170858681418776576>") or (nekdo == "<@!486946934473359360>") or (random.randrange(1,5)==1):
        pridJm1 = str(rand_line('pridJmF.txt')).rstrip()
        pridJm2 = str(rand_line('pridJmF.txt')).rstrip()
        while pridJm2==pridJm1:
            pridJm2 = str(rand_line('pridJmF.txt')).rstrip()
        nad = sklon_5p(str(rand_line('nadavkyF.txt')).rstrip())
    else:
        pridJm1 = str(rand_line('pridJm.txt')).rstrip()
        pridJm2 = str(rand_line('pridJm.txt')).rstrip()
        while pridJm2==pridJm1:
            pridJm2 = str(rand_line('pridJm.txt')).rstrip()
        nad = sklon_5p(str(rand_line('nadavky.txt')).rstrip())
    ins= nekdo + ', ty '+ pridJm1 +' '+ pridJm2 +' '+ nad+'!'
    await ctx.send(ins)

@insult.error
async def info_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Je potřeba zadat jméno člověka, kterého chcete urazit.')

#iaosound command
@bot.command(name='iaosound')
async def iaosound(ctx, arg1):
    channel = ctx.author.voice.channel
    #checkuje jestli existuje file ve slozce sounds/
    if path.exists('./sounds/'+arg1+'.mp3'):
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio('./sounds/'+arg1+'.mp3'), after=lambda e: print('prehravam', e))
        while vc.is_playing():
            await asyncio.sleep(1)
        await ctx.voice_client.disconnect()

@iaosound.error
async def info_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Je potřeba zadat zvuk k přehrání')

#iaoimage command
@bot.command(name='iaoimage')
async def iaoimage(ctx, arg1):
    if path.exists('./images/'+arg1+'.png'):
        await ctx.send(file=discord.File('./images/'+arg1+'.png'))
    elif path.exists('./images/'+arg1+'.jpg'):
        await ctx.send(file=discord.File('./images/'+arg1+'.jpg'))
    elif path.exists('./images/'+arg1+'.jpeg'):
        await ctx.send(file=discord.File('./images/'+arg1+'.jpeg'))

@iaoimage.error
async def info_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Je potreba zadat obrazek')

#iaomeme command - random image z iaoimage
@bot.command(name='iaomeme')
async def iaomeme(ctx):
    await ctx.send(file=discord.File('./memes/'+random.choice(os.listdir('./memes'))))

#slovak command
@bot.command(name='slovak')
async def slovak(ctx,arg):
    os = sklon_slovak(arg).capitalize()
    sl= 'Nie je ti kokotno '+ os +'?'
    await ctx.send(sl)
@slovak.error
async def info_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Je potřeba zadat jméno člověka.')

#update bota skrz discord
@bot.command(name='updatebot')
async def updatebot(ctx):
    sendinguserid = ctx.message.author.id
    if sendinguserid in MAINTAINER:
        await ctx.send('jdu se pullovat', delete_after=5)
        cmd = '/bin/git pull'
        proc = subprocess.Popen(cmd, shell=True,stdout=subprocess.PIPE)
        await ctx.send(proc.communicate()[0], delete_after=5)
        await asyncio.sleep(2)
        await ctx.send('jdu se zabit a znovu povstat', delete_after=5)
        cmd = '/bin/systemctl restart suvbot'
        proc = subprocess.Popen(cmd, shell=True,stdout=subprocess.PIPE)
    else:
        await ctx.send('nope', delete_after=5)

#slabikar command
@bot.command(name='slabikar')
async def slabikar(ctx):
    ins = 'https://www.youtube.com/watch?v=u1HMzYSZGIo'
    await ctx.send(ins)

#join channel command
@bot.command(name='join')
async def join(ctx):
    sendinguserid = ctx.message.author.id
    if sendinguserid in MAINTAINER:
        channel=ctx.author.voice.channel
        await channel.connect()
    else:
        await ctx.send('nope', delete_after=5)

#leave channel command
@bot.command(name='leave')
async def leave(ctx):
    sendinguserid = ctx.message.author.id
    if sendinguserid in MAINTAINER:
        if ctx.voice_client !=None :
            vc=ctx.voice_client
        else:
            channel=ctx.author.voice.channel
            vc=await channel.connect()
        await vc.disconnect()
    else:
        await ctx.send('nope', delete_after=5)

#gondorhelp command - na prani mistru lesiho a dapha
@bot.command(name='gondorhelp')
async def gondorhelp(ctx,arg):
    autor=sklon_5p(str(ctx.message.author.name))
    kdo=str(arg).capitalize()
    co1 = str(rand_line('gondor.txt')).rstrip()
    co2 = str(rand_line('gondor.txt')).rstrip()
    while co1==co2:
        co2 = str(rand_line('gondor.txt')).rstrip()
    gondor= kdo+'? Kde byl '+kdo+' když ' + co1 + '? Kde byl '+kdo+', když ' + co2 + '? Kde byl '+kdo[:2]+'… Ne, můj pane ' + autor + '. Jsme sami.'
    await ctx.send(gondor)
@gondorhelp.error
async def info_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Je potřeba zadat kdo neprisel na pomoc.')

#inspire command - inspirobot
@bot.command(name='inspire')
async def inspire(ctx):
    site= "https://inspirobot.me/api?generate=true"
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = Request(site,headers=hdr)
    page = urlopen(req).read()
    soup = BeautifulSoup(page,features="html.parser")
    embed = discord.Embed()
    embed.set_image(url=soup)
    await ctx.send(embed=embed)

#recipe command
@bot.command(name='recipe')
async def recipe(ctx,*args):
    a=" ".join(args)
    a=urllib.parse.quote_plus(a)
    response=requests.get('https://api.edamam.com/search?q='+a+'&app_id=29bd28f2&app_key=1abd93a6df57ca0164ee12b63b50dd98')
    dic=response.json()
    if dic['count'] != 0 :
        if dic['count'] < 10 :
            ran=random.randrange(0,dic['count'])
        else:
            ran=random.randrange(0,10)
        res=dic['hits'][ran]['recipe']['url']
        await ctx.send(res)
    else:
        await ctx.send("Žádný recept nenalezen.")

#fact command
@bot.command(name='fact')
async def fact(ctx):
    response=requests.get('https://uselessfacts.jsph.pl/random.json?language=en')
    dic=response.json()
    res=dic['text']
    await ctx.send(res)

#joke command
@bot.command(name='joke')
async def joke(ctx):
    response=requests.get('https://icanhazdadjoke.com/slack')
    dic=response.json()
    res=dic['attachments'][0]['text']
    await ctx.send(res)

#wolfram command
@bot.command(name='wolfram')
async def wolfram(ctx,*args):
    a=" ".join(args)
    a=a.replace('+', 'plus')
    a=urllib.parse.quote_plus(a)
    response=requests.get('http://api.wolframalpha.com/v1/query?input='+a+'&appid=JJPWTU-E5XKPQ5U9X&output=json')
    dic=response.json()
    embed = discord.Embed()
    for x in range(dic['queryresult']['numpods']):
        text=dic['queryresult']['pods'][x]['subpods'][0]['plaintext']
        if text != "":
            embed.add_field(name=dic['queryresult']['pods'][x]['title'], value=text, inline=False)
        embed.set_image(url=dic['queryresult']['pods'][x]['subpods'][0]['img']['src'])
    await ctx.send(embed=embed)

#office command
@bot.command(name='office')
async def office(ctx):
    response=requests.get('https://michael-scott-quotes.herokuapp.com/quote')
    dic=response.json()
    res=dic['quote']
    await ctx.send('\"'+res+'\"')

#poll command
@bot.command(name='poll')
async def poll(ctx,type,question,*options: str):
    if type !='sc' and type !='mc':
        await ctx.send('Je třeba zadat typ pollu (sc/mc).')
        return
    if len(options) > 10:
        await ctx.send('Poll může mít maximálně 10 možností odpovědi.')
        return
    if len(options) == 0:
        reactions = ['✅', '❌']
        options = ['ANO', 'NE']
    else:
        reactions = ['1️⃣', '2⃣', '3⃣', '4⃣', '5⃣', '6⃣', '7⃣', '8⃣', '9⃣', '🔟']
    description = []
    await ctx.send(":bar_chart: "+question)
    for x, option in enumerate(options):
        description += '\n {} {}'.format(reactions[x], option)
    embed = discord.Embed(description=''.join(description))
    react_message = await ctx.send(embed=embed)
    for reaction in reactions[:len(options)]:
        await react_message.add_reaction(reaction)
    #embed.set_footer(text='Poll ID: {}'.format(react_message.id))
    #await react_message.edit(embed=embed)
    if type =='sc':
        embed.set_footer(text='Vyber jednu možnost.')
        await react_message.edit(embed=embed)
    if type =='mc':
        embed.set_footer(text='Vyber jednu nebo více možností.')
        await react_message.edit(embed=embed)
#cat command
@bot.command(name='cat')
async def cat(ctx):
    response=requests.get('http://aws.random.cat/meow')
    dic=response.json()
    res=dic['file']
    embed = discord.Embed()
    embed.set_image(url=res)
    await ctx.send(embed=embed)

###############################
########IN CASE OF NEED########
###############################
#####get id
#@bot.command(name='getid')
#async def getid(ctx):
#    userid = str(ctx.message.author.id)
#    await ctx.send(userid, delete_after=5)

###BOT RUN
bot.run(TOKEN)
