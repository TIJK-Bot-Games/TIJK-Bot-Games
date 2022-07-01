# TIJK-Bot Games is made and maintained by JustIanJ and codeman1o1

import os
import nextcord
from dotenv import load_dotenv
from nextcord.ext import commands

load_dotenv()

client = nextcord.Client()
bot = commands.Bot(
    command_prefix=".",
    case_insensitive=True,
    strip_after_prefix=True,
    help_command=None,
    intents=nextcord.Intents.all(),
)


bot = commands.Bot()

SLASH_GUILDS = (870973430114181141, 865146077236822017)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    for cog in os.listdir("cogs"):
        if cog.endswith(".py"):
            try:
                bot.load_extension(f"cogs.{cog[:-3]}")
                print(f"Loaded {cog}")
            except Exception as e:
                print(e)
                print(f"Failed to load {cog}")


if __name__ == "__main__":
    for slash in os.listdir("slash").remove("custom_checks.py"):
        if slash.endswith(".py"):
            try:
                bot.load_extension(f"slash.{slash[:-3]}")
                print(f"Loaded {slash}")
            except Exception as e:
                print(e)
                print(f"Failed to load {slash}")
    bot.run(os.getenv("BOT_TOKEN"))