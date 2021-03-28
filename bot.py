import discord
import yaml

config = yaml.safe_load(open("config.yml", "r"))

class Discrod(discord.Client):
    async def on_message(self, message):
        if message.content.startswith(config['prefix']):
            args = message.content[len(config["prefix"]):].split(' ')
            print(args)
        elif "69" in message.content:
            await message.channel.send("Nice.", reference = message)

client = Discrod()
client.run(config["token"])
