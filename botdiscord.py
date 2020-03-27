import discord
import asyncio

ws_url = 'ws://Guesser-Cluster.scoder12.repl.co'
guess_url = 'https://guess-it.scoder12.repl.co/guess'

client = discord.Client()

@client.event
async def on_ready():
    print("yo bro !") 
    
@client.event
async def on_message(message):
    if message.content == "!hello":
        await message.channel.send("Bonjour Humain")
    if message.content == "!carapuce":
        await message.content.send == "Beurkkkk":
    print(message.content)



client.run("NjU4NjU3MTczMTM1Njg3NzA5.Xn4czQ.rfBTqUZT9zIyBJ1A3dGQo3mkSLo")
