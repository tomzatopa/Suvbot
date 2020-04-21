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
import datetime
import aiohttp
import re
from datetime import timedelta
from os import path
from dotenv import load_dotenv
from discord.ext import commands
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from collections.abc import Sequence

###############################
###SETTINGS + IMPORT PROMENNYCH
###############################
bot = commands.Bot(command_prefix='!')
bot.remove_command('help')
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
MAINTAINER = [
    int(os.getenv('MAINTAINER1')),
    int(os.getenv('MAINTAINER2')),
    int(os.getenv('MAINTAINER3'))
    ]
SPCKAPI = os.getenv('SPCKAPI')
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
async def on_member_update(before,after):
        if len(before.roles) < len(after.roles):
        	new_role = next(role for role in after.roles if role not in before.roles)
        	if new_role.name in ('Guild'):
        		await after.send('Vítej v IAO\! \n\nJsem useless guildovní bot na memy, ale protože naši officeři jsou ještě víc useless a většinou novým lidem zapomenou napsat, jak to v téhle rádoby tryhard guildě chodí, tak ti to radši napíšu já. \n\n**NEJDŮLEŽITĚJŠÍ INFO NA ZAČÁTKU\!\!\!** Nesnaž se hledat info ingame v nějakých guild messages nebo guild infu. Jsme strašně moderní a hip, takže 99 % věcí řešíme přes discord. \n\nPokud jsi dostal/a invite do guildy, je dost pravděpodobné, že jsi dostal/a ingame rank \"kus hovna\". Jestli tě to vyloženě sere, tak ~~je nám to moc líto, ale~~ máš bohužel smůlu. Každý nějak začíná a po dvou nebo třech raidech stejně dostaneš promote. Každopádně si prosím přečti **#kus-hovna-info** , kde je víceméně to samé co ti teď píšu, jen méně aktuální. \n\nNejdůležitější v téhle guildě jsou ~~raidy~~ memes. Naše guildovní memes najdeš v channelu **#guild-memes** (neasi) a neboj se přispět i nějakým svým výtvorem. Ideální samozřejmě bude, když to nebude úplná sračka, protože špatný memy jsou horší než šedivý parsy. Kdyby ses chtěl/a inspirovat, napiš do #guild-memes \!iaomeme a vyhodí ti to nějakej náhodnej z asi 10 memů, protože Suvoj s Ehrendilem dodneška nebyli schopní jich do toho commandu přidat víc. \n\n**Raidy** se tady taky řeší docela dost.**Důležité** je, aby ses přihlašoval/a na raidy v channelu **#kalendář**. Raidujeme ve středu a v neděli od 18:40 do 22:00. \n\nPokud nejsi nějakej strašnej frajer, kterej k nám přišel z Eternal Shadows nebo nějaký jiný wannabe #1worldrank guildy, tak si přečti #jak-zlepšit-dps . Možná ti to pomůže, možná ne, ale když budeš hrát jako ~~tvoje~~ Lesiho máma, tak tě stejně do raidů nikdo brát nebude a za chvíli leavneš do jiný guildy. \n\nNeboj se tady bavit s lidma a zkus se prosím nechovat jako kokot :) I když tady si tady ze sebe rádi děláme prdel, tak pořád chceme hlavně pohodáře, kteří po sobě nebudou řvát kvůli každé píčovince. Pokud máš nějaké otázky, můžeš s nima otravovat eLGeeho.')
        	elif new_role.name in ('Core'):
        		await after.send('OOOoooOOOOOooOOOOooOOOO\!\!\! \nTady někdo dostal promote do \"kór\". Mmmmmm... To seš frajer... Seš fakt dobrej\! Fakt. Skoro jako Lesi... Ty hraješ tu hru už aspoň tak 30 let co? \nVíš co znamená v téhle guildě být core? NIC\!\!\! VŮBEC NIC\!\!\! Kromě toho, že budeš vědět o nějakejch pitomejch guildovních srazech, kde nám Lambáda vybere shitovou hospodu, kde je nejexkluzivnější drink tuzemák s koli kolou; kde se Zedd vožere za 2 hodiny a pak se nám bude snažit utéct; kde LG řekne po půlnoci, že nás někam dovede, a dovede nás do nějaký hipsterský prdele, kam už nikdo stejně nejde a všichni jdou domů? Jo, přesně to tady core znamená. \nMáš přístup do **\#wow-core**, což je jenom další useless channel navíc, kde se občas spamujou nějaký hovna. Jinak nemáš nic\! \nUžij si to\! A nezapomeň, že i tys byl/a jednou kus hovna. \nJestli někdy leavneš guildu, tak se s tebou už nikdy nikdo nebude bavit a umřou tři koťátka.')


