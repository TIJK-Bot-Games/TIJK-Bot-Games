import nextcord
import os
from dotenv import load_dotenv
from nextcord.ext import commands

load_dotenv()

# GRAB THE API TOKEN FROM THE .ENV FILE.
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
bot = commands.Bot(command_prefix=".")
