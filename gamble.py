import discord
import asyncio
import random
from discord.ext import commands


class Gamble(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.ucastnici = []
        self.rolly = {}
        self.beh = False
    
    def rolls(self, seznam, dictionary):
        for x in seznam:
            roll = random.randrange(1,101)
            dictionary.update({x:roll})

    @commands.command()
    async def gamblereg(self, ctx):
        if self.beh == True :
            """registruje hrace do gamble poolu"""
            uzivatel = ctx.message.author.name
            if uzivatel in self.ucastnici:
                await ctx.send("uz jsi registrovan")
            else:
                self.ucastnici.append(str(uzivatel))
                await ctx.send("registrace úspěšná")
        else:
            await ctx.send("není kam se registrovat, není aktivní žádný gamble")

    @commands.command()
    async def gamblelist(self, ctx):
        if self.beh == True :
            """listne ucastnici se uzivatele"""
            listuzivatelu='\n'.join(self.ucastnici)
            if not self.ucastnici:
                await ctx.send("0 účastníků")
            else:
                await ctx.send(listuzivatelu)
        else:
            await ctx.send("není aktivní žádný gamble, není co vypsat")

    @commands.command()
    async def gamble(self, ctx, amount: int):
        if self.beh == True :
            await ctx.send('Gamble už jednou běží, nedokážu dělat dvě věci najednou, nejsem Sára.')
        elif amount == 0:
            await ctx.send('Nemůžet hrát o nic, takhle to teda nefunguje.')
        else:
            """gamble uzivatelu z listu"""
            self.beh = True
            ###testovaci uzivatele
            ###self.ucastnici.append('test1')
            ###self.ucastnici.append('test2')
            ###self.ucastnici.append('test3')
            ###self.ucastnici.append('test4')
            ###self.ucastnici.append('test5')
            ###self.ucastnici.append('test6')
            ###self.ucastnici.append('test7')
            ###self.ucastnici.append('test8')
            ###self.ucastnici.append('test9')
            ###self.ucastnici.append('test10')
            ########
            await ctx.send('Gamble o ' + str(amount) + 'g')
            await ctx.send('O goldy přijdeš za 30s, stačí se přihlásit pomocí příkazu !gamblereg')
            await asyncio.sleep(30)
            if not self.ucastnici:
                await ctx.send('Nikdo se nepřidal.')
                await ctx.send('Gamble ukončen.')
            elif len(self.ucastnici) == 1:
                await ctx.send('Nemůžeš hrát sám, to prostě nejde!')
                await ctx.send('Gamble ukončen.')
            else:
                await ctx.send("Generuji hodně...hodně krásné výsledky!")
                self.rolls(self.ucastnici, self.rolly)
                while len(set(self.rolly.values())) != len(self.rolly.values()):
                    self.rolls(self.ucastnici, self.rolly)
                await ctx.send("**Roll:**")
                embedik = discord.Embed(colour = discord.Colour.blue())
                embedik.set_author(name='Rolly')
                for y, z in self.rolly.items():
                    embedik.add_field(name='__**'+str(y)+'**__', value=str(z), inline=True)
                    #await ctx.send(str(y) + ' - ' + str(z))
                await ctx.send(embed=embedik)
                prohravajici = min(self.rolly, key=self.rolly.get)
                vyhravajici = max(self.rolly, key=self.rolly.get)
                await ctx.send('Gamble ukončen.')
                await ctx.send('**Uživatel '+ str(prohravajici) + ' dá ' + str(amount) + 'g uživateli ' + vyhravajici+'**')
            self.ucastnici = []
            self.rolly = {}
            self.beh = False

###setup cogu
def setup(bot):
    bot.add_cog(Gamble(bot))