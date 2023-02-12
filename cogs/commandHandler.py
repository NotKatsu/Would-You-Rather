import random

import discord
import sqlite3
from random import *
from discord.ext import commands
from discord.commands import SlashCommandGroup

connection = sqlite3.connect("WouldYouRather.db")
cursor = connection.cursor()

fetchQuestions = cursor.execute('SELECT COUNT(1) FROM questions')
questionCount: int = cursor.fetchone()[0]


class commandHandler(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    WouldYouRather = SlashCommandGroup("wyr", "Category for WouldYouRather commands.")

    @WouldYouRather.command()
    async def random(self, ctx):
        """Get a random WouldYouRather Question sent in this Channel."""

        questionNumber = randint(1, questionCount)
        cursor.execute('SELECT * FROM questions')

        for i, row in enumerate(cursor):
            if i + 1 == questionNumber:
                WouldYouRatherEmbed = discord.Embed(title="Would You Rather...",
                                                    colour=discord.Colour(0x0696EF),
                                                    description=f"> {row[0]}\n OR..\n> {row[1]}")

                WouldYouRatherEmbed.set_footer(text=f"Would You Rather • Question ID: {questionNumber}")

                await ctx.respond(embed=WouldYouRatherEmbed)
                break


def setup(bot):
    bot.add_cog(commandHandler(bot))
