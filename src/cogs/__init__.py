"""
Init Cogs file
"""

from discord.ext.commands import Bot

from ._admin import AdminCog
from ._rcon import RconCog


async def setup_cogs(bot: Bot):
    """
    Setup cogs
    """

    await bot.add_cog(RconCog(bot))
    await bot.add_cog(AdminCog(bot))
