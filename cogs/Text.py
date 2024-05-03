import discord
from discord.ext import commands
import requests

class Text(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def hello(self, ctx):
        await ctx.send("Hello, chat!")

    @commands.command()
    async def pickupline(self, ctx):
        response = requests.get("https://api.popcat.xyz/pickuplines")
        pickupline = response.json()["pickupline"]

        embed = discord.Embed(title="Pickup Line", url="", description=pickupline, color=0xFF2400)
        embed.set_author(name=ctx.author.display_name, url="", icon_url=ctx.author.avatar.url)
        embed.set_thumbnail(url="https://cdn-icons-png.flaticon.com/128/3939/3939673.png")
        embed.set_footer(text="Hmm, I wonder...Can Brian come up with good pickup lines? :)")
        await ctx.send(embed=embed)

    @commands.command()
    async def dm(self, ctx, member:discord.Member, *, message="Hello!"):
        embed = discord.Embed(title=message)
        await member.send(embed=embed)

    @commands.command()
    async def joke(self, ctx):
        response = requests.get("https://api.popcat.xyz/joke")
        joke = response.json()["joke"]
        embed = discord.Embed(title="Joke", url="", description=joke, color=0x9966CC)
        embed.set_author(name=ctx.author.display_name, url="", icon_url=ctx.author.avatar.url)
        embed.set_thumbnail(url="https://cdn-icons-png.flaticon.com/128/5129/5129605.png")
        embed.set_footer(text=f"Brian is a joke :)")
        await ctx.send(embed=embed)

    @commands.command()
    async def wyr(self, ctx):
        response = requests.get("https://api.popcat.xyz/wyr")
        ops1 = response.json()["ops1"]
        ops2 = response.json()["ops2"]
        embed = discord.Embed(title="Would you rather...", url="", description="", color=0x1E90FF)
        embed.set_author(name=ctx.author.display_name, url="", icon_url=ctx.author.avatar.url)
        embed.set_thumbnail(url="https://cdn-icons-png.flaticon.com/128/5726/5726308.png")
        embed.add_field(name="Option 1", value=ops1, inline=True)
        embed.add_field(name="Option 2", value=ops2, inline=True)
        embed.set_footer(text=f"I bet Brian is still thinking :)")
        await ctx.send(embed=embed)

    @commands.command()
    async def translate(self, ctx, lang, *, text):
        response = requests.get(f"https://api.popcat.xyz/translate?to={lang}&text={text}")
        translation = response.json()["translated"]
        await ctx.send(translation)

    @commands.command()
    async def _8ball(self, ctx, *, msg):
        response = requests.get("https://api.popcat.xyz/8ball")
        answer = response.json()["answer"]
        embed = discord.Embed(title=msg, url="", description=answer, color=0xC0C0C0)
        embed.set_author(name=ctx.author.display_name, url="", icon_url=ctx.author.avatar.url)
        embed.set_thumbnail(url="https://cdn-icons-png.flaticon.com/128/12338/12338789.png")
        embed.set_footer(text=f"Maybe ask something like, 'is Brian cool? :)")
        await ctx.send(embed=embed)

    @commands.command()
    async def affirmation(self, ctx):
        response = requests.get("https://www.affirmations.dev/")
        affirmation = response.json()["affirmation"]
        embed = discord.Embed(title="Affirmation", url="", description=affirmation, color=0xFF9966)
        embed.set_author(name=ctx.author.display_name, url="", icon_url=ctx.author.avatar.url)
        embed.set_thumbnail(url="https://cdn-icons-png.flaticon.com/128/2573/2573337.png")
        embed.set_footer(text=f"Brian wishes you the best <3")
        await ctx.send(embed=embed)

    @commands.command()
    async def advice(self, ctx):
        response = requests.get("https://api.adviceslip.com/advice")
        advice = response.json()["slip"]["advice"]
        embed = discord.Embed(title="Advice", url="", description=advice, color=0xFFFDD0)
        embed.set_author(name=ctx.author.display_name, url="", icon_url=ctx.author.avatar.url)
        embed.set_thumbnail(url="https://cdn-icons-png.flaticon.com/128/4185/4185489.png")
        embed.set_footer(text=f"Hopefully, Brian's advices are helpful :)")
        await ctx.send(embed=embed)

    @commands.command()
    async def activity(self, ctx):
        response = requests.get("https://www.boredapi.com/api/activity")
        activity = response.json()["activity"]
        embed = discord.Embed(title="Activity", url="", description=activity, color=0x50C878)
        embed.set_author(name=ctx.author.display_name, url="", icon_url=ctx.author.avatar.url)
        embed.set_thumbnail(url="https://cdn-icons-png.flaticon.com/128/4852/4852363.png")
        embed.set_footer(text=f"Brian hopes you find something fun!")
        await ctx.send(embed=embed)

async def setup(client):
    await client.add_cog(Text(client))