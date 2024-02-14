import requests
import discord
import random
import io

# Request how many rat pics are available

'''async def get_num_rat_pics(message):
        # Get amount of rat pics available
    response = requests.get("http://localhost:5000/get-pic-amount")
    
    # Check response code
    if response.status_code == 200:
        num_rat_pics = int(response.content.decode("utf-8"))
        return num_rat_pics
    else:
        await message.channel.send(f"Failed to retrieve rat image: {response.status_code} {response.reason}")
        custom_reason = response.headers.get("Description")
        if custom_reason:
            await message.channel.send(f"Custom Reason: {custom_reason}")
        return 0'''


async def send_rat_pic(message):
    # Get amount of rat pics available
    response = requests.get("http://localhost:5000/get-pic-amount")
    
    # Check response code
    if response.status_code == 200:
        num_rat_pics = int(response.content.decode("utf-8"))
    else:
        await message.channel.send(f"Failed to retrieve rat image: {response.status_code} {response.reason}")
        print(f"Failed to retrieve rat image: {response.status_code} {response.reason}")
        custom_reason = response.headers.get("Description")
        if custom_reason:
            await message.channel.send(f"Custom Reason: {custom_reason}")
            print(f"Custom Reason: {custom_reason}")