import discord
import sqlite3
from discord.ext import commands
from discord.commands import SlashCommandGroup

connection = sqlite3.connect("WouldYouRather.db")
cursor = connection.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS questions (
                  question STRING,
                  optionOne VARCHAR(255),
                  optionTwo VARCHAR(255)
                  )""")

class commandHandler(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    WouldYouRather = SlashCommandGroup("wouldyourather", "Category for WouldYouRather commands.")

    @WouldYouRather.command()
    async def generate(self, ctx):
        """Get a random WouldYouRather Question sent in this Channel."""


def setup(bot):
    bot.add_cog(commandHandler(bot))
