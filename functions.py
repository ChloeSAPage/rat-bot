import requests
import discord
import random
import io


def get_num_rat_pics():
    '''Get amount of rat pics available from Rat API'''
    response = requests.get("http://localhost:5000/get-pic-amount")

    # Check response code
    if response.status_code == 200:
        num_rat_pics = int(response.content.decode("utf-8"))
        return num_rat_pics
    else:
        # await message.channel.send(f"Failed to retrieve rat image: {response.status_code} {response.reason}")
        print(f"Failed to retrieve rat image: {
            response.status_code} {response.reason}")
        custom_reason = response.headers.get("Description")
        if custom_reason:
            # await message.channel.send(f"Custom Reason: {custom_reason}")
            print(f"Custom Reason: {custom_reason}")
        return 0


async def send_rat_pic(message, num_rat_pics):
    '''Send Rat Pic in Discord'''
    num_rat_pics = int(num_rat_pics)
    # Get random number and format to 2 digits e.g. 02
    random_number = random.choice(range(1, num_rat_pics + 1))
    if random_number < 10:
        random_number = str(random_number).zfill(2)

    # Get Rat pic from API
    response = requests.get(f"http://localhost:5000/get-rat/{random_number}")

    if response.status_code == 200:
        image_data = response.content
        picture = discord.File(io.BytesIO(image_data),
                               filename=f"rat_{random_number}.jpg")
        await message.channel.send(file=picture)

    else:
        print(f"Failed to retrieve rat image: {
            response.status_code} {response.reason}")
        custom_reason = response.headers.get("Description")
        if custom_reason:
            print(f"Custom Reason: {custom_reason}")


async def send_rat_fact(message):
    '''Get rat fact from Rat API'''
    response = requests.get(f"http://localhost:5000/get-rat-facts")

    if response.status_code == 200:
        rat_facts = response.json()
        random_number = random.randint(1, len(rat_facts)- 1)
        await message.channel.send(rat_facts[f"{random_number}"])
