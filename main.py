import discord
from discord.ext import commands
from discord import app_commands
import json
import os

# -----------------------------
# Load config.json
# -----------------------------
with open("config.json", "r") as f:
    config = json.load(f)

TOKEN = config["token"]

# -----------------------------
# Bot Setup
# -----------------------------
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(
    command_prefix="!",
    intents=intents
)

# -----------------------------
# Bot Ready
# -----------------------------
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} slash commands.")
    except Exception as e:
        print(e)

    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name="Balance SMP | /help"
        )
    )

# -----------------------------
# /ping
# -----------------------------
@bot.tree.command(
    name="ping",
    description="Shows the bot latency."
)
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(
        f"🏓 Pong! `{round(bot.latency * 1000)}ms`"
    )

# -----------------------------
# /help
# -----------------------------
@bot.tree.command(
    name="help",
    description="Shows the command list."
)
async def help_command(interaction: discord.Interaction):

    embed = discord.Embed(
        title="🌌 Equinox Help",
        description="Official Balance SMP Bot",
        color=0x5865F2
    )

    embed.add_field(
        name="Utility",
        value="""
`/help`
`/ping`
`/ticket`
`/apply`
""",
        inline=False
    )

    embed.add_field(
        name="Moderation",
        value="""
`/warn`
`/mute`
`/kick`
`/ban`
`/clear`
""",
        inline=False
    )

    embed.set_footer(text="Equinox")

    await interaction.response.send_message(embed=embed)

# -----------------------------
# Start Bot
# -----------------------------
bot.run(TOKEN)