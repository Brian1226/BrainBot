import discord
from discord.ext import commands
import requests

class Image(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def jail(self, ctx, member:discord.Member = None):
        if not member:
            member = ctx.author
        if member.avatar:
            response = requests.get(f"https://api.popcat.xyz/jail?image={member.avatar.url}")
            await ctx.send(response.url)
        else:
            await ctx.send("User has no avatar!")

    @commands.command()
    async def hue(self, ctx, degree, member:discord.Member = None):
            if not member:
                member = ctx.author
            if member.avatar:
                response = requests.get(f"https://api.popcat.xyz/hue-rotate?img={member.avatar.url}&deg={degree}")
                await ctx.send(response.url)
            else:
                await ctx.send("User has no avatar!")

    @commands.command()
    async def sadcat(self, ctx,  *, text):
        response = requests.get(f"https://api.popcat.xyz/sadcat?text={text}")
        await ctx.send(response.url)

    @commands.command()
    async def drake(self, ctx, *, texts):
        text1, text2 = texts.split("|")
        response = requests.get(f"https://api.popcat.xyz/drake?text1={text1}&text2={text2}")
        await ctx.send(response.url)

    @commands.command()
    async def alert(self, ctx, *, text):
        response = requests.get(f"https://api.popcat.xyz/alert?text={text}")
        await ctx.send(response.url)

    @commands.command()
    async def grave(self, ctx, member:discord.Member = None):
        if not member:
            member = ctx.author
        if member.avatar:
            response = requests.get(f"https://vacefron.nl/api/grave?user={member.avatar.url}")
            await ctx.send(response.url)
        else:
            await ctx.send("User has no avatar!")

    @commands.command()
    async def npc(self, ctx, *, texts):
        text1, text2 = texts.split("|")
        response = requests.get(f"https://vacefron.nl/api/npc?text1={text1}&text2={text2}")
        await ctx.send(response.url)

    @commands.command()
    async def sign(self, ctx, *, text):
        response = requests.get(f"https://vacefron.nl/api/peeposign?text={text}")
        await ctx.send(response.url)

    @commands.command()
    async def carreverse(self, ctx, *, text):
        response = requests.get(f"https://vacefron.nl/api/carreverse?text={text}")
        await ctx.send(response.url)

async def setup(client):
    await client.add_cog(Image(client))