# TIJK-Bot Games is made and maintained by JustIanJ and codeman1o1
import nextcord
from nextcord import ButtonStyle, Interaction, Button
from nextcord.ext import commands


class Renew(nextcord.ui.View):
    def __init__(self, bot: commands.Bot = None):
        super().__init__()
        self.bot = bot

    @nextcord.ui.button(label="Renew", style=ButtonStyle.blurple)
    async def renew(self, button: Button, interaction: Interaction):
        await interaction.message.edit(
            content=f"The latency of TIJK Bot Games is {self.bot.latency * 1000}ms"
        )
