# TIJK-Bot Games is made and maintained by JustIanJ and codeman1o1
import nextcord
from nextcord.application_command import SlashOption
from nextcord import Interaction, slash_command as slash
from views.buttons.link import Link
from views.buttons.renew import Renew
from nextcord.ext import commands
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

    @slash(guild_ids=SLASH_GUILDS)
    async def aboutme(self, interaction: Interaction):
        """Tells you what TIJK-Bot Games is."""
        embed = nextcord.Embed(color=0x0DD91A)
        embed.add_field(
            name="About me:",
            value="TIJK Bot Games is a Discord bot developed by JustIanJ and codeman1o1. TIJK Bot Games is going to be a fun bot to use, it has features like 8-ball. We are currently under very heavy development. So the bot is not working properly yet. More content will be added later.",
        )
        await interaction.response.send_message(embed=embed)

    @slash(guild_ids=SLASH_GUILDS)
    async def embed(
        self,
        interaction: Interaction,
        name: str = SlashOption(description="The title of the field", required=False),
        value: str = SlashOption(description="The value of the field", required=False),
    ):
        """Makes an embed"""
        embed = nextcord.Embed(color=0x0DD91A)
        embed.add_field(name=name or "", value=value or "")
        try:
            await interaction.response.send_message(embed=embed)
        except nextcord.HTTPException:
            await interaction.response.send_message(
                "The embed is invalid", ephemeral=True
            )

    @slash(guild_ids=SLASH_GUILDS)
    async def ping(self, interaction: Interaction):
        """Sends the latency of TIJK Bot Games"""
        await interaction.response.send_message(
            f"🏓 Pong! The latency of TIJK Bot Games is {self.bot.latency * 1000}ms",
            view=Renew(self.bot),
        )


def setup(bot: commands.Bot):
    bot.add_cog(General(bot))
