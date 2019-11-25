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
            await ctx.send('Gamble už jednou běží')
        else:
            """gamble uzivatelu z listu"""
            self.beh = True
            ###testovaci uzivatele
            self.ucastnici.append('test1')
            self.ucastnici.append('test2')
            self.ucastnici.append('test3')
            self.ucastnici.append('test4')
            self.ucastnici.append('test5')
            ########
            await ctx.send('Gamble o ' + str(amount) + 'g')
            await ctx.send('Gamble se spustí za 20s.')
            await asyncio.sleep(20)
            if not self.ucastnici:
                await ctx.send('Zaregistrovalo se 0 účastníků.')
            else:
                for x in self.ucastnici:
                    roll = random.randrange(1,101)
                    self.rolly.update({x:roll})
                self.rolly = sorted(self.rolly.values())
                await ctx.send("aktuálni rolly:")
                for y, z in self.rolly.items():
                    await ctx.send(str(y) + ' - ' + str(z))
                self.ucastnici = []
                self.rolly = {}
                await ctx.send('Gamble ukončen.')
                self.beh = False

    


# toto byl test
#    @commands.command()
#    async def gamble(self, ctx):
#        """gamble"""
#        if self.coinflip() == 1:
#            await ctx.send("1")
#        else:
#            await ctx.send("0")

###setup cogu
def setup(bot):
    bot.add_cog(Gamble(bot))