#stolen shit aby fungovala prihlaska
def make_sequence(seq):
    if seq is None:
        return ()
    if isinstance(seq, Sequence) and not isinstance(seq, str):
        return seq
    else:
        return (seq,)
def message_check(channel=None, author=None, content=None, ignore_bot=True, lower=True):
    channel = make_sequence(channel)
    author = make_sequence(author)
    content = make_sequence(content)
    if lower:
        content = tuple(c.lower() for c in content)
    def check(message):
        if ignore_bot and message.author.bot:
            return False
        if channel and message.channel not in channel:
            return False
        if author and message.author not in author:
            return False
        actual_content = message.content.lower() if lower else message.content
        if content and actual_content not in content:
            return False
        return True
    return check
async def otazka(user,text):
    await user.send(text)
    try:
        response = await bot.wait_for('message',check=message_check(channel=user.dm_channel),timeout=420.0)
    except asyncio.TimeoutError:
        await user.send('Vypršel ti čas na zadání odpovědi.')
        return True,''
    else:
        return False,response.content
def odpovedWrapper(text1,text2):
    return '**' + text1 + "**" + '\n*' + text2 + '*\n'\
async def simpleOtazka(user,text):
    await user.send(text)
    try:
        response = await bot.wait_for('message',check=message_check(channel=user.dm_channel),timeout=420.0)
    except asyncio.TimeoutError:
        await user.send('Vypršel ti čas na zadání odpovědi.')
        return True,''
    else:
        return False,response.content.lower().strip()

