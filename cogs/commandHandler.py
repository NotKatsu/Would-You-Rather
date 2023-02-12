import discord
from discord.ext import commands


class commandHandler(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot


def setup(bot):
    bot.add_cog(commandHandler(bot))
