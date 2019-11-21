import os
import os.path
from os import path
import random
import discord
import asyncio
from dotenv import load_dotenv
from discord.ext import commands

bot = commands.Bot(command_prefix='!')
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
MAINTAINER = os.getenv('MAINTAINER1')

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
    elif text.endswith('s') or text.endswith('š') or text.endswith('x') or text.endswith('j')  or text.endswith('č') or text.endswith('ř'):
        sklon+='i'
    elif text.endswith('g') or text.endswith('h') or text.endswith('k') or text.endswith('q'):
        sklon+='u'
    elif text.endswith('i') or text.endswith('í') or text.endswith('e') or text.endswith('é') or text.endswith('o') or text.endswith('y') or text.endswith('á'):
        sklon=text
    else:
        sklon+='e'
    return sklon

@bot.command(name='leaveguld', help='!leaveguld osoba1 osoba2')
async def leaveguld(ctx, arg1, arg2):
    osoba1 = str(arg1)
    osoba2 = sklon_5p(str(arg2))
    pridJm1 = str(rand_line('pridJm.txt')).rstrip()
    pridJm2 = str(rand_line('pridJm.txt')).rstrip()
    while pridJm1==pridJm2:
        pridJm2 = str(rand_line('pridJm.txt')).rstrip()
    nadFirst = str(rand_line('nadavky.txt')).rstrip()
    nadSecond = str(rand_line('nadavky.txt')).rstrip()
    while nadFirst==nadSecond:
        nadSecond = str(rand_line('nadavky.txt')).rstrip()
    nadTy = str(rand_line('nadavkyTy.txt')).rstrip()
    nadLast = str(rand_line('nadavkyLast.txt')).rstrip()
    while nadTy==nadLast:
        nadLast = str(rand_line('nadavkyLast.txt')).rstrip()
    nadS = str(rand_line('nadavkyS.txt')).rstrip()
    misto = str(rand_line('misto.txt')).rstrip()
    os1 = str(rand_line('osoba1.txt')).rstrip()
    os2 = str(rand_line('osoba2.txt')).rstrip()
    guilda = str(rand_line('guilda.txt')).rstrip()

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

@bot.command(name='insult', help='!insult osoba')
async def insult(ctx,arg1):
    nekdo = sklon_5p(str(arg1))
    pridJm1 = str(rand_line('pridJm.txt')).rstrip()
    pridJm2 = str(rand_line('pridJm.txt')).rstrip()
    while pridJm2==pridJm1:
        pridJm2 = str(rand_line('pridJm.txt')).rstrip()
    nad = str(rand_line('nadavkyTy.txt')).rstrip()
    ins= nekdo + ', ty '+ pridJm1 +' '+ pridJm2 +' '+ nad+'!'
    await ctx.send(ins)

@insult.error
async def info_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Je potřeba zadat jméno člověka, kterého chcete urazit.')


@bot.command(name='iaosound', help='!iaosound zeddone-honk')
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

######update bota skrz discord
@bot.command(name='updatebot', help='!updatebot omezeno pro urcite uzivatele')
async def updatebot(ctx):
    #username = str(ctx.message.author.name)
    #userid = str(ctx.message.author.id)
    #userdiscriminator = str(ctx.message.author.discriminator)
    #final = 'name = ' + username + ', userid = ' + userid + ', discriminator = ' + userdiscriminator 
    #await ctx.send(final)
    sendinguserid = ctx.message.author.id
    if sendinguserid == MAINTAINER:
        await ctx.send('jupí', delete_after=5)
    else:
        await ctx.send('nope', delete_after=5)


@bot.command(name='slabikar', help='!slabikar')
async def slabikar(ctx):
    ins = 'https://www.youtube.com/watch?v=u1HMzYSZGIo'
    await ctx.send(ins)

bot.run(TOKEN)
