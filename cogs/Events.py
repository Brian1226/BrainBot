from discord.ext import commands

class Events(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, member):
        await member.guild.system_channel.send(f"Welcome, {member}")

    # @commands.Cog.listener()
    # async def on_message(self, message):
    #     if message.content == "deez":
    #         await message.delete()
    #         await message.channel.send("Message deleted!")
    #     await self.client.process_commands(message)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        await member.guild.system_channel.send(f"Bye, {member}")

async def setup(client):
    await client.add_cog(Events(client))