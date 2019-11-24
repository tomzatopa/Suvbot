import discord
import asyncio
import random
from discord.ext import commands


class Gamble(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.ucastnici = []
        self.rolly = {}

    @commands.command()
    async def gamblereg(self, ctx):
        """registruje hrace do gamble poolu"""
        uzivatel = ctx.message.author.name
        if uzivatel in self.ucastnici:
            await ctx.send("uz jsi registrovan")
        else:
            self.ucastnici.append(str(uzivatel))
            await ctx.send("registrace úspěšná")

    @commands.command()
    async def gamblelist(self, ctx):
        """listne ucastnici se uzivatele"""
        listuzivatelu='\n'.join(self.ucastnici)
        if not self.ucastnici:
            await ctx.send("0 účastníků")
        else:
            await ctx.send(listuzivatelu)

    @commands.command()
    async def gamble(self, ctx, amount: int):
        """gamble uzivatelu z listu"""
        await ctx.send('Gamble o ' + str(amount) + 'g')
        await ctx.send('Gamble se spustí za 60s.')
        await asyncio.sleep(60)
        if not self.ucastnici:
            await ctx.send('Zaregistrovalo se 0 účastníků.')
        else:
            for x in self.ucastnici:
                self.rolly[x] = random.randrange(1,101)
            await ctx.send("aktuálni rolly:")
            for y, z in self.rolly.items():
                await ctx.send(str(y) + ' - ' + str(z))
            self.ucastnici = []
            self.rolly = {}
            await ctx.send('Gamble ukončen.')

    


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