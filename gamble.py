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
        await ctx.send(listuzivatelu)

    @commands.command()
    async def gamble(self, ctx, amount: int):
        """gamble uzivatelu z listu"""
        await asyncio.sleep(15)
        for x in self.ucastnici:
            self.rolly[x] = random.randrange(1,101)
        await ctx.send("aktuálni rolly:")
        for y, z in self.rolly.items():
            await ctx.send(y + ' ' + z)
        
    


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