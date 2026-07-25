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


    rcon = app_commands.Group(
        name="rcon",
        description="Executar comandos RCON no servidor Minecraft"
    )

    @rcon.command(
        name="execute",
        description="Execute a Minecraft RCON command"
    )
    @commands.is_owner()
    async def execute(
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

    @rcon.command(
        name="say",
        description="Send a message to the Minecraft server chat"
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

    @rcon.command(
        name="status",
        description="Mostra o status do servidor"
    )
    async def status(
        self,
        interaction: discord.Interaction
    ):

        await interaction.response.defer()

        try:
            with MCRcon(
                setup.rcon_host,
                setup.rcon_password,
                port=setup.rcon_port
            ) as rcon:

                players = rcon.command("list")
                time = rcon.command(
                    "time query daytime"
                )
                difficulty = rcon.command(
                    "difficulty"
                )
                seed = rcon.command(
                    "seed"
                )

                try:
                    version = rcon.command(
                        "version"
                    )
                except:
                    version = "Não disponível"

                try:
                    tps = rcon.command(
                        "tps"
                    )
                except:
                    tps = "Não disponível"


            ticks = int(
                time.split()[-1]
            )

            periodo = (
                "☀️ Dia"
                if ticks < 13000
                else "🌙 Noite"
            )


            embed = discord.Embed(
                title="🟢 Minecraft Status",
                color=0x00ff00
            )

            embed.add_field(
                name="👥 Players",
                value=players,
                inline=False
            )

            embed.add_field(
                name="☀️ Tempo",
                value=f"{periodo} ({ticks})"
            )

            embed.add_field(
                name="⚙️ Dificuldade",
                value=difficulty
            )

            embed.add_field(
                name="🌎 Seed",
                value=seed
            )

            embed.add_field(
                name="🎮 Versão",
                value=version
            )

            embed.add_field(
                name="⚡ TPS",
                value=tps
            )


            await interaction.followup.send(
                embed=embed
            )


        except Exception as e:
            await interaction.followup.send(
                f"🔴 Servidor offline\n`{e}`"
            )
