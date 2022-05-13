# TIJK-Bot Games is made and maintained by JustIanJ and codeman1o1

import os
import nextcord
from nextcord.ext import commands
from dotenv import load_dotenv

bot = commands.Bot()


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    print("I'm Alive")


load_dotenv()
bot.run(os.getenv("BOT_TOKEN"))
