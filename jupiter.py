# jupiter
import os

import discord
import requests
import io
import aiohttp
from dotenv import load_dotenv
import random

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
        # if it starts with the command !ragecat
    elif message.content.startswith('!ragecat'):
        # I added another gif, its pretty random xD
        await message.channel.send(f'ahh type faster', file=discord.File('cat_typing.gif'))
    # I was just experimenting and wanted to make an 8ball feature.
    # If it starts with the command !8ball
    elif message.content.startswith('!8ball'):
        #here are the responses, we can add more or remove some
        responses = ["It is certain.",
        "It is decidedly so.",
        "Without a doubt.",
        "Yes - definitely.",
        "You may rely on it.",
        "As I see it, yes.",
        "Most likely.",
        "Outlook good.",
        "Signs point to yes.",
        "Ask again later.",
        "Better not tell you now.",
        "Concentrate and ask again.",
        "Don't count on it.",
        "My reply is no.",
        "My sources say no.",
        "It lowkey do be true.",
        "nah fam.",
        "it aint so.",
        "Hocus pocus, the answer is no.",
        "Outlook not so good.",
        "Very doubtful."]
        #here is the output
        await message.channel.send(f'{random.choice(responses)}')
    # Music recomendations
    elif message.content.startswith('!music'):
        #here are the responses, we can add more or remove some
        recomendations = ["Space Song by Beach House",
        "Greek God by Conan Grey",
        "Daunt by Jelani Aryeh",
        "Summertime In Paris by Jaden, WILLOW",
        "MARBLE TEA by Shawn Wasabi",
        "The List by Moonchild",
        "Groceries by Mallrat",
        "Always Afternoon by Medasin, Kathleen",
        "Big Jet Plane by Angus & Julia Stone",
        "That I Miss You by Vansire",
        "Nice Boys by TEMPOREX",
        "Cigarette Daydreams by Cage the Elephant",
        "How Was Your Day? by Mellow Fellow, Clairo",
        "Mountains by Message to Bears",
        "Imagination by Foster the People",
        "Spring By Two Door Cinema Club",
        "Lucy by Still Woozy, ODIE",
        "Closer by Tegan and Sara",
        "Sweet Talk by Saint Motel",
        "Let it Pass by Jakob Ogawa",
        "You're Not with Me by No Vacation"]
        #here is the output
        await message.channel.send(f'{random.choice(recomendations)}')

    # if it starts with the command !cat
    elif message.content.startswith('!cat'):
        await cat_picture(message)
    #if it starts with the command !meme
    elif message.content.startswith('!meme'):
        await meme_pics(message)
    #if it starts with the command !birb
    elif message.content.startswith('!birb'):
        await birb_picture(message)
    #if it starts with the command !memes. This is an added meme command to allow for more memes.
    elif message.content.startswith('!memes'):
        await meme_pics_two(message)

async def cat_picture(message):
    url = None
    for _ in range(3):
        try:
            #this is the part where it gets a photo from the link provided
            r = requests.get('http://aws.random.cat/meow')
            r.raise_for_status()
        except:
            continue
        # accessing the url
        url = r.json()['file']
    # aiohttp is the library we downloaded to access pics
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status != 200:
                return await message.channel.send('Could not download file...')
            data = io.BytesIO(await resp.read())
            # here is the line which sends the picture
            if url.endswith('.gif'):
                await message.channel.send(file=discord.File(data, 'cat.gif'))
            else:
                await message.channel.send(file=discord.File(data, 'cat.jpg'))

async def meme_pics(message):
    url = None
    for _ in range(3):
        try:
            #this is the part where it gets a photo from the link provided
            r = requests.get('https://meme-api.herokuapp.com/gimme')
            r.raise_for_status()
        except:
            continue
        # accessing the url
        url = r.json()['url']
    # aiohttp is the library we downloaded to access pics
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status != 200:
                return await message.channel.send('Could not download file...')
            data = io.BytesIO(await resp.read())
            # here is the line which sends the meme_pics
            if url.endswith('.png'):
                await message.channel.send(file=discord.File(data, 'meme.png'))
            else:
                await message.channel.send(file=discord.File(data, 'meme.jpg'))

async def birb_picture(message):
    url = None
    for _ in range(3):
        try:
            #this is the part where it gets a photo from the link provided
            r = requests.get('https://some-random-api.ml/img/birb')
            r.raise_for_status()
        except:
            continue
        # accessing the url
        url = r.json()['link']
    # aiohttp is the library we downloaded to access pics
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status != 200:
                return await message.channel.send('Could not download file...')
            data = io.BytesIO(await resp.read())
            # here is the line which sends the pic
            if url.endswith('.gif'):
                await message.channel.send(file=discord.File(data, 'birb.gif'))
            else:
                await message.channel.send(file=discord.File(data, 'birb.jpg'))

async def meme_pics_two(message):
    url = None
    for _ in range(3):
        try:
            #this is the part where it gets a photo from the link provided
            r = requests.get('https://some-random-api.ml/meme')
            r.raise_for_status()
        except:
            continue
        # accessing the url
        url = r.json()['id']
    # aiohttp is the library we downloaded to access pics
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status != 200:
                return await message.channel.send('Could not download file...')
            data = io.BytesIO(await resp.read())
            # here is the line which sends the meme_pics_two
            if url.endswith('.jpg'):
                await message.channel.send(file=discord.File(data, 'meme.jpg'))
            else:
                await message.channel.send(file=discord.File(data, 'meme.png'))


client.run(TOKEN)
