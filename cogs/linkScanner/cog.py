import nextcord
from nextcord.ext import commands

# Twitter/X fix link strings
twtfix = "fxtwitter.com/"
xfix = "fixupx.com/"

# TikTok fix link string
tiktokfix = "vxtiktok.com/"


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
                    new_msg = message.content.replace("twitter.com/", twtfix) + " - " + message.author.mention
                    await message.channel.send(new_msg)
                    await message.delete()

                elif "x.com/" in message.content:
                    new_msg = message.content.replace("x.com/", xfix) + " - " + message.author.mention
                    await message.channel.send(new_msg)
                    await message.delete()

            elif "vxtiktok.com/" not in message.content:
                # Avoid already fixed links.
                if "tiktok.com/" in message.content:
                    new_msg = message.content.replace("tiktok.com/", tiktokfix) + " - " + message.author.mention
                    await message.channel.send(new_msg)
                    await message.delete()

def setup(bot):
    bot.add_cog(LinkScannerCog(bot))