@bot.event
async def on_message(message):
    if (message.channel.id == 634683421616111616) and (message.author.id != 291891867703050240) and 'start' in message.content:
        user = message.author
        id = message.author.id
        await message.delete()
        finalmsg= ''
        await user.send("Čau! Já jsem Suvbot. Narozdíl od IAO, kteří ani nezvládají vyhrát World First Alliance Drak\'thul Third First Race, já jsem s velkou pravděpodobností ten nejchytřejší guild bot široko daleko.\nBudu se tě ptát na otázky a ty mi na ně prosím odpovídej.Tvé odpovědi zpracuji a přepošlu officer týmu naší guildy.\nU každé otázky je limit 7 min(420 sec XD) na odpověď, takže kdyby ses během vyplňování přihlášky rozhodl/a, že na to sereš, tak prostě neodpovídej a proces vytváření přihlášky se po 7 min automaticky zruší." )

        err,response= await simpleOtazka(user,"Chápeš všechno, co jsem ti teď napsal? Odpověz prosím **ano**. Můžeš odpovědět i **ne**, ale zatím to snad nebylo tak složitý.")
        if err==True:
            return
        if response=='ano':
            await user.send("Výborně! Můžeme začít s přihláškou.")
        elif response=='ne':
            embed = discord.Embed()
            embed.set_image(url="https://media1.tenor.com/images/4b32ba323922f0fd0b73aea62ce75af1/tenor.gif?itemid=4919469")
            await user.send(embed=embed)
            err,response= await simpleOtazka(user," Oukej tak znovu. JÁ SE TĚ BUDU POSTUPNĚ PTÁT NA OTÁZKY. TY MI NA NĚ BUDEŠ ODPOVÍDAT.\nUž jsi mi jednou odpověděl **NE**, když jsem se tě ptal, jestli to celý chápeš...\n*JÁ SE PTÁT, TY ODPOVÍDAT. TY UŽ CHÁPAT?! - TY NAPSAT* **ANO** *DOLE!* ")
            if err==True:
                return
            if response=='ano':
                await user.send("Výborně! Můžeme začít s přihláškou.")
            else:
                await user.send("Tvoje přihláška se ruší. Nemám na to, sorry.")
                channel=bot.get_channel(702074796984500234)
                await channel.send("Ahoj všichni! Rád bych vám oznámil, že <@"+str(id)+"> je debil! HALÓ HALÓ!!! <@"+str(id)+"> JE HLUPÁK!!! Nemám na to s ním vyplňovat přihlášku. Nebudu to dělat...")
                return
        else:
            await user.send("Hahaha! Napíšu botovi něco jinýho než ano/ne, protože na to beztak nikdo nemyslel? Oooooooo jak originální! Když jsi tak chytrej, tak jdeme vyplňovat přihlášku.")

        jedna="Nick a class tvojí postavy:"
        err,response= await otazka(user,jedna)
        if err==True:
            return
        else:
            jedna = odpovedWrapper(jedna,response)

        dva="Máš nějaké zásadní problémy s raid timem? (Třeba práce na směny, jezdíš později z práce každou středu atd.)"
        err,response= await otazka(user,dva)
        if err==True:
            return
        else:
            dva = odpovedWrapper(dva,response)

        tri="Odkaz na raider.io tvého charu"
        err,response= await otazka(user,tri)
        if err==True:
            return
        else:
            while ('eu/drakthul' not in response and 'eu/burning-blade' not in response) or 'raider.io/characters' not in response:
                await user.send("Ale notak. Není to tak těžký...")
                if 'raider.io/characters' not in response:
                    await user.send("Vůbec jsi neposlal/a odkaz na char na raider.io")
                else:
                    await user.send("Musíš poslat odkaz na postavu z EU Drak'thul/Burning Blade.")
                await user.send("Zkus to znovu:")
                err,response= await otazka(user,tri)
                if err==True:
                    return
            await user.send("GOOD JOB! Tohle se povede tak jednomu člověku z deseti.")
            tri = odpovedWrapper(tri,response)

        ctyri="Odkaz na warcraftlogs tvého charu:"
        err,response= await otazka(user,ctyri)
        if err==True:
            return
        else:
            if ('eu/drakthul' not in response and 'eu/burning-blade' not in response) or 'warcraftlogs.com/character' not in response:
                await user.send("C'mon, dal/a jsi předchozí otázku dáš i tohle")
                if 'raider.io/characters' not in response:
                    await user.send("Vůbec jsi neposlal/a odkaz na char na warcraftlogs")
                else:
                    await user.send("Musíš poslat odkaz na postavu z EU Drak'thul/Burning Blade.")
                await user.send("Try again:")
                err,response= await otazka(user,ctyri)
                if err==True:
                    return
                if ('eu/drakthul' not in response and 'eu/burning-blade' not in response) or 'warcraftlogs.com/character' not in response:
                    await user.send("Whatever...jdeme na další otázku")
                else:
                    await user.send("NICE...jdeme na další otázku")

            ctyri = odpovedWrapper(ctyri,response)

        pet="Pokud máš použitelné offspecy a alty, tak je nějak stručně vypiš:"
        err,response= await otazka(user,pet)
        if err==True:
            return
        else:
            pet = odpovedWrapper(pet,response)

        sest="Předchozí guilda a důvod odchodu:"
        err,response= await otazka(user,sest)
        if err==True:
            return
        else:
            sest = odpovedWrapper(sest,response)

        sedm="Znáš a používáš raidbots a/nebo wowanalyzer?"
        err,response= await otazka(user,sedm)
        if err==True:
            return
        else:
            sedm = odpovedWrapper(sedm,response)

        osm="Proč chceš k nám a co si od toho slibuješ?"
        err,response= await otazka(user,osm)
        if err==True:
            return
        else:
            osm = odpovedWrapper(osm,response)

        devet="Napiš nám něco o sobě (kolik ti je? kde bydlíš? číslo kreditní karty?):"
        err,response= await otazka(user,devet)
        if err==True:
            return
        else:
            devet = odpovedWrapper(devet,response)

        deset="Cokoliv dalšího co nám chceš říct:"
        err,response= await otazka(user,deset)
        if err==True:
            return
        else:
            deset = odpovedWrapper(deset,response)

        finalmsg= "1) "+jedna+"2) "+dva+"3) "+tri+"4) "+ctyri+"5) "+pet+"6) "+sest+"7) "+sedm+"8) "+osm+"9) "+devet+"10) "+deset

        await user.send("Wow, zvládli jsme to. Úžasný. Tady si to po sobě prosím ještě jednou přečti, tohle budu přeposílat officerům:")
        await user.send(finalmsg)
        await user.send("Vidíš, že jsem ty otázečky pěkně očísloval.")
        err,response= await simpleOtazka(user,"Jestli chceš něco upravit, napiš číslo otázky. Pokud nechceš nic upravovat, napiš **odeslat** a je hotovo")
        if err==True:
            return
        while response!='odeslat':
            if response=='1':
                await user.send("Upravuješ:")
                err,response= await otazka(user,jedna)
                if err==True:
                    return
                else:
                    jedna = odpovedWrapper(jedna,response)
            elif response=='2':
                await user.send("Upravuješ:")
                err,response= await otazka(user,dva)
                if err==True:
                    return
                else:
                    dva = odpovedWrapper(dva,response)
            elif response=='3':
                await user.send("Upravuješ:")
                err,response= await otazka(user,tri)
                if err==True:
                    return
                else:
                    while ('eu/drakthul' not in response and 'eu/burning-blade' not in response) or 'raider.io/characters' not in response:
                        await user.send("Ale notak. Jednou se ti tohle už povedlo zadat správně...")
                        if 'raider.io/characters' not in response:
                            await user.send("Vůbec jsi neposlal/a odkaz na char na raider.io")
                        else:
                            await user.send("Musíš poslat odkaz na postavu z EU Drak'thul/Burning Blade.")
                        await user.send("Zkus to znovu:")
                        err,response= await otazka(user,tri)
                        if err==True:
                            return
                    await user.send("GOOD JOB!")
                    tri = odpovedWrapper(tri,response)
            elif response=='4':
                await user.send("Upravuješ:")
                err,response= await otazka(user,ctyri)
                if err==True:
                    return
                else:
                    ctyri = odpovedWrapper(ctyri,response)
            elif response=='5':
                await user.send("Upravuješ:")
                err,response= await otazka(user,pet)
                if err==True:
                    return
                else:
                    pet = odpovedWrapper(pet,response)
            elif response=='6':
                await user.send("Upravuješ:")
                err,response= await otazka(user,sest)
                if err==True:
                    return
                else:
                    sest = odpovedWrapper(sest,response)
            elif response=='7':
                await user.send("Upravuješ:")
                err,response= await otazka(user,sedm)
                if err==True:
                    return
                else:
                    sedm = odpovedWrapper(sedm,response)
            elif response=='8':
                await user.send("Upravuješ:")
                err,response= await otazka(user,osm)
                if err==True:
                    return
                else:
                    osm = odpovedWrapper(osm,response)
            elif response=='9':
                await user.send("Upravuješ:")
                err,response= await otazka(user,devet)
                if err==True:
                    return
                else:
                    devet = odpovedWrapper(devet,response)
            elif response=='10':
                await user.send("Upravuješ:")
                err,response= await otazka(user,deset)
                if err==True:
                    return
                else:
                    deset = odpovedWrapper(deset,response)
            else:
                await user.send("Nenapsal/a jsi platné č. otázky nebo **odeslat**")
            err,response= await simpleOtazka(user,"Jestli chceš ještě něco upravit, napiš číslo otázky. Pokud už nechceš nic upravovat, napiš **odeslat**")
            if err==True:
                return

        finalmsg=jedna+dva+tri+ctyri+pet+sest+sedm+osm+devet+deset

        channel = bot.get_channel(634689737910648832)
        await channel.send('<@'+str(id)+'>')
        await channel.send(finalmsg)
        await user.send("Přihláška byla odeslána!")

    if (message.channel.id == 634683421616111616) and (message.author.id != 291891867703050240) and 'start' not in message.content:
        await message.delete()
        channel = bot.get_channel(634683421616111616)
        await channel.send("Pro zahájení procesu tvorby přihlášky napiš **start**",delete_after=5)
    if (message.channel.id == 493688092075753502) and (message.author.id != 291891867703050240):
        finalmsg = message.content
        id = message.author.id
        if "www.warcraftlogs.com" not in finalmsg:
            channel = bot.get_channel(493688092075753502)
            if id in MAINTAINER:
                await channel.send("Sorry Master, ale tenhle channel je pouze na logy!",delete_after=10)
            else:
                await channel.send("<@!"+str(id)+"> čo si kokot? Tenhle channel je na logy!",delete_after=10)
            await message.delete()
    if (message.channel.id == 702074796984500234) and (message.author.id != 291891867703050240):
        await message.delete()
        channel = bot.get_channel(702074796984500234)
        await channel.send("Sem můžu psát jenom já!",delete_after=5)
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

