import os
import random

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

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
    pridjm = [
        'dementní',
        'vyjebanej',
        'zkurvenej',
        'zasranej',
        'vypíčenej',
        'zpíčenej',
    ]
    nad = [
        'kotot',
        'zmrd',
        'čůrák',
        'dement',
        'mentál',
        'fagot',
    ]
    nade = [
        'kotote',
        'zmrde',
        'čůráku',
        'demente',
        'mentále',
        'fagote',
    ]
    nade2 = [
        'kotote',
        'zmrde',
        'čůráku',
        'píčo jedna',
        'chcanko',
        'sračko',
        'mrdko jedna',
    ]
    nadm = [
        'kototem',
        'zmrdem',
        'čůrákem',
        'zkurvysynem',

    ]

    misto = [
        'prdele',
        'řiti',
        'kundy',
        'píči',
        'zadku',
        'víte kam'
    ]
    lesi = [
        'jenom na všechny řve',
        'akorát každýho kritizuje',
        'stejně neumí hrát ferála',
        'akorát parsuje na píču',
        'si o sobě myslí jak je dobrej, i když je to nula',
        'ani neumí vyprat polštář',
    ]
    elgee = [
        'jít zabít',
        'jít vysrat',
        'KYS',
        'jít oběsit',
        'jít zastřelit',
    ]
    guilda = [
        'dostanete cancer',
        'všichni shoříte',
        'nezabijete ani prvního bosse na mythic',
        'nedoděláte ani curvu',
        'všichni commitnete noliving',
        'dostanete ban',
    ]


    if message.content == '!leaveguild':

        leave='Ahoj, rozhodl jsem se leavnout guildu, protože Lesi je ' + random.choice(nad) + ' a ' + random.choice(pridjm) + ' ' + random.choice(nad) + ', který ' + random.choice(lesi) + '. Hraju to už '+str(random.randrange(5,51))+' let a prošel jsem už '+str(random.randrange(5,21))+' guild a s takovým ' + random.choice(nadm) + ' jako je Lesi jsem se ještě nesetkal. Doufám, že v příštím tieru ' + random.choice(guilda) + '. Strčte si vaší guildu do ' + random.choice(misto) + ', jdu mít '+str(random.randrange(1,51))+' parsy jinam! A LG ty ' + random.choice(pridjm) + ' ' + random.choice(nade) + ' se taky můžeš ' + random.choice(elgee) + ' ty ' + random.choice(nade2)+ '!'
        await message.channel.send(leave)

    elif message.content == 'raise-exception':
       raise discord.DiscordException


client.run(TOKEN)
