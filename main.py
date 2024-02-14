import discord
from dotenv import load_dotenv
import os
from functions import send_rat_pic

# Load Token
load_dotenv()
TOKEN = os.getenv("RATBOT_TOKEN")

# Intents
intents = discord.Intents.default()
intents.message_content = True

# Bot
bot = discord.Client(intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')


@bot.event
async def on_message(message):
    # Check the message is from a user
    if message.author == bot.user:
        return

    # Responds to messages starting with '!'
    if message.content.startswith("!ratpic"):
        await send_rat_pic(message)


bot.run(TOKEN)
