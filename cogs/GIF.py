import discord
from discord.ext import commands
import requests

class GIF(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def angry(self, ctx):
        response = requests.get("https://purrbot.site/api/img/sfw/angry/gif")
        gif = response.json()["link"]
        await ctx.send(gif)

    @commands.command()
    async def bite(self, ctx):
        response = requests.get("https://purrbot.site/api/img/sfw/bite/gif")
        gif = response.json()["link"]
        await ctx.send(gif)

    @commands.command()
    async def blush(self, ctx):
        response = requests.get("https://purrbot.site/api/img/sfw/blush/gif")
        gif = response.json()["link"]
        await ctx.send(gif)
    
    @commands.command()
    async def comfy(self, ctx):
        response = requests.get("https://purrbot.site/api/img/sfw/comfy/gif")
        gif = response.json()["link"]
        await ctx.send(gif)

    @commands.command()
    async def cry(self, ctx):
        response = requests.get("https://purrbot.site/api/img/sfw/cry/gif")
        gif = response.json()["link"]
        await ctx.send(gif)

    @commands.command()
    async def cuddle(self, ctx):
        response = requests.get("https://purrbot.site/api/img/sfw/cuddle/gif")
        gif = response.json()["link"]
        await ctx.send(gif)

    @commands.command()
    async def hug(self, ctx):
        response = requests.get("https://purrbot.site/api/img/sfw/hug/gif")
        gif = response.json()["link"]
        await ctx.send(gif)

    @commands.command()
    async def kiss(self, ctx):
        response = requests.get("https://purrbot.site/api/img/sfw/kiss/gif")
        gif = response.json()["link"]
        await ctx.send(gif)

    @commands.command()
    async def lick(self, ctx):
        response = requests.get("https://purrbot.site/api/img/sfw/lick/gif")
        gif = response.json()["link"]
        await ctx.send(gif)

    @commands.command()
    async def pat(self, ctx):
        response = requests.get("https://purrbot.site/api/img/sfw/pat/gif")
        gif = response.json()["link"]
        await ctx.send(gif)

    @commands.command()
    async def poke(self, ctx):
        response = requests.get("https://purrbot.site/api/img/sfw/poke/gif")
        gif = response.json()["link"]
        await ctx.send(gif)

    @commands.command()
    async def slap(self, ctx):
        response = requests.get("https://purrbot.site/api/img/sfw/slap/gif")
        gif = response.json()["link"]
        await ctx.send(gif)

    
async def setup(client):
    await client.add_cog(GIF(client))