def sklon_2p(text):
    sklon=text
    if text.endswith('an'):
        sklon=text[:-2]+'na'
    elif text.endswith('na'):
        sklon=text[:-1]+'y'
    elif text.endswith('e'):
        sklon=text[:-1]+'a'
    elif text.endswith('dk') or text.endswith('dh'):
        sklon+='čka'
    else:
        sklon+='a'
    return sklon

def sklon_4p(text):
    sklon=text
    if text.endswith('an'):
        sklon=text[:-2]+'na'
    elif text.endswith('na'):
        sklon=text[:-1]+'u'
    elif text.endswith('e'):
        sklon=text[:-1]+'a'
    elif text.endswith('dk') or text.endswith('dh'):
        sklon+='čko'
    else:
        sklon+='a'
    return sklon

def sklon_7p(text):
    sklon=text
    if text.endswith('na'):
        sklon=text[:-1]+'ou'
    elif text.endswith('e'):
        sklon+='m'
    elif text.endswith('dk') or text.endswith('dh'):
        sklon+='čkem'
    else:
        sklon+='em'
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
    helpmsg.add_field(name='__**!compliment osoba**__', value='Složí kompliment osobě. Kappa', inline=True)
    helpmsg.add_field(name='__**!say text**__', value='Zopakuje to co napíšete.', inline=True)
    helpmsg.add_field(name='__**!emojify text**__', value='Text-to-emoji konvertor.', inline=True)
    helpmsg.add_field(name='__**!iaosound vybrany-zvuk (číslo)**__', value='Přehraje ve voice kanále vybraný zvuk. Pokud za název napíšete ještě číslo, přehraje se zvuk vícekrát(max 50 - vyšší číslo je bráno jako 50). Pro list dostupných zvuků zadejte: !help iaosound', inline=True)
    helpmsg.add_field(name='__**!iaoimage vybrany-img**__', value='Pošle do kanálu vyberaný image. Pro list dostupných zvuků zadejte: !help iaoimage', inline=True)
    helpmsg.add_field(name='__**!iaomeme**__', value='Pošle do kanálu random meme!', inline=True)
    helpmsg.add_field(name='__**!slovak osoba**__', value='Pro naše bratry, nebojte se užít mention a jednoho z nich označit! ', inline=True)
    helpmsg.add_field(name='__**!slabikar**__', value='Bův ví co to je... :shrug:', inline=True)
    helpmsg.add_field(name='__**!gondorhelp kdo-neprisel-na-pomoc**__', value='Gondor help.... mluví za vše', inline=True)
    helpmsg.add_field(name='__**!inspire**__', value='Zobrazí náhodnou \"inspirational quote\"', inline=True)
    helpmsg.add_field(name='__**!recipe neco**__', value='Vyhledá recept', inline=True)
    helpmsg.add_field(name='__**!yoda text**__', value='Přeloží zadaný text do Yoda mluvy.', inline=True)
    helpmsg.add_field(name='__**!fact **__', value='Zobrazí náhodný fun fact', inline=True)
    helpmsg.add_field(name='__**!funfact **__', value='Same as !fact - cos all facts are fun', inline=True)
    helpmsg.add_field(name='__**!joke**__', value='Zobrazí náhodný dad joke', inline=True)
    helpmsg.add_field(name='__**!wolfram**__', value='Zobrazí odpověď na wolframalpha dotaz', inline=True)
    helpmsg.add_field(name='__**!office**__', value='Zobrazí náhodnou hlášku Michaela Scotta z The Office', inline=True)
    helpmsg.add_field(name='__**!cat**__', value='Zobrazí náhodný cat pic', inline=True)
    helpmsg.add_field(name='__**!poll typ otázka odpoved1 odpoved2 atd**__', value='Vytvoří hlasování. Pro více info: !help poll', inline=True)
    helpmsg.add_field(name='__**!gamble prikaz mluvi sam za sebe**__', value='Vytvoří gamble. Pro více info: !help gamble', inline=True)
    helpmsg.add_field(name='__**!short URL**__', value='Zkrátí URL', inline=True)

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
        elif "gamble" in args:
            helpmsg.set_author(name='SUVBOT HELPIK')
            helpmsg.add_field(name='Obecné info:', value='Gamble může být spuštěn pouze jeden v danou chvíli. \nNa registraci do gamblu od jeho zadání máte 30 sekund.\n', inline=False)
            helpmsg.add_field(name='!gamble "počet goldů"', value='vytvoří gamble o zadaný počet goldů', inline=False)
            helpmsg.add_field(name='!gamblereg', value='provede registraci do gamblu, musí být nejdříve někým zadán !gamble "počet goldů"', inline=False)
            helpmsg.add_field(name='!gamblelist', value='vrátí seznam uživatelů zapsaných do gamblu', inline=False)
            await user.send(embed=helpmsg)
    else:
        await user.send("Help, který by pochopil snad každý!")
        await user.send(embed=helpmsg)

