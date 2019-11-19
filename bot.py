import os
import random
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

#vyber random radku z filu - Ehrendil
def rand_line(soubor):
    x = random.choice(list(open(soubor,encoding='utf-8'))) 
    return x

client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following server:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return
#zprehledneni promennych - Ehrendil
    pridjm = str(rand_line('pridjm.txt')).rstrip()
    nad = str(rand_line('nad.txt')).rstrip()
    nade = str(rand_line('nade.txt')).rstrip()
    nade2 = str(rand_line('nade2.txt')).rstrip()
    nadm = str(rand_line('nadm.txt')).rstrip()
    misto = str(rand_line('misto.txt')).rstrip()
    lesi = str(rand_line('lesi.txt')).rstrip()
    elgee = str(rand_line('elgee.txt')).rstrip()
    guilda = str(rand_line('guilda.txt')).rstrip()

    if message.content == '!leaveguild':
#leave template
        leave='Ahoj, rozhodl jsem se leavnout guildu, protože Lesi je ' + nad \
            + ' a ' + pridjm \
            + ' ' + nad \
            + ', který ' + lesi \
            + '. Hraju to už '+str(random.randrange(5,51)) \
            +' let a prošel jsem už '+str(random.randrange(5,21)) \
            +' guild a s takovým ' + nadm \
            + ' jako je Lesi jsem se ještě nesetkal. Doufám, že v příštím tieru ' + guilda \
            + '. Strčte si vaší guildu do ' + misto \
            + ', jdu mít '+str(random.randrange(1,51)) \
            +' parsy jinam! A LG ty ' + pridjm \
            + ' ' + nade \
            + ' se taky můžeš ' + elgee \
            + ' ty ' + nade2+ '!'
        await message.channel.send(leave)

    elif message.content == 'raise-exception':
       raise discord.DiscordException

client.run(TOKEN)
