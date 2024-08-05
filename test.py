import discord
import os
from discord.ext import commands
#type: ignore

print('Goodbye cruel world')

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
client = discord.Client(intents=intents)

print('Hello world')