#################################
#leaveguld command
@bot.command(name='leaveguld')
async def leaveguld(ctx, arg1, arg2):
    for r in ctx.message.author.roles:
        if r.id  == 467773009952899072 or r.id  == 647096577491599360 :
            await ctx.send('Nice try, ale ty nikam nejdeš!')
            return

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


#alt command
@bot.command(name='alt')
async def alt(ctx, arg1, arg2):

    altc = str(arg1).lower()
    alt2p = sklon_2p(altc)
    alt4p = sklon_4p(altc)
    alt7p = sklon_7p(altc)
    mainc = str(arg2).lower()

    if alt4p.endswith('na'):
        a1="tu "+alt4p
    elif alt2p.endswith('čko'):
        a1="to "+alt4p
    else:
        a1="toho "+alt4p

    if alt7p.startswith('s'):
        a2="se "+alt7p
    else:
        a2="s "+alt7p

    id = str(rand_line('ideal.txt')).rstrip()
    ra = str(rand_line('kvuli.txt')).rstrip()
    dr = str(rand_line('kvuli.txt')).rstrip()
    while ra==dr:
        dr = str(rand_line('kvuli.txt')).rstrip()
    il = str(rand_line('zase.txt')).rstrip()

    alt='Mám otázku do pléna. Co si myslíte o tom, že bych zkusil nějak equipnout '+a1 \
        + ' kvůli toolkitu? Obecně je samozřejmě ' + mainc \
        + ' lepší a jistější, ale utilita ' +  alt2p \
        + ' v tomhle tieru je fakt celkem velká a už na Vexioně jsme měli trochu problém v tom, že ' + id \
        + '. Raden taky celkem dobře funguje ' + a2 + ' kvůli ' + ra \
        + ' (i když '+ mainc +' je tam prostě klasicky v pohodě)' \
        + '. Drest je ' + mainc + ' fight kvůli ' + dr \
        + ', Ilgynoth  má zase ' + il  + ', takže ' + altc+ ' value.'


    await ctx.send(alt)

