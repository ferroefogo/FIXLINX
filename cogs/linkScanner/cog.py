import nextcord
from nextcord.ext import commands
import re

xfix = "https://fxtwitter.com/"
twtfix = "https://fixupx.com/"
url_regex = r'(https?://[^\s]+)'

class LinkScannerCog(commands.Cog, name="Link Scanner"):
    def __init__(self, bot: commands.Bot):
        self.__bot = bot

    def fix_url(self, match):
        url = match.group(1)
        if "twitter.com" in url:
            return twtfix + url.replace("https://twitter.com/", "")
        elif "x.com" in url:
            return xfix + url.replace("http://x.com/", "")

    @commands.Cog.listener()
    async def on_message(self, message: nextcord.Message):
        if not message.author.bot:
            # Avoid infinite loop.
            fixed_string = re.sub(url_regex, self.fix_url, message.content)
            await message.channel.send(fixed_string)

def setup(bot):
    bot.add_cog(LinkScannerCog(bot))
