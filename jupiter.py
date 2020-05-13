# jupiter
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

# Whenever the discord bot starts up
@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

# Whenever a new member joins we create a new DM and say welcome to the server!
@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

# On message means that when there is a new message it process it
@client.event
async def on_message(message):
    # If the message author is not the client we are looking for (not same peep)
    if message.author == client.user:
        return
    # If it starts with the command !hello
    if message.content.startswith('!hello'):
        # Send out a message with the name of the author
        # We are limited to only using local files unless we install some new library
        await message.channel.send(f'Hello!! {message.author.name}', file=discord.File('giphy.gif'))

client.run(TOKEN)
