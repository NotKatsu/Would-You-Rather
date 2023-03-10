import discord
from discord.ext import commands

bot = commands.Bot(status=discord.Status.online)


@bot.event
async def on_ready():
    print(f"{bot.user.name}#{bot.user.discriminator} Is now Online.")


if __name__ == "__main__":
    extensions = ["cogs.databaseHandler", "cogs.commandHandler"]
    for extension in extensions:
        bot.load_extension(extension)

bot.run("TOKEN")