@alt.error
async def info_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Je potřeba zadat jména class: !alt "alt class" "main class"')

#insult command
@bot.command(name='insult')
async def insult(ctx,arg1):
    nekdo = sklon_5p(str(arg1)).capitalize()
    if 'Suvbot' in nekdo or 'suvbot' in nekdo or '291891867703050240' in nekdo :
        if ctx.message.author.id in MAINTAINER:
            await ctx.send('Sorry Master, but even you shall not insult me.')
            return
        else:
            await ctx.send('Nice try...')
            return
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

#compliment command
@bot.command(name='compliment')
async def compliment(ctx,arg1):
    id="<@!"+str(ctx.message.author.id)+">"
    nekdo = str(arg1).capitalize()
    if 'Suvbot' in nekdo or 'suvbot' in nekdo or '291891867703050240' in nekdo :
        com="Thank you very much " + id + ", dělám co můžu."
    elif id == nekdo or ctx.message.author.display_name in nekdo:
        r=random.randrange(1,4)
        if r==1:
            com="\"Bláhovec vlastní přednosti vynáší na povrch, moudrý je skrývá uvnitř - v nedohlednu.\"\n*Lucius Annaeus Seneca*"
        elif r==2:
            com="\"Kdo sám se chválí, rychle posměch utrží.\"\n*Publilius Syrus*"
        else:
            com="\"Ať tě chválí cizí a ne tvá vlastní ústa, cizinec a ne tvoje rty.\"\n*Přísloví 27,2, Bible*"
    else:
        com="Nah...We don't do that here."
    await ctx.send(com)

