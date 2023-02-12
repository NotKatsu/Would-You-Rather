import sqlite3

import random
import discord
from discord.ext import commands
from discord.commands import SlashCommandGroup

connection = sqlite3.connect("WouldYouRather.db")
cursor = connection.cursor()


class databaseHandler(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        WouldYouRatherOptions = [
            {"option_one": "Never see or talk to anyone ever again.",
             "option_two": "Have to handshake everyone you ever meet."},
            {"option_one": "Be rich but you can't make anymore money ever again.",
             "option_two": "Be poor but you can make as much money as you want."},
            {"option_one": "Have telekinesis (the ability to move things with your mind).",
             "option_two": "Telepathy (the ability to read minds)."},
            {"option_one": "Have the ability to see 10 minutes into the future.",
             "option_two": "150 years into the future."},
            {"option_one": "Team up with Wonder Woman.", "option_two": "Captain Marvel."},
            {"option_one": "Be in jail for five years.", "option_two": "Be in a coma for a month."},
            {"option_one": "Swim in a pool full of Nutella.", "option_two": "A pool full of maple syrup."},
            {"option_one": "Buy 10 things you don't need every time you go shopping.",
             "option_two": "Always forget the one thing that you need when you go to the store."},
            {"option_one": "Never be able to go out during the day.",
             "option_two": "Never be able to go out at night."},
            {"option_one": "Be royalty 1,000 years ago.", "option_two": "An average person today."},
            {"option_one": "Wear the same socks for a month.", "option_two": "The same underwear for a week."},
            {"option_one": "Always be 10 minutes late.", "option_two": "Always be 20 minutes early."},
            {"option_one": "Spend a week in the forest.", "option_two": "a night in a real haunted house."},
            {"option_one": "Always have a full phone battery.", "option_two": "Always have a full gas tank."},
            {"option_one": "Be forced to live the same day over and over again for a full year.",
             "option_two": "Take 3 years off the end of your life."}
        ]

        cursor.execute("""CREATE TABLE IF NOT EXISTS questions (
                          optionOne VARCHAR(255),
                          optionTwo VARCHAR(255)
                          )""")

        for question in WouldYouRatherOptions:
            cursor.execute('SELECT optionOne FROM questions WHERE optionOne = ?', (question["option_one"],))

            if cursor.fetchone() is None:
                cursor.execute('INSERT INTO questions(optionOne, optionTwo) VALUES(?, ?)',
                               (question["option_one"], question["option_two"]))
                connection.commit()
                print("Inserted Question")


def setup(bot):
    bot.add_cog(databaseHandler(bot))
