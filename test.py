import discord
from discord.ext import commands
import os
#type: ignore

client = commands.Bot(command_prefix="$", intents=discord.Intents.all())


#readying the bot for commands
@client.event
async def on_ready():
  print('The bot is now ready to take commands mistrss')
  print('----------------------')


@client.command()
#look into what ctx means
async def hello(ctx):
  await ctx.send("Hi I'm Frenbot, I'm here to with whatever you need! :3")


discord_bot_token = os.environ['SECRET_DISCORD']
client.run(discord_bot_token)
