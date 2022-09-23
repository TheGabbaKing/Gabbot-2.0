import discord
import os
from dotenv import load_dotenv #dotenv is used for the .env file 
from discord.ext import commands
from discord.commands import Option 


#### INITIALISATION ####
load_dotenv() #loads all the varaiables in the .env file
bot = commands.Bot(command_prefix="g.") #(debug_guilds [serverID]) of test server (remove debug_guilds during production)
bot = commands.Bot(intents=discord.Intents.all())


bot.load_extension('cogs.commands')

#### COMMANDS/EVENTS ####
@bot.event 
async def on_ready(): 
    print(f"{bot.user} is ready and online!") #prints in the console that the bot is online

bot.run(os.getenv('TOKEN')) # run the bot with the token



