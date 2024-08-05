import discord
from discord.ext import commands
import os
#type: ignore
\
#setting bot command prefix and intents
client = commands.Bot(command_prefix="$", intents=discord.Intents.all())


#readying the bot for commands
@client.event
async def on_ready():
  print('The bot is now ready to take commands mistrss')
  print('----------------------')


#hello client command
@client.command()
#look into what ctx means
async def hello(ctx):
  await ctx.send("Hi I'm Frenbot, I'm here to help with whatever you need! :3")



#member join event
@client.event
async def on_member_join(member):
  channel = client.get_channel(1268253320980598889)
  await channel.send('Hello')


#member leave event
@client.event
async def on_member_remove(member):
  channel = client.get_channel(1268253320980598889)
  await channel.send('Goodbye')


discord_bot_token = os.environ['SECRET_DISCORD']
client.run(discord_bot_token)
