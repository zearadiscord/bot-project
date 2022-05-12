import discord
from discord.ext import commands

client = discord.Client()

@client.event
async def on_message(message):
  if message.content == "test":
    await message.channel.send("test")
client.run()
