# Work with Python 3.6
import discord
import random

TOKEN = 'NTUxNDM1ODE5NjQ3MjM4MTkw.D1xCTQ.jYtsxz0_Qyr69gD7Zx8FqObc0hY'

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content == ('!help'):
        msg=[]
        #POPULATE WITH COMMANDS
        await client.send_message(message.channel, msg)

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if (message.content.lower().startswith('owo') or message.content.lower().startswith('uwu')):
        msg = 'Hewwo {0.author.mention}'.format(message) + " senpai, you're vewy kawaii-desu."
        await client.send_message(message.channel, msg) #this is cursed, blame the weeb dev

    if "I'm" in message.content:
        msg = "Hi " + message.content[message.content.find("I'm")+4:] + ", I'm LudiBot!"
        await client.send_message(message.channel, msg)

    if message.content.startswith('!degenerate'):
        msg = message.content[12:]
        msg = msg.replace('r','w')
        msg = msg.replace('ove','uv')
        msg = msg.replace('l','w')
        await client.send_message(message.channel, msg)

    if message.content.startswith('!members'):
        msg = '__All current members are:__ \n \n'
        x = message.server.members
        for member in x:
            name = member.name
            msg = msg + name + '\n'
        await client.send_message(message.channel, msg)

    if message.content.startswith('!roles'):
        members = message.server.members
        msg = ''
        for member in members:
            msg = msg + '**' + member.name + '**' + '\'s highest role is ' + member.top_role.name + '\n \n'
        await client.send_message(message.channel, msg)

    if message.content.startswith('!eldest'):
        members = message.server.members
        oldMan = ''
        oldest = list(members)[0].joined_at
        for member in members:
            if member.joined_at < oldest:
                oldest = member.joined_at
                oldMan = member.name
        msg = oldMan + ' is the oldie of the chat! Respect your elders! He joined ' + oldest.strftime("%A, %B %d %Y @ %H:%M:%S %p")
        await client.send_message(message.channel, msg)

    if message.content.startswith('!baby'):
        members = message.server.members
        baby = ''
        youngest = list(members)[0].joined_at
        for member in members:
            if member.joined_at > youngest:
                youngest = member.joined_at
                baby = member.name
        msg = baby + ' is the baby of the chat! He joined ' + youngest.strftime("%A, %B %d %Y @ %H:%M:%S %p")
        await client.send_message(message.channel, msg)

    if message.content.startswith('?random'):
        limit = message.content[message.content.find("?random")+8:]
        msg = random.randint(1,int(limit))
        await client.send_message(message.channel, msg)

    if message.content.startswith('!degenerate'):
        msg = message.content[12:]
        msg = msg.replace('r','w')
        msg = msg.replace('ove','uv')
        msg = msg.replace('l','w')
        await client.send_message(message.channel, msg)

    if message.content.startswith('!comp'):
        compFile = open("comp.txt", "r")
        compliment = [comp for comp in compFile]
        msg = compliment[random.randint(0,len(compliment)-1)]
        await client.send_message(message.channel, msg)
        
    if message.content.startswith('!cleanse'):
        num = int(message.content[9:])
        async for x in client.logs_from(message.channel, limit = num+1):
            await client.delete_message(x)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


client.run(TOKEN)