@compliment.error
async def info_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Je potřeba zadat jméno člověka, kterému chcete složit kompliment.')


#say command
@bot.command(name='say')
async def say(ctx,*args):
    a=" ".join(args)
    await ctx.send(a)
    await ctx.message.delete()

@say.error
async def info_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Je potreba zadat text')

#emojify command
@bot.command(name='emojify')
async def emojify(ctx,*args):
    text=(" ".join(args)).lower()
    emojified = ''
    numwords = {0: 'zero',1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
    alph = r'[A-Za-z]+'
    num = r'[0-9]'
    for i in text:
        if re.search(alph, i):
            emojified += ':regional_indicator_{}: '.format(i)
        elif re.search(num, i):
            emojified += ':{}: '.format(numwords[int(i)])
        else:
            emojified += '  '+i+'  '
    await ctx.send(emojified)

@emojify.error
async def info_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Je potreba zadat text')

#iaosound command
@bot.command(name='iaosound')
async def iaosound(ctx, arg1, *args):
    channel = ctx.author.voice.channel
    #checkuje jestli existuje file ve slozce sounds/
    if path.exists('./sounds/'+arg1+'.mp3'):
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio('./sounds/'+arg1+'.mp3'), after=lambda e: print('prehravam', e))
        while vc.is_playing():
            await asyncio.sleep(1)
        if args and args[0].isnumeric():
                if (int(args[0]) == 420) or (int(args[0]) < 51):
                    r=int(args[0])-1
                else:
                    r=49
                for x in range(r):
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
    r=random.randrange(1,3)
    if r==1:
        sl= 'Nie je ti pičně '+ os +'?'
    else:
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

#reset command
@bot.command(name='reset')
async def reset(ctx):
    ins = 'https://www.youtube.com/watch?v=xA111D1jQCw&feature=youtu.be'
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

#yoda command
@bot.command(name='yoda')
async def yoda(ctx,*args):
    a=" ".join(args)
    a=urllib.parse.quote_plus(a)
    response=requests.get('https://api.funtranslations.com/translate/yoda.json?text='+a)
    dic=response.json()
    res=dic['contents']['translated']
    await ctx.send(res)
@yoda.error
async def info_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Je potřeba zadat text co chcete přeložit.')

#fact command
@bot.command(name='fact')
async def fact(ctx):
    response=requests.get('https://uselessfacts.jsph.pl/random.json?language=en')
    dic=response.json()
    res=dic['text']
    await ctx.send(res)

#funfact command
@bot.command(name='funfact')
async def funfact(ctx):
    response=requests.get('https://uselessfacts.jsph.pl/random.json?language=en')
    dic=response.json()
    res=dic['text']
    await ctx.send(res)

#shorturl command
@bot.command(name='shorturl')
async def shorturl(ctx, arg1: str):
    user = ctx.author
    begindate=datetime.datetime.now()
    enddate=begindate+datetime.timedelta(days=1)
    content='{"longUrl":"'+arg1+'","validSince":"'+begindate.strftime('%Y-%m-%dT%H:%M:%SZ')+'","validUntil":"'+enddate.strftime('%Y-%m-%dT%H:%M:%SZ')+'","findIfExists":"true"}'
    headers={
        'Content-Type':'application/json',
        'Accept':'application/json',
        'X-Api-Key':''+SPCKAPI+''
        }
    print(content)
    print(headers)
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.post('https://spck.cz/rest/v2/short-urls', data=content, headers=headers) as resp:
            if resp.status != 200:
                await user.send("Něco se pokazilo - err: "+str(resp.status))
            else:
                answ=await resp.json()
                await user.send('Zkracena URL: {}'.format(answ.get("shortUrl")))

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
    if len(options) > 26:
        await ctx.send('Poll může mít maximálně 20 možností odpovědi.')
        return
    if len(options) == 0:
        reactions = ['✅', '❌']
        options = ['ANO', 'NE']
    else:
        reactions = ['🇦', '🇧', '🇨', '🇩', '🇪', '🇫', '🇬', '🇭', '🇮', '🇯', '🇰', '🇱', '🇲', '🇳', '🇴', '🇵', '🇶', '🇷', '🇸', '🇹']
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
    await ctx.message.delete()
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
