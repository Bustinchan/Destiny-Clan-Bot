import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

def connect():
    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')


    intents = discord.Intents.default()
    client = discord.client.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} has connected to Discord!')


    client.run(TOKEN)

connect()