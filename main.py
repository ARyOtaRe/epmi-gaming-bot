import discord 
from discord.ext import commands
from discord.ext.commands import MissingPermissions
import datetime
import json


with open('tokens.json', 'r') as token_file:
    Tokens = json.loads(token_file.read())


class Gaming(commands.Bot):
    async def on_ready(self):
        '''connecting'''
        await self.change_presence(activity=discord.Activity(name="le serveur", type=discord.ActivityType.watching))
        synced = await self.tree.sync()
        print(f"synced {len(synced)} commands!")

    async def on_message(self, message):
        if message.author == self.user:
            return

        await self.process_commands(message)

client = Gaming(command_prefix=commands.when_mentioned_or('bot:'), intents=discord.Intents.all())

@client.tree.command(name="regles", description="te mets les règles de epmi gaming")
@commands.has_permissions(administrator=True)
async def regles(ctx, channel_id:str,interaction=discord.Interaction):
    embed = discord.Embed(title='Règles', description="Bienvenue sur le Discord EPMI's GAMING ! Attention, en tant que gameur.se, avant de te lancer sur ce Discord, nous te demandons de bien respecter ces règles :\n\n", color=0x460551) \
        .add_field(name='-1-', value='**Sois respectueux.se envers les autres** : les insultes ne sont pas tolérées (même convenues, même "pour rire") et pas de pseudo provoquant. Les débats religieux et politiques ne sont évidemment pas acceptés non plus.\n\n', inline=False) \
        .add_field(name='-2-', value='Ne poste pas de lien ou d\'image à contenu incorrect, choquant, inapproprié. Cela inclut les contenus sexuellement explicite/implicite. Même si cela ne te paraît pas choquant, ces posts peuvent l\'être pour d\'autres. **Respectez les sensibilités de chacun**.\n\n', inline=False) \
        .add_field(name='-3-', value='Évite d\'envoyer des spam/flood sur les salons du groupe non-appropriés, nous te demandons donc **pas de lien, emote ou tag à répétition**.\n\n', inline=False) \
        .add_field(name="-4-", value='**Vérifie bien que tu es dans le bon salon** pour communiquer avec les organisateurs et les joueurs\n\n', inline=False) \
        .add_field(name="Évidence", value='Bien sûr les modérateurs seront là pour juger les limites : n\'essaye pas d\'argumenter leurs décisions, celles-ci sont prises en commun et réfléchies avec les membres de l\'association EPMI\'s GAMING. Pour tout problème avec un membre de ce serveur, ou si tu veux faire une remarque, demande donc via message privé à un administrateur, ou modérateur connecté pour faire parvenir ta réclamation.', inline=False) \
        .add_field(name="Si tu as lu, déjà merci!", value='Maintenant clique sur l\'émoji <a:PinkVerified:1021519853024194592> pour accéder au serveur!', inline=False) \
        .set_footer(text="Le bureau de EPMI's GAMING")
    channel = await client.fetch_channel(channel_id)  # Use fetch_channel instead of get_channel
    message = await channel.send(embed=embed)
    await interaction.response.send_message("c'est bon!")

@client.tree.command(name="coucou", description="Te dit coucou")
@commands.has_permissions(administrator=True)
async def event(interaction=discord.Interaction):
    await interaction.response.send_message("coucou!")


@client.tree.command(name="event", description="Permet de créer un évenement")
@commands.has_permissions(administrator=True)
async def event(interaction=discord.Interaction,name,description,date,channel:str,location:str,start_time:str,end_time:str,):
    print("triple monstre")




@client.event
async def on_reaction_add(reaction, user):
    Channel = client.get_channel(725402289291919362)
    if reaction.message.channel.id != Channel.id:
        return
    if str(reaction.emoji) == "<a:PinkVerified:1021519853024194592>":  # Use str() to compare emoji strings
        Role = discord.utils.get(user.guild.roles, name="one")  # Use guild.roles instead of server.roles
        await user.add_roles(Role)



client.run(Tokens["bot_token"]["token"])