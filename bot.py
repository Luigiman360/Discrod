import discord
import yaml

class Discrod(discord.Client):
    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

client = Discrod()
config = yaml.safe_load(open("config.yml", "r"))
client.run(config["token"])
