import os, asyncio
import nextcord
from nextcord.ext import commands
import config


def main():
    # init Intents to allow bots to interact with Members, Presence and Guilds
    intents = nextcord.Intents.all()
    client = commands.Bot(intents=intents, help_command=None)

    
    @client.event
    async def on_ready():   
        print(f"{client.user.name} has connected to Discord.")
        await client.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.watching, name="chat"))
        #await sync_commands()
        for guild in client.guilds:
            print(guild.name)
    
    
    async def count_servers():
        await client.wait_until_ready()
        while not client.is_closed():
            print(f"{str(len(client.guilds))} servers joined.")
            await asyncio.sleep(24*60*60) # wait 24 hours


    # load all cogs
    for folder in os.listdir("cogs"):
        if os.path.exists(os.path.join("cogs", folder, "cog.py")):
            client.load_extension(f"cogs.{folder}.cog")
    
    
    '''USE THIS FOR DEBUGGING COMMANDS OR WHEN CREATING NEW ONES (WILL ONLY SYNC TO SPECIFIED GUILD)'''
    # async def sync_commands():
    #     await client.sync_application_commands(guild_id = config.GUILD)

    
    # Check how many servers the bot is in every 24 hours
    client.loop.create_task(count_servers())
    
    # run the bot
    client.run(config.BOT_TOKEN)


if __name__ == "__main__":
    main()
