import sqlite3
from random import *

import discord
from discord.commands import SlashCommandGroup
from discord.ext import commands

connection = sqlite3.connect("WouldYouRather.db")
cursor = connection.cursor()

fetchQuestions = cursor.execute('SELECT COUNT(1) FROM questions')
questionCount: int = cursor.fetchone()[0]


def getQuestion(questionNumber):
    cursor.execute('SELECT * FROM questions')

    for i, row in enumerate(cursor):
        if i + 1 == questionNumber:
            return row[0], row[1]


class commandHandler(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    WouldYouRather = SlashCommandGroup("wyr", "Category for WouldYouRather commands.")

    @WouldYouRather.command()
    async def random(self, ctx):
        """Get a random WouldYouRather Question sent in this Channel."""

        questionNumber = randint(1, questionCount)
        questionResponse = getQuestion(questionNumber)

        WouldYouRatherEmbed = discord.Embed(title="Would You Rather...",
                                            colour=discord.Colour(0x0696EF),
                                            description=f"> {questionResponse[0]}\n OR..\n> {questionResponse[1]}")

        WouldYouRatherEmbed.set_footer(text=f"Would You Rather • Question ID: {questionNumber}")

        await ctx.respond(embed=WouldYouRatherEmbed)


def setup(bot):
    bot.add_cog(commandHandler(bot))
