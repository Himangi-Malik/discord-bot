
import discord
import requests
import json
import random


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " - " + json_data[0]['a']
    return quote

sad_words = ["sad", "depressed", "angry", "not feeling well", "unhappy", "crying", "depressing"]

starter_encouragements = ["Cheer up!", "muggu babies support you",
                          "hang in there!", "you are a hard working person!"]

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    msg = message.content
    if message.content.startswith('$inspire'):
        quote = get_quote()
        await message.channel.send(quote) 
    
    if any(word in msg for word in sad_words ):
        await message.channel.send(random.choice(starter_encouragements))
 
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

client.run('MTE5NjQzMzE1MDM3NzczODI4MA.G-h8aZ.IAkDPYBjgDjO1mtcdEoZPnszOAlF4E6xHp5VFw')
