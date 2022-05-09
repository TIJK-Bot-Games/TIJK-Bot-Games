# TIJK-Bot Games is made and maintained by JustIanJ and codeman1o1

import nextcord
from nextcord.ext import commands
from dotenv import load_dotenv
import os

bot = commands.Bot()

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

load_dotenv()
bot.run(os.getenv("BOT_TOKEN"))