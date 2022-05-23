from nextcord.ext import commands
# Made by JustIanJ and codeman1o1.

class EventHandler(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot


def setup(bot: commands.Bot):
    bot.add_cog(EventHandler(bot))
