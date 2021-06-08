import discord
token = 'INSERT TOKEN HERE'

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)
prefix = "*"


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_member_join(member):
    case = member.name.lower()
    if '.com/' in case:
        await member.kick()


client.run(token)
