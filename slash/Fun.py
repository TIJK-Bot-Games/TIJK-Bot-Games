from cgitb import text
import nextcord
from nextcord.ext import commands
from nextcord import Interaction, slash_command as slash
from views.buttons.link import Link

from main import SLASH_GUILDS


class Fun(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @slash(guild_ids=SLASH_GUILDS)
    async def whatami(self, interaction: Interaction):
        """Tells you what you are"""
        embed = nextcord.Embed(color=0x0DD91A)
        embed.add_field(
            name="Tells you what you are.",
            value="You are a silly goose.",
            inline=False,
        )
        await interaction.response.send_message(
            embed=embed ("You are a silly goose.")
        )


def setup(bot: commands.Bot):
    bot.add_cog(Fun(bot))
