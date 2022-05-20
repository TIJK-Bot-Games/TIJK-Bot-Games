import nextcord
from nextcord.ext import commands
from nextcord import Interaction, slash_command as slash
from views.buttons.link import Link

from main import SLASH_GUILDS


class General(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @slash(guild_ids=SLASH_GUILDS)
    async def github(self, interaction: Interaction):
        """Send a link to the official TIJK Bot Games GitHub page"""
        embed = nextcord.Embed(color=0x0DD91A)
        embed.add_field(
            name="View the official TIJK Bot Games code now!",
            value="https://github.com/TIJK-Bot-Games/TIJK-Bot-Games",
            inline=False,
        )
        await interaction.response.send_message(
            embed=embed, view=Link("https://github.com/TIJK-Bot-Games/TIJK-Bot-Games")
        )

class Fun(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @slash(guild_ids=SLASH_GUILDS)
    async def github(self, interaction: Interaction):
        """Tells you what you are"""
        embed = nextcord.Embed(color=0x0DD91A)
        embed.add_field(
            name="Tells you what you are.",
            value="You are a silly goose.",
            inline=False,
        )
        await interaction.response.send_message(
            embed=embed, view=Link("You are a silly goose.")
        )


def setup(bot: commands.Bot):
    bot.add_cog(General(bot))
