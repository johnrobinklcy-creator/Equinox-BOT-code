import discord
from discord.ext import commands
import json

with open("config.json", "r") as f:
    config = json.load(f)

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=config["prefix"], intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} is online!")

@bot.command()
async def ping(ctx):
    await ctx.send("🏓 Pong!")

bot.run(config["token"])