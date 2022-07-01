import nextcord
import os
import json
import random
from nextcord.application_command import SlashOption
from nextcord.ext import commands
from nextcord import Interaction, slash_command as slash
from main import SLASH_GUILDS

root = os.path.abspath(os.getcwd())
eight_ball_responses = open(
    os.path.join(root, "eightball_responses.json"), "r", encoding="utf-8"
)
eight_ball_responses = tuple(json.load(eight_ball_responses)["responses"])


class Fun(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @slash(guild_ids=SLASH_GUILDS)
    async def whatami(self, interaction: Interaction):
        """Tells you what you are"""
        embed = nextcord.Embed(color=0x0DD91A)
        embed.add_field(
            name="-=-=-=-=-=-=-=-=-=-=-=-",
            value="You are a very silly goose!",
            inline=False,
        )
        await interaction.response.send_message(embed=embed)

    @slash(name="8ball", guild_ids=SLASH_GUILDS)
    async def eightball(
        self,
        interaction: Interaction,
        question: str = SlashOption(description="Your question", required=True),
    ):
        """Rolls the magic 8ball for advise"""
        embed = nextcord.Embed(color=0x0DD91A, title=question)
        embed.description = random.choice(eight_ball_responses)
        await interaction.response.send_message(embed=embed)

    @slash(guild_ids=SLASH_GUILDS)
    async def headsortails(self, interaction: Interaction):
        """Throws a coin"""
        embed = nextcord.Embed(color=0x0DD91A)
        embed.add_field(name="You have got:", value=random.choice(("Heads", "Tails")))
        await interaction.response.send_message(embed=embed)

    @slash(guild_ids=SLASH_GUILDS)
    async def beverage(self, interaction: Interaction):
        """Shows you the best beverage ever made."""
        img = nextcord.File("images/beverage.jpg")
        embed = nextcord.Embed(color=0x0DD91A)
        embed.add_field(
            name="The best beverage ever made.",
            value="<3",
            inline=False,
        )
        embed.set_image(url="attachment://beverage.jpg")
        await interaction.response.send_message(embed=embed, file=img)

    @slash(guild_ids=SLASH_GUILDS)
    async def f(self, interaction: Interaction, text: str = SlashOption(required=True)):
        """Press F to pay respect"""
        hearts = ("❤", "💛", "💚", "💙", "💜")
        reason = f"for **{text}** " if text else ""
        await interaction.response.send_message(
            f"**{interaction.user.name}** has paid their respect {reason}{random.choice(hearts)}"
        )

    @slash(guild_ids=SLASH_GUILDS)
    async def hotcalc(self, ctx, *, user: nextcord.Member = None):
        """ Returns a random percent for how hot is a discord user """
        user = user or ctx.author

        random.seed(user.id)
        r = random.randint(1, 100)
        hot = r / 1.17
        
        if hot > 75:
            emoji = "💞"
        elif hot > 50:
            emoji = "💖"
        elif hot > 25:
            emoji = "❤"
        else:
            emoji = "💔"

        await ctx.send(f"**{user.name}** is **{hot:.2f}%** hot {emoji}")

    @slash(guild_ids=SLASH_GUILDS)
    async def ihavethering(self, interaction: Interaction):
        """shows you what happens when you have the ring."""
        img = nextcord.File("images/gollem.jpg")
        embed = nextcord.Embed(color=0x0DD91A)
        embed.add_field(
            name="Smeagol:",
            value="My precious <3",
            inline=False,
        )
        embed.set_image(url="attachment://gollem.jpg")
        await interaction.response.send_message(embed=embed, file=img)


def setup(bot: commands.Bot):
    bot.add_cog(Fun(bot))
