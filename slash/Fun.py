import nextcord
import os
import json
import random
from nextcord.application_command import SlashOption
from nextcord.ext import commands
from nextcord import Interaction, slash_command as slash
from views.buttons.link import Link

# Made by JustIanJ and codeman1o1
root = os.path.abspath(os.getcwd())
eight_ball_responses = open(
    os.path.join(root, "eightball_responses.json"), "r", encoding="utf-8"
)
eight_ball_responses = tuple(json.load(eight_ball_responses)["responses"])
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
            value="You are a very silly goose!",
            inline=False,
        )
        await interaction.response.send_message(embed=embed)

    @slash(guild_ids=SLASH_GUILDS)
    async def eightball(
        self,
        interaction: Interaction,
        question=SlashOption(description="Question", required=True),
    ):
        """Rolls the magic eightball for advise."""
        embed = nextcord.Embed(color=0x0DD91A, title=question)
        embed.description = random.choice(eight_ball_responses)
        await interaction.response.send_message(embed=embed)


def setup(bot: commands.Bot):
    bot.add_cog(Fun(bot))
