import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.all()
intents.members = True

client = commands.Bot(command_prefix="!", intents=intents)

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game("Developed by Brian"))
    await setup_hook()
    print("THE BOT IS NOW READY")
    print("--------------------")

@client.event
async def setup_hook():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            cog_name = f'cogs.{filename[:-3]}'
            if cog_name not in client.extensions:
                await client.load_extension(cog_name)
                print(f"Loaded Cog: {filename[:-3]}")

if __name__ == "__main__":
    client.run(os.getenv("BOT_TOKEN"))