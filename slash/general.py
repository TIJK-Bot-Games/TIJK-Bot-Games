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
    async def avatar(self, ctx, *, user: nextcord.Member = None):
        """ Get the avatar of you or someone else """
        user = user or ctx.author

        avatars_list = []

        def target_avatar_formats(target):
            formats = ["JPEG", "PNG", "WebP"]
            if target.is_animated():
                formats.append("GIF")
            return formats

        if not user.avatar and not user.guild_avatar:
            return await ctx.send(f"**{user}** has no avatar set, at all...")

        if user.avatar:
            avatars_list.append("**Account avatar:** " + " **-** ".join(
                f"[{img_format}]({user.avatar.replace(format=img_format.lower(), size=1024)})"
                for img_format in target_avatar_formats(user.avatar)
            ))

        embed = nextcord.Embed(colour=user.top_role.colour.value)

        if user.guild_avatar:
            avatars_list.append("**Server avatar:** " + " **-** ".join(
                f"[{img_format}]({user.guild_avatar.replace(format=img_format.lower(), size=1024)})"
                for img_format in target_avatar_formats(user.guild_avatar)
            ))
            embed.set_thumbnail(url=user.avatar.replace(format="png"))

        embed.set_image(url=f"{user.display_avatar.with_size(256).with_static_format('png')}")
        embed.description = "\n".join(avatars_list)

        await ctx.send(f"🖼 Avatar to **{user}**", embed=embed)

    @slash(guild_ids=SLASH_GUILDS)
    async def about(self, interaction: Interaction):
        """Tells you what TIJK Bot Games is."""
        embed = nextcord.Embed(color=0x0DD91A)
        embed.add_field(
            name="About me:",
            value="TIJK Bot Games is a Discord bot developed by JustIanJ and codeman1o1. TIJK Bot Games is going to be a fun bot to use because it is going to have a lot of fun features. It is currently under quite heavy development, so the bot is not working properly yet and the bot will have some bugs, please report those on our Github page (use /github command for the link). More content will be added later. Have fun using it!",
        )
        await interaction.response.send_message(embed=embed)

    @slash(guild_ids=SLASH_GUILDS)
    async def embed(
        self,
        interaction: Interaction,
        name: str = SlashOption(description="The name of the field", required=False),
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
