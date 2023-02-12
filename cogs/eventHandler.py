import discord
from discord.ext import commands


class eventHandler(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot


def setup(bot):
    bot.add_cog(eventHandler(bot))
