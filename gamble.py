import discord
import asyncio
import random
from discord.ext import commands


class Gamble(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def coinflip(self):
        return random.randint(0, 1)

    @commands.command()
    async def gamble(self, ctx):
        """gamble"""
        if self.coinflip() == 1:
            await ctx.send("1")
        else:
            await ctx.send("0")
def setup(bot):
    bot.add_cog(Gamble(bot))