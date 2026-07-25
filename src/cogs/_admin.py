from discord.ext import commands
from discord.ext.commands import Bot
import discord

from setup import setup


class AdminCog(commands.Cog):

    def __init__(self, bot: Bot):
        self.bot = bot


    @commands.command(name="sync")
    @commands.is_owner()
    async def sync(self, ctx):

        commands = await self.bot.tree.sync()

        await ctx.send(
            f"✅ Sincronizados {len(commands)} comandos na guild"
        )

        print("Comandos sincronizados:")
        for command in commands:
            print(f"- {command.name}")