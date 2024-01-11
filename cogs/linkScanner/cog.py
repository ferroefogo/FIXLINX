import nextcord
from nextcord.ext import commands
import re

xfix = "https://fxtwitter.com/"
twtfix = "https://fixupx.com/"

class LinkScannerCog(commands.Cog, name="Link Scanner"):
    def __init__(self, bot: commands.Bot):
        self.__bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: nextcord.Message):
        if not message.author.bot:
            # Avoid infinite loop.
            if "fxtwitter.com/" not in message.content and "fixupx.com/" not in message.content:
                # Avoid already fixed links.
                if "twitter.com/" in message.content:
                    new_msg = message.content.replace("twitter.com/", "fxtwitter.com/")
                    await message.channel.send(new_msg)
                elif "x.com/" in message.content:
                    new_msg = message.content.replace("x.com/", "fixupx.com/")
                    await message.channel.send(new_msg)

def setup(bot):
    bot.add_cog(LinkScannerCog(bot))
