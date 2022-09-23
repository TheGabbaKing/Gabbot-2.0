import discord
from discord.ext import commands
from discord.commands import Option
import random
import uuid
import requests
import shutil

class Commands(discord.Cog):

    def __init__(self, bot):
        self.bot = bot

    ######### PREFIX COMMAND #########
    #@commands.command() #creates a prefixed commands
    #async def hello(self, ctx):
    #     await ctx.send("Hello")


    ######### ON MESSAGE EVENT #########
    @commands.Cog.listener()
    async def on_message(self, ctx):
        if ctx.content.startswith("https://www.instagram.com") or ctx.content.startswith("https://twitter.com"):
            url = ctx.content.split("?") #splits URL into parts
            if ctx.author.id == self.bot.user.id or ctx.author.id != 487110546223661076: #checks if the user who sent it was the bot or NOT me
                return
            elif ctx.content.startswith("https://twitter.com"):
                cutURL = url[0]
                if ctx.content.endswith("no"):
                    await ctx.channel.send(f"{url[0]}")
                else:
                    newURL = cutURL[:8] + "fx" + cutURL[8:]
                    await ctx.channel.send(f"{newURL}")
            else:
                await ctx.channel.send(f"{url[0]}")
            await ctx.delete()


    ######### PENIS SIZE #########
    @discord.slash_command(name="penis-calculator", description="Calculates your penis size")
    async def penis_size(self, ctx):
        sizes =[3, 3.25, 3.5, 3.75, 4, 4.25, 4.5, 4.75, 5, 5.25, 5.5, 5.75, 6, 6.25, 6.5, 6.75, 7, 7.25, 7.5, 7.75, 8]
        penis = random.choice(sizes)
        if penis < 5:
            await ctx.respond(f"Your penis is {penis} inches long <:gyurikekpoint:1020239117960892416>") #change this to the ftb one
        elif 5 <= penis < 6:
            await ctx.respond(f"Your penis is {penis} inches long <a:aYunkyNotbad:792248677540167700>")
        elif 6 <= penis < 7:
            await ctx.respond(f"Your penis is {penis} inches long :hot_face:")
        elif 7 <= penis < 8:
            await ctx.respond(f"Your penis is {penis} inches long <a:COCKA:824761345509294152>")
        else:
            await ctx.respond(f"Your penis is {penis} inches long <:gigachad:948481454470484048>")


    @discord.slash_command(name="parse", description="Parses URLs to remove sharing properties")
    async def parse(
        self, 
        ctx: discord.ApplicationContext, 
        url: Option(str, "Paste your URL")
        ):
        if url.startswith("https://www.instagram.com") or url.startswith("https://twitter.com"):
            userUrl = url.split("?") #splits URL into parts
            if ctx.author.id == self.bot.user.id or ctx.author.id != 487110546223661076: #checks if the user who sent it was the bot or NOT me
                return
            elif url.startswith("https://twitter.com"):
                cutURL = userUrl[0]
                newURL = cutURL[:8] + "fx" + cutURL[8:]
                await ctx.respond(f"{newURL}")
            else:
                await ctx.respond(f"{userUrl[0]}")

    @commands.command()
    async def saveimage(self, ctx):
        try:
            url = ctx.message.attachments[0].url
        except IndexError:
            print("Error: No attachments")
            await ctx.send("No attachments found!")

        else:
            if url[0:26] == "https://cdn.discordapp.com":
                r = requests.get(url, stream=True)
                fileName = f'files/{str(uuid.uuid4())}' + '.mp4'
                with open(fileName, 'wb') as outFile:
                    print("Saving file: " + fileName)
                    shutil.copyfileobj(r.raw, outFile)
                    await ctx.send(file=discord.File(f'{fileName}'))

        


def setup(bot):
    bot.add_cog(Commands(bot)) # add the cog to the bot