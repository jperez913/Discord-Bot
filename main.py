# Work with Python 3.6
import discord

TOKEN = 'NTUxNDM1ODE5NjQ3MjM4MTkw.D1xCTQ.jYtsxz0_Qyr69gD7Zx8FqObc0hY'

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if (message.content.lower().startswith('owo') or message.content.lower().startswith('uwu')):
        msg = 'Hewwo {0.author.mention}'.format(message) + " senpai, you're vewy kawaii-desu."
        await client.send_message(message.channel, msg) #this is cursed, blame the weeb dev

    if "I'm" in message.content:
        msg = "Hi " + message.content[message.content.find("I'm")+4:] + ", I'm pepegaBot!"
        await client.send_message(message.channel, msg)

    if message.content.startswith('!degenerate'):
        msg = message.content[12:]
        msg = msg.replace('r','w')
        msg = msg.replace('ove','uv')
        msg = msg.replace('l','w')
        await client.send_message(message.channel, msg)        

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


client.run(TOKEN)
