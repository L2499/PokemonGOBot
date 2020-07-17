import requests
import discord
from discord.ext import commands
import requests
import bs4
from selenium import webdriver
import shutil

client = commands.Bot(command_prefix = ".")

@client.event
async def on_ready():
   print("Pokemon Bot is ready!")

@client.command(pass_context=True)
async def clear(ctx,amount=1):
    channel = ctx.message.channel
    messages = await channel.history(limit=int(amount)).flatten()
    await channel.delete_messages(messages)

@client.event
async def on_message(message):

    if message.content.startswith(".find"):
        url = "https://pokemon-go1.p.rapidapi.com/pokemon_stats.json"
        Pokemon_name = message.content.split()
        Pokemon_name = Pokemon_name[-1]
        headers = {
            'x-rapidapi-host': "pokemon-go1.p.rapidapi.com",
            'x-rapidapi-key': "d088b6503bmshdc714a4f2084684p1fa298jsne50d46634631"
        }
        # image_url_link = "https://en.wikipedia.org/wiki/"+Pokemon_name
        #
        # # soup = bs4.BeautifulSoup(requests.get(image_url_link).text, features='lxml')
        # # image = soup.find_all("img")
        # # for i in image:
        # #     print(i["src"])
        image_url = "https://img.pokemondb.net/artwork/"+Pokemon_name.lower()+".jpg"
        r = requests.get(image_url)
        with open("python_logo.png", 'wb') as f:
            f.write(r.content)
        stats_data = requests.request("GET", url, headers=headers).json()
        for i in range(0,len(stats_data)):
            if Pokemon_name == stats_data[i]["pokemon_name"] and stats_data[i]["form"]=="Normal":
                await message.channel.send(file=discord.File("python_logo.png"))
                attack = stats_data[i]["base_attack"]
                defence = stats_data[i]["base_defense"]
                stamina = stats_data[i]["base_stamina"]
                print(attack,defence,stamina)
    await client.process_commands(message)

client.run('NzMzNzgzMzI3NDU0MTM0MzIy.XxILNw.2uHLwMz4q3GNyYL1NV1DJcfRReE')