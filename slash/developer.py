import nextcord
from nextcord.application_command import SlashOption
from nextcord import Interaction, slash_command as slash
from nextcord.ext import commands
from main import SLASH_GUILDS
from slash.custom_checks import is_bot_owner


class Developer(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @slash(guild_ids=SLASH_GUILDS)
    @is_bot_owner()
    async def leave_server(
        self, interaction: Interaction, server_id: str = SlashOption(required=False)
    ):
        """Remove TIJK Bot Games from a server"""
        if server_id:
            try:
                server_id = int(server_id)
            except ValueError:
                embed = nextcord.Embed(color=0xFFC800, title="Invalid server ID!")
                await interaction.response.send_message(embed=embed, ephemeral=True)
                return
            if guild := nextcord.utils.get(self.bot.guilds, id=server_id):
                await guild.leave()
                embed = nextcord.Embed(color=0x0DD91A, title=f"Left {guild.name}")
                await interaction.response.send_message(embed=embed)
            else:
                embed = nextcord.Embed(
                    color=0xFFC800, title="That is not a guild or I am not in it!"
                )
                await interaction.response.send_message(embed=embed, ephemeral=True)
        else:
            embed = nextcord.Embed(color=0x0DD91A)
            servers = "\n".join(
                f"> {GUILD.name} (**{GUILD.id}**)" for GUILD in self.bot.guilds
            )
            embed.add_field(name="Available servers:", value=servers)
            await interaction.response.send_message(embed=embed, ephemeral=True)

def setup(bot: commands.Bot):
    bot.add_cog(Developer(bot))

