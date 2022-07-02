#from asyncio import events
#from cgi import test
#from email import message
#from email.mime import image
from io import BytesIO
from mimetypes import init
from multiprocessing.sharedctypes import Value
from sqlite3 import Timestamp
from sys import builtin_module_names, prefix
from textwrap import indent
from turtle import color, title
from unicodedata import name
from unittest import async_case
import discord
import time
import requests, os
import random
import discord
import colorama
from colorama import Fore
import time
from time import sleep
#~#~##import nextcord
from nextcord.ext import commands
#~#~##from discord.ext import commands, tasks
from itertools import cycle
import random
import aiohttp
fro#~#~##m io import BytesIO
import #~#~##json
from datetime import datetime 
import youtube_dl
import #~#~##asyncio
from pystyle import Colors, Colorate
from pystyle import Write
from disc#~#~##ord_slash import SlashCommand
import httpx

os#~#~##.system("title Hosting Through my pc :( ")
#~#~##
os#~#~##.system("cls")


client = commands.Bot(command_prefix = (","),help_command=None)
s#~#~##lash = SlashCommand(client, sync_commands=True)

pla#~#~##yers = {}

@#~#~##client.event
async def on_ready():
    await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Activity(type=discord.ActivityType.streaming, name="DMDGO GANG BANG SESSION", url="https://www.twitch.tv/zeusonwaterfire"))
    Write.Print(f"""
#~#~##██████╗ ██╗███████╗██████╗  █████╗       ███████╗██╗  ██╗██╗██████╗ 
██╔══██╗██║╚══███╔╝██╔══██╗██╔══██╗      ██╔════╝██║ ██╔╝██║██╔══██╗
██████╔╝██║  ███╔╝ ██║  ██║███████║█████╗███████╗█████╔╝ ██║██║  ██║
██╔═══╝ ██║ ███╔╝  ██║  ██║██╔══██║╚════╝╚════██║██╔═██╗ ██║██║  ██║
██║     ██║███████╗██████╔╝██║  ██║      ███████║██║  ██╗██║██████╔╝
╚═╝     ╚═╝╚══════╝╚═════╝ ╚═╝  ╚═╝      ╚══════╝╚═╝  ╚═╝╚═╝╚═════╝ By @GotRipped\n\n{client.user} = Online | Prefix = /\n\n""", Colors.red_to_yellow, interval=0.000001)


@slash.s#~#~##lash(description="We know the game and we're gonna play it.")
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'Kicked {member.mention} Reason: {reason}')

@slash.sl#~#~##ash(description="Never gonna give you up, never gonna let you down")
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Banned {member.mention} Reason: {reason}')

@slash.#~#~##slash(description="And if you ask me how I'm feeling, don't tell me you're too blind to see.")
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member, *, reason=None):
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="muted")

    if not mutedRole:
        mutedRole = await guild.create_role(name ="muted")

        for channel in guild.channels:
            await channel.set_permissions(mutedRole, speak=False, sned_messages=False, read_message_history=True, read_messages=True)

    await member.add_roles(mutedRole, reason=reason)
    await ctx.send(f"Muted {member.mention} Reason: {reason}")
    await member.send(f"You were muted in **{guild.name}** *Reason*: {reason}")

@slash.sl#~#~##ash(description="Never gonna make you cry, never gonna say goodbye")
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member):
    mutedRole = discord.utils.get(ctx.guild.roles, name="muted")

    await member.remove_roles(mutedRole)
    await ctx.send(f"Unmuted {member.mention}")

