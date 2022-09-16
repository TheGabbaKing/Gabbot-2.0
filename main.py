import discord
import os
from dotenv import load_dotenv #dotenv is used for the .env file 
from discord.ext import commands


#### INITIALISATION ####
load_dotenv() #loads all the varaiables in the .env file
bot = commands.Bot(debug_guilds=[524776650945200138]) #debug_guilds serverID of test server (remove debug_guilds during production)
bot = commands.Bot(intents=discord.Intents.all())


bot.load_extension('cogs.commands')

#### COMMANDS/EVENTS ####
@bot.event 
async def on_ready(): 
    print(f"{bot.user} is ready and online!") #prints in the console that the bot is online

@bot.slash_command(name="hello", description="say hello to the bot")
async def say_hello(ctx):
    await ctx.respond("Hey!") #directly replies to the user who used the slash command

bot.run(os.getenv('TOKEN')) # run the bot with the token


