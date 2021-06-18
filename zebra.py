import discord 
import os 
import shutil


try:
    os.system('color')
    os.system('mode con: cols=150 lines=46')
except:
    pass

def prRed(prt): print("\033[91m {}\033[00m" .format(prt))
def prGreen(prt): print("\033[92m {}\033[00m" .format(prt))

def padToCenter(l:list,w:int)->str:
    padding =  ' '*(w//2)
    parts = [ padding[0: (w-len(p))//2+1]+p for p in l]
    return '\n'.join(parts)


# put your token between the quotes below
token = ""

zebra = """              ████████                                                      
      ██      ██  ░░░░██  ██                                                
    ██  ██    ██  ░░░░████  ██                                              
    ██  ██    ██░░░░▒▒██    ██                                              
    ██    ██  ██████████    ██                                              
      ██  ████    ████    ██  ██                                            
        ██  ██  ██      ██░░  ████                                          
        ██  ██  ██        ██░░██  ██                                        
        ██  ██  ██        ██▒▒██  ██                                        
      ██                    ██    ████                                      
      ██                    ██░░██  ██                                      
      ██  ██    ██            ████    ██                                    
      ██  ██    ██              ██░░████                                    
      ██              ██          ████  ██                                  
      ████              ██      ██  ██░░██                                  
    ████          ██▓▓    ██  ██      ██░░██                                
    ██                ██  ██        ██  ████        ████████████            
    ██████████        ██░░██      ██      ██████████  ██    ██  ██          
  ██░░░░░░░░░░██  ░░░░░░██      ██      ██  ██  ██      ██    ██  ██        
  ██░░░░░░░░▒▒░░██░░▒▒██░░    ░░      ██    ██    ██    ██    ██    ████    
  ██░░██░░██░░▒▒██████  ▓▓░░  ░░░░  ██░░    ██  ░░██    ██    ██    ██  ██  
  ██░░░░░░░░░░░░██  ░░  ▓▓░░░░░░    ░░      ██    ██    ██  ░░██    ██  ██  
    ██▒▒▒▒▒▒▒▒▒▒██        ████████          ██    ██    ██    ██    ██    ██
      ██████████          ██░░            ██      ██    ██    ██    ██    ██
                          ██░░      ██          ██    ██    ██      ██  ██  
                          ██████████        ██                    ████  ██  
                          ██░░              ██    ██    ██      ██  ██  ██  
                          ██░░        ██    ██    ██    ██    ██    ██      
                          ████████████    ██      ██    ██          ██      
                            ██                  ██    ██      ██    ██      
                            ██    ██      ██▒▒░░░░░░░░░░░░░░██      ██      
                            ██░░  ████    ██████████████████░░      ██      
                              ██  ██  ██  ██          ██▒▒░░██████  ██      
                              ██████  ██████          ██████░░██░░    ██    
                              ██  ██  ██  ██            ██░░░░████░░████    
                              ██████  ██████            ██░░████  ██    ██  
                              ██  ██  ██  ██              ██░░██    ██  ██  
                              ██  ██  ██  ██              ██░░██    ██░░██  
                              ██░░██  ██░░██              ██░░██    ██░░██  
                              ██████  ██████              ██████    ██████  
                              ██████  ██████              ██████    ██████  
                                      ░░                            ░░      
                    ░░    ░░                  ░░░░  ░░░░░░                  
"""

class zebra(discord.Client):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.token = token
        self.zebra = zebra
        
    
    async def on_message(self, message):
        
        if message.author != self.user:
            return
        
        if message.content == "cl":
            async for msg in message.channel.history(limit=9999).filter(lambda m: m.author == self.user).map(lambda m: m):
                try:
                    await msg.delete()
                except:
                    pass
            prGreen("Cleared messages")
        
        elif message.content == "cleardms":
            for channel in self.private_channels:
                if isinstance(channel, discord.DMChannel):
                    async for msg in message.channel.history(limit=9999).filter(lambda m: m.author == self.user).map(lambda m: m):
                        try:
                            await msg.delete()
                        except:
                            pass
                    prGreen("Cleared chat with: " + str(channel.recipient))
        
        elif message.content == ".sv":
            for channel in message.guild.channels:
                if isinstance(channel, discord.TextChannel):
                    if channel.permissions_for(message.author).send_messages:
                        async for msg in channel.history(limit=9999).filter(lambda m: m.author == self.user).map(lambda m: m):
                            try:
                                await msg.delete()
                            except:
                                pass
            prGreen("Cleared messages in: " + str(message.guild.name))
        
        elif message.content == "clearservers":
            for guild in self.guilds:
                for channel in guild.channels:
                    if isinstance(channel, discord.TextChannel):
                        if channel.permissions_for(message.author).send_messages:
                            async for msg in channel.history(limit=9999).filter(lambda m: m.author == self.user).map(lambda m: m):
                                try:
                                    await msg.delete()
                                except:
                                    pass
            prGreen("Cleared all servers")
        
        elif message.content == "clearaccount":
            for guild in self.guilds:
                for channel in guild.channels:
                    if isinstance(channel, discord.TextChannel):
                        if channel.permissions_for(message.author).send_messages:
                            async for msg in channel.history(limit=9999).filter(lambda m: m.author == self.user).map(lambda m: m):
                                try:
                                    await msg.delete()
                                except:
                                    pass
                            prGreen(f"Cleared {channel.guild.name} channel:  {channel.name}")
            # if you read this javin is poor
            # balls in his mouth
            # javins mouth btw
            for guild in self.guilds:
                prGreen(f"Left server: {guild.name}")
                try:
                    await guild.leave()
                except:
                    await guild.delete()
            
            for channel in self.private_channels:
                if isinstance(channel, discord.DMChannel):
                    async for msg in channel.history(limit=9999).filter(lambda m: m.author == self.user).map(lambda m: m):
                        try:
                            await msg.delete()
                        except:
                            pass
                    user = channel.recipient
                    try:
                        await user.remove_friend() 
                    except:
                        pass
                    prGreen(f"Removed Friend: {user}")       
                if isinstance(channel, discord.GroupChannel):
                    await channel.leave()
                    prGreen(f"Left GroupChat: {channel.name}")
            
            prGreen("Cleared account")
    
    async def on_command_error(self, ctx, e):
        pass
                    
    async def on_connect(self):
        width = shutil.get_terminal_size().columns
        
        print (padToCenter(zebra.splitlines(),width))
        print ("----------------------------------------".center(width))
        print (f"Yeehaw: {self.user}".center(width))
    
    def run(self):
        super().run(self.token, bot=False)

if __name__ == "__main__":
    zebra = zebra()
    zebra.run()

