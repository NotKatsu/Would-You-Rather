import random
import discord
import sqlite3
from discord.ext import commands
from discord.commands import SlashCommandGroup


class commandHandler(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    WouldYouRather = SlashCommandGroup("wouldyourather", "Category for WouldYouRather commands.")

    @WouldYouRather.command()
    async def generate(self, ctx):
        """Get a random WouldYouRather Question sent in this Channel."""


def setup(bot):
    bot.add_cog(commandHandler(bot))
