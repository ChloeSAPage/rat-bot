import discord
from dotenv import load_dotenv
import os
from functions import send_rat_pic, get_num_rat_pics, send_rat_fact

# Load Token
load_dotenv()
TOKEN = os.getenv("RATBOT_TOKEN")

# Intents
intents = discord.Intents.default()
intents.message_content = True

# Bot
bot = discord.Client(intents=intents)

# Number of rat pics available
num_rat_pics = get_num_rat_pics()


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
        if num_rat_pics == 0:
            await message.channel.send("I don't have any Rat Pics :(")
        await send_rat_pic(message, num_rat_pics)

    if message.content.startswith("!ratfact"):
        await send_rat_fact(message)


bot.run(TOKEN)
