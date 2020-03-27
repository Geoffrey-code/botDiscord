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
        member_name = message.author.name
        guild_name = message.guild.name
        new_msg = await message.channel.send("Bonjour + "   +   member_name     +   " et bienvenue sur "   +   guild_name)
        await new_msg.pin()

em = discord.Embed(title="titre", description="desc", color=0xFF0000, timestamp=message.created_at)
em.add_field(name="Un field", value="Youpi", inline=True)
em.add_field(name="Un autre field", value="o/", inline=True)
em.add.field(name="Un field pas sur la même ligne", value="grâce au 'inline'", inline=False)
em.set.author(name="Un gars super", icon_url=message.author.avatar_url)
em.set.author(name="Sur un super serveur", icon_url=message.guild.icon_url)
em.set_image(url=​"https://cdn.discordapp.com/attachments/" + ​"567630033246617621/581496185424969749/1733852_0.jpg"​)
await message.channel.send(embed=em)

client.run("NjU4NjU3MTczMTM1Njg3NzA5.Xn4nGA.5yJkWLv7Y_-8ToqtUaL-bC5XJoI")
