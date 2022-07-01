import nextcord
from nextcord.application_command import SlashOption
from nextcord import Interaction, slash_command as slash
from views.buttons.link import Link
from views.buttons.renew import Renew
from nextcord.ext import commands
from main import SLASH_GUILDS


class Developer(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot


def setup(bot: commands.Bot):
    bot.add_cog(Developer(bot))