@sla#~#~##sh.slash(description="Never gonna run around and desert you")
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member):
    bannedUsers = await ctx.guild.bans()
    name, discriminator = member.split('#')
    
    for ban in bannedUsers:
        user = ban.user

        if (user.name, user.discriminator) == (name, discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return

@slash.#~#~##slash(description="Never gonna tell a lie and hurt you.")
async def webho0k(ctx, *, webhook):
    webhook = discord.utils.get(webhook), requests.delete(webhook)
    webho0k = await ctx.send(f"*Succesfully deleted* ||**{webhook}**||")
    await asyncio.sleep(2)
    await webho0k.delete()

@sla##~#~##~#~##sh.slash(description="Chechk If Toucan Is Valid.")
async #~#~##def cktoucan(ctx, message):
    if message != None:
        resp = httpx.get("https://discord.com/api/v9/users/@me/channels", headers={"Authorization": message})
        if resp.status_code == 200:
            token = "**Valid**"
        elif resp.status_code == 401:
            token = "**Invalid**"
        elif resp.status_code == 403:
            token = "**Locked**"
        await ctx.send(f"~~Toucan~~: ||**{message}**|| ► {token}")

@sla#~#~###~#~###~#~##sh.slash(description="Never gonna run around and desert you")
asyn#~#~##c def check(ctx, *, webhook):
    webhook = requests.get(webhook)
    if webhook.status_code == 404:
        checkedniggerhookunv = await ctx.send(f"**Not Valid**")
        await asyncio.sleep(2)
        await checkedniggerhookunv.delete
    elif webhook.status_code == 200:
        checkedniggerhook = await ctx.send(f"**Valid**")
        await asyncio.sleep(2)
        await checkedniggerhook.delete

@#~#~##slash.slash(description="Never gonna run around and desert you")
as#~#~##ync def sex(ctx):
    niggermaxy_snicker6083 = await ctx.send(f"yes i would love some baba gurl!")
    await asyncio.sleep(3)
    await niggermaxy_snicker6083.delete()

@slash#~#~##.slash(description="Never gonna make you cry, never gonna say goodbye")
async d#~#~##ef sexy(ctx):
    delete_sexy52 = await ctx.send(f"*yesyes* **im sexy** you not **L**. ||respectfully 🥶||")
    await asyncio.sleep(3)
    await delete_sexy52.delete()

@slash#~#~##.slash(description="Your heart's been aching, but you're too shy to say it")
@comm#~#~##ands.has_permissions(administrator=True)
async def guirhgiulhrg6fugehXXXactivity(ctx, *, activty):
    await client.change_presence(activity=discord.Game(name=activty))
    delete_me5 = await ctx.send(f"Bot's activity is succesfully changed to: **{activty}**")
    await asyncio.sleep(1.4)
    await delete_me5.delete()

@slash#~#~##.slash(description="We've known each other for so long")
@commands.has_permissions(administrator=True)
async #~#~##def ghost(ctx):
    delete_me_daddy_ping = await ctx.send(f"@everyone ||nigger 🥶||")
    await asyncio.sleep(0.1)
    await delete_me_daddy_ping.delete()

@sl#~#~##ash.slash(description="(Ooh, give you up, ooh, give you up)..")
asy#~#~##nc def whois(ctx,user:discord.Member=None):
    embed = discord.Embed(colour=user.color,timestamp=ctx.message.created_at)

    embed.set_author(name=f"{user}'s Info"),
    embed.set_thumbnail(url=user.avatar_url),
    embed.set_footer(text=f'Requested by - {ctx.author}', icon_url=ctx.author.avatar_url)

    emb#~#~##ed.add_field(name='ID:', value=user.id,inline=False)
    embed.add_field(name='Name:', value=user.display_name,inline=False)

    e#~#~##mbed.add_field(name='Created At:', value=user.created_at,inline=False)
    em#~#~##bed.add_field(name='Joined At:', value=user.joined_at,inline=False)

    embed.add_field(name='Is He/It A Bot?:', value=user.bot,inline=False)

    await ctx.send(embed=embed)

@slash.slash(description="Never gonna tell a lie and hurt you.")
async#~#~## def download(ctx):
    delete_to0ls = await ctx.send('<#963520997208760341> **or** <#963522567728164884> **-** https://github.com/V4NSH4J/discord-mass-DM-GO/releases/tag/v1.9.2')
    aw#~#~##ait asyncio.sleep(8)
    await delete_to0ls.delete()


snip#~#~##e_message_author = {}
snipe_message_content = {}
 #~#~#~#~####
@client.event
async def on_message_delete(message):
   #~#~##  snipe_message_author[message.channel.id] = message.author
     snipe_message_content[message.channel.id] = message.content
     await sleep(1)
    #~#~## del snipe_message_author[message.channel.id]
     del snipe_message_content[message.channel.id]
 
@slash.slash(description="Never gonna tell a lie and hurt you.")
asyn#~#~##c def snipe(ctx):
    channel = ctx.channel 
    try:
   #~#~##     snipeEmbed = discord.Embed(title=f"Latest deleted message in #{channel.name}", description = snipe_message_content[channel.id])
        snipeEmbed.set_footer(text=f"Sniped a reindeer: @{snipe_message_author[channel.id]}")
        await ctx.send(embed = snipeEmbed)
#~#~##
    except:
        delete_me3 = await ctx.send(f"There are no deleted messages in #{channel.name}.")
        await asyncio.sleep(1.4)
        await delete_me3.delete()


@s#~#~##lash.slash(description="Never gonna give you up, never gonna let you down")
@com#~#~##mands.has_permissions(manage_emojis=True)
async def steal(ctx, url:str, *, name):
    guild = ctx.guild
    async with aiohttp.ClientSession() as ses:
     #~#~##   async with ses.get(url) as r:
            try:
                imgOrGif = BytesIO(await r.read())
                bValue = imgOrGif.getvalue()
             #~#~##   if r.status in range(200, 299):
                    emoji = await guild.create_custom_emoji(image=bValue, name=name)
                    delete_emoji_message_stoled = await ctx.send('Emoji successfully stoled!')
                    await asyncio.sleep(1)
                    await delete_emoji_message_stoled.delete()
                    await ses.close()
                else:
                    delete_error_emoji = await ctx.send(f'An unexpected error were shown ;-;, check my perms/sent link/prob bad/invalid link | **Error {r.status} **')
                    await asyncio.sleep(1)
                    await delete_error_emoji.delete()
            except nextcord.HTTPException:
                delete_2thic = await ctx.send('The file is 2 thicc')
                await asyncio.sleep(1)
                await delete_2thic.delete()

@sl#~#~##ash.slash(name='purge', description="Never gonna give you up, never gonna let you down")
@com#~#~##mands.has_permissions(administrator=True)
asy#~#~##nc def purge(ctx, amount, arg:str=None):
    await#~#~## ctx.channel.purge(limit=int(amount))
    message#~#~##_to_delete = await ctx.send(f'Deleted amount of messages **{amount}**!')
    awa#~#~##it asyncio.sleep(1)
    await #~#~##message_to_delete.delete()

@purg#~#~##e.error
async#~#~## def purge_error(ctx, error):
    i#~#~##f isinstance(error, commands.MissingPermissions):
      #~#~##  await ctx.send('**You have no perms to purge messages in this server**.')
    el#~#~##if isinstance(error, commands.MissingRequiredArgument):
        #~#~##delete_me = await ctx.send('**Pls make sure to input how many message you would like to purge**.')
        #~#~##await asyncio.sleep(1)
        a#~#~##wait delete_me.delete()

@slash#~#~##.slash(description="Inside we both know what's been going on")
async de#~#~##f howto(ctx):
    de#~#~##lete_helpme = await ctx.send('*How To*? - https://youtu.be/9HX64DHJYWI \n *How To Embed*? - https://youtu.be/3m56RTbThbg **(1:50)** \n *New Works Or Nah*? - https://youtu.be/rEQgHi4YZKM **([currently] *yes works*)**')
    await#~#~## asyncio.sleep(7)
    awai#~#~##t delete_helpme.delete()

@cl#~#~##ient.c#~#~##ommand(name='help')
async def help(ctx):
   #~#~## nigggggggaaaaaa = await ctx.send(f"Run \"/\"**commmands** not \",\" nigga https://tenor.com/view/lamar-franklin-lamar-roasts-franklin-gif-20079680")
    a#~#~##wait ctx.message.delete()
    #~#~##~#~###await asyncio.sleep(2)
    await n#~#~##igggggggaaaaaa.delete()

#~#~##@slash.slash(description="Never gonna make you cry, never gonna say goodbye")
#~#~##async def commands(ctx):
#~#~##    embed = discord.Embed(
#~#~##        title = 'My sexy commands | Click Me For Free Tokns + Proxies <3',
#~#~##        url= 'https://bit.ly/dmdgo-help',
#~#~##        description = '\n'
#~#~##    )
#~#~##    embed.set_footer(text=f'Github・@V4NSH4J, @unfamous',icon_url='https://cdn.discordapp.com/attachments/944894882856701973/965586889388212304/DMDGO_BEST.gif')
#~#~##    embed.set_image(url='https://cdn.discordapp.com/attachments/961296471502774353/963451578755481610/unknown.png')
#~#~##    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/961296471502774353/963452273239932958/unknown.png')
#~#~##    embed.add_field(name='Mod', value='`ban`, `kick`, `unban`, `mute` `unmute` `purge`, `guirhgiulhrg6fugehXXXactivity`')
#~#~##    embed.add_field(name='Pub/Fun', value='`snipe`, `steal`, `whois`, `sex`, `sexy`, ',inline=False)
#~#~##    embed.add_field(name='Support', value='`howto`, `download`', inline=False)
 #~#~##   embed.add_field(name='InMadeTools', value='`webho0k`, `check, cktoucan`\n \n https://discord.gg/dmdgo')
 #~#~##   await ctx.send(embed=embed)

#~#~##client.run('BOTS TOKEN IN HERE!!!!!')


























#####ALL Rights Reserved To Gingest <3 | Github = @lemmebe <3
#Current Dc server: discord.gg/vcc & discord.gg/termsofservice <~~ maybe taken by some nft faggot :|
#Telegram $~~> print("https://t.me/lemmekms + t.me/tosviolators")

#~#~## Don't check the imports :crying_lmfao:





#I don't like to give my sexy bot sources away so u have to delete the # by  urself faggot <3.
