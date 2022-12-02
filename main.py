import discord
 
intents = discord.Intents.all()
client = discord.Client(command_prefix='!', intents=intents)
 
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
 
@client.event
async def on_message(message):
    print("message-->", message)
    if message.author == client.user:
        return
 
    if message.content.startswith('Salut'):
        await message.channel.send('Salut!,comment je peux vous aider ')
    if message.content.startswith('jai un question concernant si jai le hiv'):
        await message.channel.send('Okey,Te sens-tu fatigué?(oui/non)')
    if message.content.startswith('oui') or  message.content.startswith('non'):
        await message.channel.send('Avez-vous Sueurs nocturnes?(Oui1/Non1)')
    if message.content.startswith('Oui1') or  message.content.startswith('Non1'):
        await message.channel.send('Avez-vous Ganglions lymphatiques fortement gonflés, pas seulement au niveau du cou?(OUI2/NON2)')
    if message.content.startswith('OUI2') or  message.content.startswith('NON2'):
        await message.channel.send('Avez-vous Maux de gorge?(Oui3/Non3)')
    if message.content.startswith('Oui3') or  message.content.startswith('Non3'):
        await message.channel.send('Avez-vous  Eruption cutanée(OuI4/NOn4)')
    if message.content.startswith('OuI4') or  message.content.startswith('NOn4'):
        await message.channel.send('Ecrire result to voire ton resultat')
    if message.content.startswith('result'):
        await message.channel.send('Vous avez hiv aller au hopital')
 
client.run('MTA0ODAyODgzMzk2Nzc3OTg2MQ.GJKx4_.QMp0-fGN03J-x-AcjhudxQAeaREEiMl7AEyJCc')