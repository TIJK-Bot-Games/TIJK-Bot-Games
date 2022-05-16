# TIJK-Bot Games is made and maintained by JustIanJ and codeman1o1

# importing libs
import nextcord
import os
from nextcord.ext import commands
from dotenv import load_dotenv

load_dotenv()
bot = commands.Bot()


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    for cog in os.listdir("cogs"):
        try:
            bot.load_extension("cogs." + cog.strip(".py"))
            print(f"Loaded {cog}")
        except Exception as e:
            print(e)
            print(f"{cog} couldn't be loaded")


# ping cmd
@bot.command()
async def ping(ctx):
    await ctx.channel.send("pong")


if __name__ == "__main__":
    bot.run(os.getenv("BOT_TOKEN"))
