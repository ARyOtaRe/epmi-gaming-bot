import discord 
from discord.ext import commands
from discord.ext.commands import MissingPermissions
import datetime
from datetime import datetime

class Gaming(commands.Bot):
    async def on_ready(self):
        '''connecting'''
        await client.change_presence(activity = discord.Activity(name = "le serveur",
        type = discord.ActivityType.watching))


    async def on_message(self, message):
        if message.author == client.user:
            return 

        return await client.process_commands(message)
        

    
client =  Gaming(command_prefix = commands.when_mentioned_or('bot:'),intents=discord.Intents.all())

client.remove_command('help')


@client.command()
@commands.is_owner()
async def règles(ctx):
    embed=discord.Embed(title='Règles', description="Bienvenue sur le Discord EPMI's GAMING ! Attention, en tant que gameur.se, avant de te lancer sur ce Discord, nous te demandons de bien respecter ces règles :\n\n", color=0x460551)\
        .add_field(name='-1-',value='**Sois respectueux.se envers les autres** : les insultes ne sont pas tolérées (même convenues, même "pour rire") et pas de pseudo provoquant. Les débats religieux et politiques ne sont évidemment pas acceptés non plus.\n\n',inline=False)\
        .add_field(name='-2-',value='Ne poste pas de lien ou d\'image à contenu incorrect, choquant, inapproprié. Cela inclut les contenus sexuellement explicite/implicite. Même si cela ne te paraît pas choquant, ces posts peuvent l\'être pour d\'autres. **Respectez les sensibilités de chacun**.\n\n',inline=False)\
        .add_field(name='-3-',value='Évite d\'envoyer des spam/flood sur les salons du groupe non-appropriés, nous te demandons donc **pas de lien, emote ou tag à répétition**.\n\n',inline=False)\
        .add_field(name="-4-",value='**Vérifie bien que tu es dans le bon salon** pour communiquer avec les organisateurs et les joueurs\n\n',inline=False)\
        .add_field(name="Évidence",value='Bien sûr les modérateurs seront là pour juger les limites : n\'essaye pas d\'argumenter leurs décisions, celles-ci sont prises en commun et réfléchies avec les membres de l\'association EPMI\'s GAMING. Pour tout problème avec un membre de ce serveur, ou si tu veux faire une remarque, demande donc via message privé à un administrateur, ou modérateur connecté pour faire parvenir ta réclamation.',inline=False)\
        .add_field(name="Si tu as lu, déjà merci!",value='Maintenant clique sur l\'émoji <a:PinkVerified:1021519853024194592> pour accéder au serveur!',inline=False)\
        .set_footer(text="Le bureau de EPMI's GAMING")
    message= await ctx.send(embed=embed)
    await message.add_reaction("<a:PinkVerified:1021519853024194592>")





client.run("MTAyMTkzOTQxOTA1OTU4NTExNg.GkLkr2.gCp5JBIqt7EI5Sr6dYCVQ3VzYCWpcKOUlYKWqU")