import nextcord
from nextcord.ext import commands

formats_fixes = {
    "twitter.com": "fx",
    "x.com": "fixup"
}

class LinkScannerCog(commands.Cog, name="Link Scanner"):
    def __init__(self, bot: commands.Bot):
        self.__bot = bot


    @commands.Cog.listener()
    async def on_message(self, message: nextcord.Message):
        # Check link format against fixes
        for format, fix in formats_fixes.items():
            msg_start_index = message.content.find(format)
            if msg_start_index != -1:
                if format == "x.com":
                    new_content = "https://" + fix + message.content[msg_start_index:]
                elif format == "twitter.com":
                    new_content = "https://" + fix + message.content[msg_start_index:]
        # Known twt link formats: www.twitter.com/..., www.x.com/...
        message.edit(new_content)


def setup(bot):
    bot.add_cog(LinkScannerCog(bot))
