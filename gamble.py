import discord
import asyncio
import random
from discord.ext import commands


class Gamble(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.ucastnici = []

    def coinflip(self):
        return random.randint(0, 1)

    @commands.command()
    async def gamblereg(self, ctx):
        """registruje hrace do gamble poolu"""
        uzivatel = ctx.message.author.name
        self.ucastnici.append(str(uzivatel))

    @commands.command()
    async def gamblelist(self, ctx):
        """listne ucastnici se uzivatele"""
        listuzivatelu='\n'.join(self.ucastnici)
        await ctx.send(listuzivatelu)

    @commands.command()
    async def gamble(self, ctx):
        """gamble"""
        if self.coinflip() == 1:
            await ctx.send("1")
        else:
            await ctx.send("0")

###setup cogu
def setup(bot):
    bot.add_cog(Gamble(bot))