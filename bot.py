import os
import random
import discord
from dotenv import load_dotenv
from discord.ext import commands

bot = commands.Bot(command_prefix='!')
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

#vyber random radku z filu - Ehrendil
def rand_line(soubor):
    x = random.choice(list(open(soubor,encoding='utf-8'))) 
    return x

@bot.command(name='leaveguld', help='!leaveguld osoba1 osoba2')
async def leaveguld(ctx, arg1, arg2):
    osoba1 = str(arg1)
    osoba2 = str(arg2)
    pridjm = str(rand_line('pridjm.txt')).rstrip()
    nad = str(rand_line('nad.txt')).rstrip()
    nade = str(rand_line('nade.txt')).rstrip()
    nade2 = str(rand_line('nade2.txt')).rstrip()
    nadm = str(rand_line('nadm.txt')).rstrip()
    misto = str(rand_line('misto.txt')).rstrip()
    lesi = str(rand_line('lesi.txt')).rstrip()
    elgee = str(rand_line('elgee.txt')).rstrip()
    guilda = str(rand_line('guilda.txt')).rstrip()


    leave='Ahoj, rozhodl jsem se leavnout guildu, protože '+osoba1+' je ' + nad \
        + ' a ' + pridjm \
        + ' ' + nad \
        + ', který ' + lesi \
        + '. Hraju to už '+str(random.randrange(5,51)) \
        +' let a prošel jsem už '+str(random.randrange(5,21)) \
        +' guild a s takovým ' + nadm \
        + ' jako je '+osoba1+' jsem se ještě nesetkal. Doufám, že v příštím tieru ' + guilda \
        + '. Strčte si vaší guildu do ' + misto \
        + ', jdu mít '+str(random.randrange(1,51)) \
        +' parsy jinam! A '+osoba2+' ty ' + pridjm \
        + ' ' + nade \
        + ' se taky můžeš ' + elgee \
        + ' ty ' + nade2+ '!'
    await ctx.send(leave)

@leaveguld.error
async def info_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Je potřeba dodat jmena lidi: osoba1 osoba2')

bot.run(TOKEN)

