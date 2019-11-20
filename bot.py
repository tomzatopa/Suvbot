import os
import random
import discord
from dotenv import load_dotenv
from discord.ext import commands

bot = commands.Bot(command_prefix='!')
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

@bot.event
async def on_ready():
    akt=random.randrange(1,4)
    if akt==1:
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching,name='tvojí nahou mámu'))
    elif akt==2:
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening,name='tvojí mámu sténat'))
    else:
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing,name='si s tvojí mámou'))


#vyber random radku z filu - Ehrendil
def rand_line(soubor):
    x = random.choice(list(open(soubor,encoding='utf-8')))
    return x

@bot.command(name='leaveguld', help='!leaveguld osoba1 osoba2')
async def leaveguld(ctx, arg1, arg2):
    osoba1 = str(arg1)
    osoba2 = str(arg2)
    if osoba2.endswith('a') or osoba2.endswith('u'):
        osoba2=osoba2[:-1]+'o'
    elif osoba2.endswith('ec'):
        osoba2=osoba2[:-2]+'če'
    elif osoba2.endswith('c'):
        osoba2=osoba2[:-1]+'če'
    elif osoba2.endswith('ek'):
        osoba2=osoba2[:-2]+'ku'
    elif osoba2.endswith('s') or osoba2.endswith('š') or osoba2.endswith('x') or osoba2.endswith('j')  or osoba2.endswith('č') or osoba2.endswith('ř'):
        osoba2+='i'
    elif osoba2.endswith('g') or osoba2.endswith('h') or osoba2.endswith('k') or osoba2.endswith('q'):
        osoba2+='u'
    elif osoba2.endswith('i') or osoba2.endswith('í') or osoba2.endswith('e') or osoba2.endswith('é') or osoba2.endswith('o') or osoba2.endswith('y') or osoba2.endswith('á'):
        osoba2=osoba2
    else:
        osoba2+='e'
    pridJm = str(rand_line('pridJm.txt')).rstrip()
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
        + ' a ' + pridJm \
        + ' ' + nadSecond \
        + ', který ' + os1 \
        + '. Hraju to už '+str(random.randrange(5,51)) \
        +' let a prošel jsem už '+str(random.randrange(5,21)) \
        +' guild a s takovým ' + nadS \
        + ' jako je '+osoba1+' jsem se ještě nesetkal. Doufám, že v příštím tieru ' + guilda \
        + '. Strčte si vaší guildu ' + misto \
        + ', jdu mít '+str(random.randrange(1,51)) \
        +' parsy jinam! A '+osoba2+' ty ' + pridJm \
        + ' ' + nadTy \
        + ' se taky můžeš ' + os2 \
        + ' ty ' + nadLast+ '!'
    await ctx.send(leave)

@leaveguld.error
async def info_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Je potřeba dodat jmena lidi: osoba1 osoba2')

bot.run(TOKEN)
