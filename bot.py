import discord
from discord.ext import commands

# Set up the bot with a command prefix
intents = discord.Intents.default()
intents.messages = True  # Allow message reading (required for some commands)

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')

@bot.command()
async def hello(ctx):
    await ctx.send("Hello! I'm a bot!")
