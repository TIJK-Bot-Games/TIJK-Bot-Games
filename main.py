# TIJK-Bot Games is made and maintained by JustIanJ and codeman1o1

# importing libs
import nextcord
import os
from nextcord.ext import commands
from dotenv import load_dotenv
from nextcord import slash_command as slash
from nextcord import Interaction
from nextcord.application_command import SlashOption
from views.buttons.link import Link
import requests
import datetime
import random

client = nextcord.Client()
bot = commands.Bot(
    command_prefix=".",
    case_insensitive=True,
    strip_after_prefix=True,
    help_command=None,
    intents=nextcord.Intents.all(),
)

load_dotenv()
bot = commands.Bot()

SLASH_GUILDS = (870973430114181141, 865146077236822017)


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


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    print("I'm Alive")
