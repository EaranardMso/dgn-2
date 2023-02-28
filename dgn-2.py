import discord
import os
from discord.ext import commands
from discord.ext.commands import Bot

token = os.environ['TOKEN']
intents = discord.Intents.default()
intents.message_content = True

bot = Bot(intents=intents, command_prefix="`")

@bot.event
async def on_ready():
    print("We have logged in as {0.user}".format(bot))
    print("--------------------------------------------")

@bot.command()
async def hello(ctx):
    await ctx.send("Hello! I am a bot!")

bot.run(token)