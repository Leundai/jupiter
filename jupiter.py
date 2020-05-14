# jupiter
import os

import discord
import requests
import io
import aiohttp
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
        f'Hi {member.name}, welcome to my playground!'
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
    elif message.content.startswith('!ragecat'):
        # I added another gif, its pretty random xD
        await message.channel.send(f'ahh type faster', file=discord.File('cat_typing.gif'))

    elif message.content.startswith('!cat'):
        # Sometimes random.cat gives us gifs
        url = None
        for _ in range(3):
            try:
                r = requests.get('http://aws.random.cat/meow')
                r.raise_for_status()
            except:
                continue

            url = r.json()['file']
            if not url.endswith('.gif'):
                break
            else:
                return message.channel.send(r.status_code + ' Cat not found :(')

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                if resp.status != 200:
                    return await message.channel.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await message.channel.send(file=discord.File(data, 'cat.jpg'))

client.run(TOKEN)
