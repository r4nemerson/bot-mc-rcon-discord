import discord

from discord.ext import commands
from discord import app_commands

from mcrcon import MCRcon

from setup import setup


class RconCog(commands.Cog):
    """
    Minecraft RCON Cog
    """

    def __init__(self, bot):
        self.bot = bot


    @app_commands.command(
        name="rcon",
        description="Execute a Minecraft RCON command"
    )
    @app_commands.describe(
        command="Minecraft command to execute"
    )
    async def rcon(
        self,
        interaction: discord.Interaction,
        command: str
    ):

        # evita timeout do Discord
        await interaction.response.defer()


        try:
            with MCRcon(
                setup.rcon_host,
                setup.rcon_password,
                port=setup.rcon_port
            ) as rcon:

                response = rcon.command(command)


            embed = discord.Embed(
                title="🎮 Minecraft RCON",
                description="Command executed successfully",
                color=discord.Color.green()
            )


            embed.add_field(
                name="Command",
                value=f"```{command}```",
                inline=False
            )


            embed.add_field(
                name="Response",
                value=f"```{response or 'No response'}```",
                inline=False
            )


            embed.set_footer(
                text=f"Executed by {interaction.user}"
            )


            await interaction.followup.send(
                embed=embed
            )


        except Exception as error:

            embed = discord.Embed(
                title="❌ RCON Error",
                description="Failed to execute command",
                color=discord.Color.red()
            )


            embed.add_field(
                name="Error",
                value=f"```{error}```",
                inline=False
            )


            await interaction.followup.send(
                embed=embed,
                ephemeral=True
            )

    @app_commands.command(
        name="say",
        description="Send a message to the Minecraft server chat"
    )
    @app_commands.describe(
        message="Message to send"
    )
    async def say(
        self,
        interaction: discord.Interaction,
        message: str
    ):
        await interaction.response.defer()

        try:
            username = interaction.user.display_name

            tellraw = (
                f'tellraw @a '
                f'{{"text":"[Discord] {username}: {message}","color":"green"}}'
            )

            with MCRcon(
                setup.rcon_host,
                setup.rcon_password,
                port=setup.rcon_port
            ) as rcon:

                response = rcon.command(tellraw)


            embed = discord.Embed(
                title="💬 Minecraft Chat",
                description="Mensagem enviada com sucesso",
                color=discord.Color.blue()
            )

            embed.add_field(
                name="Message",
                value=f"```{message}```",
                inline=False
            )

            embed.set_footer(
                text=f"Enviada por {interaction.user}"
            )

            await interaction.followup.send(
                embed=embed
            )

        except Exception as error:

            embed = discord.Embed(
                title="❌ Chat Error",
                description="Failed to send message",
                color=discord.Color.red()
            )

            embed.add_field(
                name="Error",
                value=f"```{error}```",
                inline=False
            )

            await interaction.followup.send(
                embed=embed,
                ephemeral=True
            )
