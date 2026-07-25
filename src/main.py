import discord
from discord.ext import commands

from cogs import setup_cogs
from setup import setup


class Bot(commands.Bot):
    """
    Bot class
    """

    def __init__(self):
        super().__init__(
            command_prefix="!",
            intents=discord.Intents.all()
        )

    async def setup_hook(self):
    
        await setup_cogs(self)
        await self.tree.sync()

bot = Bot()
bot.run(setup.bot_token)
